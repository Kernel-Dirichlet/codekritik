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


def fetch_git_history(repo_url = None,
                      local_path = None,
                      branch = 'main'): 
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
        subprocess.run(['git',
                        'clone',
                        repo_url,
                        tmp_dir],
                        check = True)
        os.chdir(tmp_dir)
    elif local_path:
        tmp_dir = None
        src = repo_url
        os.chdir(local_path)
    else:
        raise ValueError("Either an invalid GitHub URL or local dir was provided")
    print('Fetching git history from {} branch: {}...\n'.format(src,
                                                                branch))

    git_history = subprocess.run(['git',
                                  'log',
                                   branch,
                                   '--numstat',
                                   '--pretty=format:%H|%an|%ad|%s',
                                   '--date=short'],
                                   capture_output = True,
                                   text = True)
    if git_history.returncode != 0: 
        print('Failed to fetch git stats from {} branch: {}'.format(src,branch))
        print('branch might be incorrect, fetching default branch...\n')
        try:
            git_history = subprocess.run(['git',
                                          'log',
                                          '--numstat',
                                          '--pretty=format:%H|%an|%ad|%s',
                                          '--date=short'],
                                          capture_output = True,
                                          text = True)
        except:
            print('failed to fetch, URL or local repo is invalid')
            git_history = 0
            
    try:
        num_commits = subprocess.run(['git',
                                      'rev-list',
                                      '--count',
                                       branch],
                                       capture_output = True,
                                       text = True).stdout.strip()

    except:
        print('failed to fetch commit length from {} branch {}'.format(src,
                                                                       branch))
        try:
            num_commits = subprocess.run(['git',
                                          'rev-list',
                                          '--count'],
                                          capture_output = True,
                                          text = True).stdout.strip()
        except:
            print('failed to fetch, URL or local repo is invalid')
            num_commits = 0
    
    results_dict = {'git_history': git_history,
                    'num_commits': int(num_commits)}
    if tmp_dir is not None:
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir)

    return results_dict


