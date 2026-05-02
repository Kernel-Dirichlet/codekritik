import subprocess
import os
import sys
import shutil
import time
from tqdm import tqdm
from collections import defaultdict
from datetime import datetime, timedelta
import numpy as np
import json
import re
from collections import Counter


# ── Commit classification ─────────────────────────────────────────────────────
# Single source of truth for all commit-type keyword matching.
# Each entry: (metric_key, list_of_keywords_that_must_appear_in_message)

COMMIT_TYPE_RULES = [
    ("fixes",     ["fix:", "bug"]),
    ("tests",     ["test:"]),
    ("perf",      ["perf:", "performance"]),
    ("ci",        ["ci:", "build"]),
    ("feats",     ["feat:", "feature"]),
    ("docs",      ["doc:"]),
    ("chores",    ["chore:"]),
    ("refactors", ["refactor:", "cleanup"]),
    ("merges",    ["merge"]),
]


def classify_commit_message(message: str) -> dict:
    """
    Return a dict of commit-type flags (0 or 1) for a commit message.
    Uses COMMIT_TYPE_RULES as the single source of truth.
    """
    msg_lower = message.lower()
    result = {}
    for key, keywords in COMMIT_TYPE_RULES:
        result[key] = 1 if any(kw in msg_lower for kw in keywords) else 0
    return result


# ── fetch_git_history ─────────────────────────────────────────────────────────

def fetch_git_history(repo_url=None,
                      local_path=None,
                      branch='main'):
    '''
    Fetch git commit history from
     1) GitHub repository via URL
     2) Local Git repository
    '''
    if repo_url:
        src = repo_url
        tmp_dir = 'tmp_repo'
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir)
        subprocess.run(['git', 'clone', repo_url, tmp_dir], check=True)
        os.chdir(tmp_dir)
    elif local_path:
        tmp_dir = None
        src = local_path          # fixed: was incorrectly set to repo_url
        os.chdir(local_path)
    else:
        raise ValueError("Either an invalid GitHub URL or local dir was provided")

    print('Fetching git history from {} branch: {}...\n'.format(src, branch))

    git_history = subprocess.run(
        ['git', 'log', branch, '--numstat',
         '--pretty=format:%H|%an|%ad|%s', '--date=short'],
        capture_output=True, text=True
    )
    if git_history.returncode != 0:
        print('Failed to fetch git stats from {} branch: {}'.format(src, branch))
        print('branch might be incorrect, fetching default branch...\n')
        try:
            git_history = subprocess.run(
                ['git', 'log', '--numstat',
                 '--pretty=format:%H|%an|%ad|%s', '--date=short'],
                capture_output=True, text=True
            )
        except Exception:
            print('failed to fetch, URL or local repo is invalid')
            git_history = 0

    try:
        num_commits = subprocess.run(
            ['git', 'rev-list', '--count', branch],
            capture_output=True, text=True
        ).stdout.strip()
    except Exception:
        print('failed to fetch commit length from {} branch {}'.format(src, branch))
        try:
            num_commits = subprocess.run(
                ['git', 'rev-list', '--count'],
                capture_output=True, text=True
            ).stdout.strip()
        except Exception:
            print('failed to fetch, URL or local repo is invalid')
            num_commits = 0

    results_dict = {'git_history': git_history,
                    'num_commits': int(num_commits)}
    if tmp_dir is not None:
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir)

    return results_dict


# ── create_user_commit_jsons ──────────────────────────────────────────────────

