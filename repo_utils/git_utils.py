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
    
    sorted_dates = []
    authors = set()
    lines = git_history_results['git_history'].stdout.splitlines()
    current_commit = None
    #import pdb ; pdb.set_trace()
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

    # Initialize user commit stats
    user_commit_stats = defaultdict(lambda: {'lines_added': 0, 'lines_removed': 0, 'commit_size': []})
    
    # Loop over commits to collect author-specific stats
    for commit in commit_stats:
        author = commit['author']
        commit_size = commit['lines_added'] + commit['lines_removed']
        user_commit_stats[author]['lines_added'] += commit['lines_added']
        user_commit_stats[author]['lines_removed'] += commit['lines_removed']
        user_commit_stats[author]['commit_size'].append(commit_size)
    
    # Calculate stats per user
    for author, stats in user_commit_stats.items():
        commit_sizes = stats['commit_size']
        user_commit_stats[author]['average_commit_size'] = round(np.mean(commit_sizes).item(),2) if commit_sizes else 0
        user_commit_stats[author]['std_commit_size'] = round(np.std(commit_sizes).item(),2) if commit_sizes else 0
    
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
        'commits': commit_stats,
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
        'chore_commits': chore_commits
    }

    return commit_data
    
github_results = fetch_git_history(repo_url = 'https://github.com/Kernel-Dirichlet/codekritik')
repo_results = fetch_git_stats(github_results)
git_results_dump(path = 'git_stats.json',git_stats_dict = repo_results,
                 mode = 'full')
#json.dump(repo_results,open('git_stats.json','w'),indent = 4)