def create_user_commit_jsons(repo_url=None, local_path=None, branch='main', since=None, until=None, base_dir='repo_analysis/users'):
    """
    Parse git history for the repo/branch and create a JSON file for each user
    under base_dir/<sanitized_user>/user_commits.json. The JSON maps commit
    hashes to a nested date->metrics dict containing:
      lines_added, lines_removed, code_churn, files_added, files_deleted,
      file_churn, fixes, docs, chores, refactors

    If repo_url is provided the repo will be cloned to a temporary directory.
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
        cmd += ['--numstat', "--pretty=format:%H|%an|%ad|%s", '--date=short']

        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=repo_path)
        if proc.returncode != 0:
            raise RuntimeError(f'git log failed: {proc.stderr}')

        lines = proc.stdout.splitlines()

        # Parse commits and collect per-file stats
        user_commits = defaultdict(dict)  # author -> {commit_hash: {date: metrics}}
        current_commit = None

        for line in lines:
            if '|' in line:
                # commit header
                parts = line.split('|', 3)
                if len(parts) < 3:
                    continue
                commit_hash, author, date = parts[0], parts[1], parts[2]
                current_commit = {
                    'hash': commit_hash,
                    'author': author,
                    'date': date,
                    'message': parts[3] if len(parts) > 3 else '',
                    'lines_added': 0,
                    'lines_removed': 0,
                    'files_added': 0,
                    'files_deleted': 0,
                    'files_changed': 0
                }
                continue

            if '\t' in line and current_commit is not None:
                try:
                    added_s, removed_s, filename = line.split('\t')
                except ValueError:
                    continue
                if added_s != '-' and removed_s != '-':
                    try:
                        added = int(added_s)
                        removed = int(removed_s)
                    except ValueError:
                        added = 0
                        removed = 0
                    current_commit['lines_added'] += added
                    current_commit['lines_removed'] += removed
                    current_commit['files_changed'] += 1
                    if added > 0 and removed == 0:
                        current_commit['files_added'] += 1
                    elif removed > 0 and added == 0:
                        current_commit['files_deleted'] += 1

            # If we hit an empty line or next header, finalize previous commit
            if current_commit is not None and (line == '' or (line.startswith('%') and '|' in line)):
                # finalize
                metrics = {
                    'lines_added': current_commit['lines_added'],
                    'lines_removed': current_commit['lines_removed'],
                    'code_churn': current_commit['lines_added'] - current_commit['lines_removed'],
                    'files_added': current_commit['files_added'],
                    'files_deleted': current_commit['files_deleted'],
                    'file_churn': current_commit['files_added'] - current_commit['files_deleted'],
                    'fixes': 1 if 'fix' in current_commit['message'].lower() or 'bug' in current_commit['message'].lower() else 0,
                    'tests': 1 if 'test' in current_commit['message'].lower() else 0,
                    'perf': 1 if 'perf' in current_commit['message'].lower() or 'performance' in current_commit['message'].lower() else 0,
                    'ci': 1 if 'ci' in current_commit['message'].lower() or 'build' in current_commit['message'].lower() else 0,
                    'feats': 1 if 'feat' in current_commit['message'].lower() or 'feature' in current_commit['message'].lower() else 0,
                    'docs': 1 if 'doc' in current_commit['message'].lower() else 0,
                    'chores': 1 if 'chore' in current_commit['message'].lower() else 0,
                    'refactors': 1 if 'refactor' in current_commit['message'].lower() or 'cleanup' in current_commit['message'].lower() else 0
                }
                # Store under author -> commit_hash -> date
                author = current_commit['author']
                commit_hash = current_commit['hash']
                date_key = current_commit['date']
                user_commits[author][commit_hash] = {date_key: metrics}
                current_commit = None

        # Edge: if last commit still pending
        if current_commit is not None:
            metrics = {
                'lines_added': current_commit['lines_added'],
                'lines_removed': current_commit['lines_removed'],
                'code_churn': current_commit['lines_added'] - current_commit['lines_removed'],
                'files_added': current_commit['files_added'],
                'files_deleted': current_commit['files_deleted'],
                'file_churn': current_commit['files_added'] - current_commit['files_deleted'],
                'fixes': 1 if 'fix' in current_commit['message'].lower() or 'bug' in current_commit['message'].lower() else 0,
                'tests': 1 if 'test' in current_commit['message'].lower() else 0,
                'perf': 1 if 'perf' in current_commit['message'].lower() or 'performance' in current_commit['message'].lower() else 0,
                'ci': 1 if 'ci' in current_commit['message'].lower() or 'build' in current_commit['message'].lower() else 0,
                'feats': 1 if 'feat' in current_commit['message'].lower() or 'feature' in current_commit['message'].lower() else 0,
                'docs': 1 if 'doc' in current_commit['message'].lower() else 0,
                'chores': 1 if 'chore' in current_commit['message'].lower() else 0,
                'refactors': 1 if 'refactor' in current_commit['message'].lower() or 'cleanup' in current_commit['message'].lower() else 0
            }
            author = current_commit['author']
            commit_hash = current_commit['hash']
            date_key = current_commit['date']
            user_commits[author][commit_hash] = {date_key: metrics}

        # Return the in-memory mapping author -> commits dict (do not write files)
        return dict(user_commits)
    finally:
        if tmp_dir and os.path.exists(tmp_dir):
            try:
                shutil.rmtree(tmp_dir)
            except Exception:
                pass


def get_active_users(branch_repo_path, since_date, until_date, branch_name):
    """
    Get all authors from the specified branch in a local repository between since_date and until_date.
    Dates are in MM-DD-YYYY format.

    Args:
        branch_repo_path: Path to the local git repository (already cloned).
        since_date: Start date in MM-DD-YYYY format.
        until_date: End date in MM-DD-YYYY format.
        branch_name: Branch to inspect.

    Returns:
        List of unique author names.
    """
    # Convert dates to Git-friendly format YYYY-MM-DD
    try:
        since_git = datetime.strptime(since_date, "%m-%d-%Y").strftime("%Y-%m-%d")
        until_git = datetime.strptime(until_date, "%m-%d-%Y").strftime("%Y-%m-%d")
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return []

    # Ensure branch exists locally
    try:
        subprocess.run(
            ["git", "rev-parse", "--verify", branch_name],
            cwd=branch_repo_path,
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError:
        print(f"Branch '{branch_name}' does not exist locally in {branch_repo_path}.")
        return []

    # Run git log only on the specific branch
    git_log_cmd = [
        "git",
        "log",
        branch_name,
        f"--since={since_git}",
        f"--until={until_git}",
        "--pretty=format:%an"
    ]

    try:
        result = subprocess.run(
            git_log_cmd,
            cwd=branch_repo_path,
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error fetching git log: {e}")
        return []

    # Deduplicate authors
    authors = set(line.strip() for line in result.stdout.splitlines() if line.strip())
    return list(authors)
    



def git_results_dump(git_stats_dict,
                     path = 'git_stats.json',
                     mode = 'full'):

    if mode == 'full':
        json.dump(git_stats_dict,open(path,'w'),indent = 4)
    if mode == 'simple':
        json.dump(git_stats_dict['user_commit_stats'],open(path,'w'),indent = 4)

def fetch_git_stats(git_history_results):
    """
    Process git history results and collect global and author-specific statistics.
    Args:
        git_history_results: Output of git log command.

    Returns:
        A dictionary containing global and author-specific stats.
    """
    commit_stats = []
    lines_by_user = defaultdict(lambda: {'lines_added': 0, 'lines_removed': 0, 'commits': 0, 'churn': 0})
    commit_frequency = defaultdict(int)
    commits_by_day = defaultdict(int)
    commits_by_week = defaultdict(int)
    commits_by_month = defaultdict(int)
    file_change_count = defaultdict(int)
    
    bug_fix_commits = []
    merge_commits = []
    feat_commits = []
    chore_commits = []
    ci_commits = []
    refactor_commits = []
    perf_commits = []
    test_commits = []

    sorted_dates = []
    authors = set()
    lines = git_history_results['git_history'].stdout.splitlines()
    current_commit = None
    total_commits = git_history_results['num_commits']  # Track the total number of lines for progress bar
    
    # Outer loop: Process each line from the git history results
    for i, line in tqdm(enumerate(lines),
                        total = len(lines),
                        desc = 'processing commit lines',
                        ncols = 100):

        if '|' in line:
            # Split commit details
            commit_hash, author, date, message = line.split('|', 3)
            current_commit = {
                'hash': commit_hash,
                'author': author,
                'date': date,
                'message': message,
                'lines_added': 0,
                'lines_removed': 0,
                'files_changed': 0
            }

            commit_stats.append(current_commit)
            lines_by_user[author]['commits'] += 1
            commit_frequency[date] += 1
            authors.add(author)
            sorted_dates.append(date)

            commit_datetime = datetime.strptime(date, '%Y-%m-%d')
            commits_by_day[commit_datetime.strftime('%m-%d-%Y')] += 1
            commits_by_week[commit_datetime.strftime('%W-%Y')] += 1
            commits_by_month[commit_datetime.strftime('%m-%Y')] += 1

            # Classify commit type
            if 'merge' in message.lower():
                merge_commits.append(current_commit)
            if 'fix' in message.lower() or 'bug' in message.lower():
                bug_fix_commits.append(current_commit)
            if 'chore' in message.lower():
                chore_commits.append(current_commit)
            if 'feat' in message.lower() or 'feature' in message.lower():
                feat_commits.append(current_commit)
            if 'refactor' in message.lower() or 'cleanup' in message.lower():
                refactor_commits.append(current_commit)
            if 'perf' in message.lower() or 'performance' in message.lower():
                perf_commits.append(current_commit)
            if 'ci' in message.lower() or 'build' in message.lower():
                ci_commits.append(current_commit)
            if 'test' in message.lower():
                test_commits.append(current_commit)

        elif '\t' in line and current_commit:
            # Handle line changes
            added, removed, filename = line.split('\t')
            if added != '-' and removed != '-':
                lines_added = int(added)
                lines_removed = int(removed)
                
                current_commit['lines_added'] += lines_added
                current_commit['lines_removed'] += lines_removed
                lines_by_user[current_commit['author']]['lines_added'] += lines_added
                lines_by_user[current_commit['author']]['lines_removed'] += lines_removed
                lines_by_user[current_commit['author']]['churn'] += lines_added + lines_removed
                current_commit['files_changed'] += 1
                file_change_count[filename] += 1

    # Initialize user commit stats using an online accumulator to avoid storing per-commit lists
    # We'll keep counts, sum, and sumsq to compute mean/std without storing all values
    user_commit_stats = defaultdict(lambda: {'lines_added': 0, 'lines_removed': 0, 'commit_count': 0, 'commit_size_sum': 0.0, 'commit_size_sumsq': 0.0})

    # Loop over commits to collect author-specific stats
    for commit in commit_stats:
        author = commit['author']
        commit_size = commit['lines_added'] + commit['lines_removed']
        user_commit_stats[author]['lines_added'] += commit['lines_added']
        user_commit_stats[author]['lines_removed'] += commit['lines_removed']
        user_commit_stats[author]['commit_count'] += 1
        user_commit_stats[author]['commit_size_sum'] += commit_size
        user_commit_stats[author]['commit_size_sumsq'] += (commit_size * commit_size)

    # Calculate stats per user and reduce payload (no per-commit arrays)
    for author, stats in list(user_commit_stats.items()):
        n = stats.get('commit_count', 0)
        if n > 0:
            mean = stats['commit_size_sum'] / n
            # population std (use sample or population? keep population for simplicity)
            variance = (stats['commit_size_sumsq'] / n) - (mean * mean)
            std = float(np.sqrt(variance)) if variance > 0 else 0.0
        else:
            mean = 0.0
            std = 0.0

        # Replace accumulator fields with compact stats
        user_commit_stats[author] = {
            'lines_added': int(stats.get('lines_added', 0)),
            'lines_removed': int(stats.get('lines_removed', 0)),
            'commits': int(n),
            'average_commit_size': round(float(mean), 2),
            'std_commit_size': round(float(std), 2)
        }
    
    # Calculate global stats
    total_lines_added = sum(commit['lines_added'] for commit in commit_stats)
    total_lines_removed = sum(commit['lines_removed'] for commit in commit_stats)
    average_commit_size = (total_lines_added + total_lines_removed) / len(commit_stats) if commit_stats else 0
    
    churn_rate = {
        'lines_added': total_lines_added,
        'lines_removed': total_lines_removed
    }

    # Prepare and return the final statistics
    commit_data = {
        'authors': list(authors),
        'lines_by_user': dict(lines_by_user),
        'user_commit_stats': dict(user_commit_stats),
        'commit_frequency': dict(commit_frequency),
        'commits_by_day': dict(commits_by_day),
        'commits_by_week': dict(commits_by_week),
        'commits_by_month': dict(commits_by_month),
        'file_change_count': dict(file_change_count),
        'churn_rate': churn_rate,
        'average_commit_size': average_commit_size,
        'merge_commits': merge_commits,
        'bug_fix_commits': bug_fix_commits,
        'feat_commits': feat_commits,
        'ci_commits': ci_commits,
        'chore_commits': chore_commits
    }

    return commit_data