def create_user_commit_jsons(repo_url=None, local_path=None, branch='main',
                              since=None, until=None,
                              base_dir='repo_analysis/users'):
    """
    Parse git history for the repo/branch and return a per-author mapping of
    commit_hash -> {date: metrics}.

    Metrics per commit:
        lines_added, lines_removed, code_churn,
        files_added, files_deleted, file_churn,
        + all keys from classify_commit_message()
    """
    tmp_dir = None
    try:
        if repo_url:
            tmp_dir = 'tmp_repo_user_commits'
            if os.path.exists(tmp_dir):
                shutil.rmtree(tmp_dir)
            subprocess.run(['git', 'clone', repo_url, tmp_dir], check=True)
            repo_path = tmp_dir
        elif local_path:
            repo_path = local_path
        else:
            raise ValueError('Either repo_url or local_path must be provided')

        # Build git log command
        cmd = ['git', 'log']
        if branch and branch != '--all':
            cmd.append(branch)
        if since:
            cmd.append(f'--since={since}')
        if until:
            cmd.append(f'--until={until}')
        cmd += ['--numstat', '--pretty=format:%H|%an|%ad|%s', '--date=short']

        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=repo_path)
        if proc.returncode != 0:
            raise RuntimeError(f'git log failed: {proc.stderr}')

        lines = proc.stdout.splitlines()

        user_commits = defaultdict(dict)  # author -> {commit_hash: {date: metrics}}
        current_commit = None

        def _finalize(commit):
            """Build the metrics dict for a completed commit."""
            type_flags = classify_commit_message(commit['message'])
            return {
                'lines_added':    commit['lines_added'],
                'lines_removed':  commit['lines_removed'],
                'code_churn':     commit['lines_added'] - commit['lines_removed'],
                'files_added':    commit['files_added'],
                'files_deleted':  commit['files_deleted'],
                'file_churn':     commit['files_added'] - commit['files_deleted'],
                **type_flags,
            }

        for line in lines:
            if '|' in line:
                # Finalize previous commit before starting a new one
                if current_commit is not None:
                    metrics = _finalize(current_commit)
                    user_commits[current_commit['author']][current_commit['hash']] = {
                        current_commit['date']: metrics
                    }

                parts = line.split('|', 3)
                if len(parts) < 3:
                    current_commit = None
                    continue
                current_commit = {
                    'hash':          parts[0],
                    'author':        parts[1],
                    'date':          parts[2],
                    'message':       parts[3] if len(parts) > 3 else '',
                    'lines_added':   0,
                    'lines_removed': 0,
                    'files_added':   0,
                    'files_deleted': 0,
                    'files_changed': 0,
                }
                continue

            if '\t' in line and current_commit is not None:
                try:
                    added_s, removed_s, filename = line.split('\t')
                except ValueError:
                    continue
                if added_s != '-' and removed_s != '-':
                    try:
                        added   = int(added_s)
                        removed = int(removed_s)
                    except ValueError:
                        added = removed = 0
                    current_commit['lines_added']   += added
                    current_commit['lines_removed']  += removed
                    current_commit['files_changed']  += 1
                    if added > 0 and removed == 0:
                        current_commit['files_added'] += 1
                    elif removed > 0 and added == 0:
                        current_commit['files_deleted'] += 1

        # Finalize the last pending commit
        if current_commit is not None:
            metrics = _finalize(current_commit)
            user_commits[current_commit['author']][current_commit['hash']] = {
                current_commit['date']: metrics
            }

        return dict(user_commits)

    finally:
        if tmp_dir and os.path.exists(tmp_dir):
            try:
                shutil.rmtree(tmp_dir)
            except Exception:
                pass


# ── get_active_users ──────────────────────────────────────────────────────────

def get_active_users(branch_repo_path, since_date, until_date, branch_name):
    """
    Get all authors from the specified branch in a local repository between
    since_date and until_date (MM-DD-YYYY format).
    """
    try:
        since_git = datetime.strptime(since_date, "%m-%d-%Y").strftime("%Y-%m-%d")
        until_git = datetime.strptime(until_date, "%m-%d-%Y").strftime("%Y-%m-%d")
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return []

    try:
        subprocess.run(
            ["git", "rev-parse", "--verify", branch_name],
            cwd=branch_repo_path, capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError:
        print(f"Branch '{branch_name}' does not exist locally in {branch_repo_path}.")
        return []

    git_log_cmd = [
        "git", "log", branch_name,
        f"--since={since_git}", f"--until={until_git}",
        "--pretty=format:%an"
    ]

    try:
        result = subprocess.run(
            git_log_cmd, cwd=branch_repo_path,
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error fetching git log: {e}")
        return []

    authors = set(line.strip() for line in result.stdout.splitlines() if line.strip())
    return list(authors)


# ── git_results_dump ──────────────────────────────────────────────────────────

def git_results_dump(git_stats_dict, path='git_stats.json', mode='full'):
    if mode == 'full':
        json.dump(git_stats_dict, open(path, 'w'), indent=4)
    if mode == 'simple':
        json.dump(git_stats_dict['user_commit_stats'], open(path, 'w'), indent=4)


# ── fetch_git_stats ───────────────────────────────────────────────────────────

def fetch_git_stats(git_history_results):
    """
    Process git history results and collect global and author-specific statistics.
    Uses classify_commit_message() for all commit-type detection.
    """
    commit_stats = []
    lines_by_user = defaultdict(lambda: {'lines_added': 0, 'lines_removed': 0,
                                          'commits': 0, 'churn': 0})
    commit_frequency  = defaultdict(int)
    commits_by_day    = defaultdict(int)
    commits_by_week   = defaultdict(int)
    commits_by_month  = defaultdict(int)
    file_change_count = defaultdict(int)

    # Buckets for each commit type (derived from COMMIT_TYPE_RULES)
    commit_type_buckets = {key: [] for key, _ in COMMIT_TYPE_RULES}

    sorted_dates = []
    authors = set()
    lines = git_history_results['git_history'].stdout.splitlines()
    current_commit = None

    for i, line in tqdm(enumerate(lines), total=len(lines),
                        desc='processing commit lines', ncols=100):

        if '|' in line:
            commit_hash, author, date, message = line.split('|', 3)
            current_commit = {
                'hash':          commit_hash,
                'author':        author,
                'date':          date,
                'message':       message,
                'lines_added':   0,
                'lines_removed': 0,
                'files_changed': 0,
            }

            commit_stats.append(current_commit)
            lines_by_user[author]['commits'] += 1
            commit_frequency[date] += 1
            authors.add(author)
            sorted_dates.append(date)

            commit_datetime = datetime.strptime(date, '%Y-%m-%d')
            commits_by_day[commit_datetime.strftime('%m-%d-%Y')]   += 1
            commits_by_week[commit_datetime.strftime('%W-%Y')]     += 1
            commits_by_month[commit_datetime.strftime('%m-%Y')]    += 1

            # Classify using shared function
            type_flags = classify_commit_message(message)
            for key, val in type_flags.items():
                if val and key in commit_type_buckets:
                    commit_type_buckets[key].append(current_commit)

        elif '\t' in line and current_commit:
            added, removed, filename = line.split('\t')
            if added != '-' and removed != '-':
                lines_added   = int(added)
                lines_removed = int(removed)
                current_commit['lines_added']   += lines_added
                current_commit['lines_removed']  += lines_removed
                lines_by_user[current_commit['author']]['lines_added']   += lines_added
                lines_by_user[current_commit['author']]['lines_removed'] += lines_removed
                lines_by_user[current_commit['author']]['churn']         += lines_added + lines_removed
                current_commit['files_changed'] += 1
                file_change_count[filename]     += 1

    # Per-user stats (online accumulator — no per-commit arrays stored)
    user_commit_stats = defaultdict(lambda: {
        'lines_added': 0, 'lines_removed': 0,
        'commit_count': 0, 'commit_size_sum': 0.0, 'commit_size_sumsq': 0.0
    })

    for commit in commit_stats:
        author      = commit['author']
        commit_size = commit['lines_added'] + commit['lines_removed']
        user_commit_stats[author]['lines_added']       += commit['lines_added']
        user_commit_stats[author]['lines_removed']     += commit['lines_removed']
        user_commit_stats[author]['commit_count']      += 1
        user_commit_stats[author]['commit_size_sum']   += commit_size
        user_commit_stats[author]['commit_size_sumsq'] += commit_size * commit_size

    for author, stats in list(user_commit_stats.items()):
        n = stats.get('commit_count', 0)
        if n > 0:
            mean     = stats['commit_size_sum'] / n
            variance = (stats['commit_size_sumsq'] / n) - (mean * mean)
            std      = float(np.sqrt(variance)) if variance > 0 else 0.0
        else:
            mean = std = 0.0

        user_commit_stats[author] = {
            'lines_added':          int(stats.get('lines_added', 0)),
            'lines_removed':        int(stats.get('lines_removed', 0)),
            'commits':              int(n),
            'average_commit_size':  round(float(mean), 2),
            'std_commit_size':      round(float(std), 2),
        }

    total_lines_added   = sum(c['lines_added']   for c in commit_stats)
    total_lines_removed = sum(c['lines_removed'] for c in commit_stats)
    average_commit_size = (
        (total_lines_added + total_lines_removed) / len(commit_stats)
        if commit_stats else 0
    )

    commit_data = {
        'authors':            list(authors),
        'lines_by_user':      dict(lines_by_user),
        'user_commit_stats':  dict(user_commit_stats),
        'commit_frequency':   dict(commit_frequency),
        'commits_by_day':     dict(commits_by_day),
        'commits_by_week':    dict(commits_by_week),
        'commits_by_month':   dict(commits_by_month),
        'file_change_count':  dict(file_change_count),
        'churn_rate':         {'lines_added': total_lines_added,
                               'lines_removed': total_lines_removed},
        'average_commit_size': average_commit_size,
        # Expose all commit-type buckets dynamically
        **{f'{key}_commits': val for key, val in commit_type_buckets.items()},
    }

    return commit_data
