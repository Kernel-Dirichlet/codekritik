import os
import subprocess
from collections import defaultdict, Counter
import pandas as pd

def run_command(command, cwd=None):
    """Helper function to run a shell command and return the output."""
    result = subprocess.run(command, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr.decode())
        exit(1)
    return result.stdout.decode().strip()

def is_git_repo(directory):
    """Check if a directory is a valid Git repository."""
    return os.path.exists(os.path.join(directory, '.git'))

def get_all_files_in_repo(repo_dir):
    """Get a list of all files in the repository, including nested subdirectories."""
    file_list = []
    for root, dirs, files in os.walk(repo_dir):
        for file in files:
            # Skip files inside .git directory
            if '.git' in root:
                continue
            file_list.append(os.path.relpath(os.path.join(root, file), repo_dir))
    return file_list

def calculate_code_churn_per_file(repo_dir):
    """Calculate code churn for each file in the repository."""
    command = "git log --pretty=tformat: --numstat"
    output = run_command(command, cwd=repo_dir)

    file_churn = defaultdict(lambda: {
        "lines_added": 0,
        "lines_deleted": 0,
        "total_churn": 0,
        "churn_ratio": 0,
        "churn_over_time": []
    })

    for line in output.splitlines():
        if line:
            added, deleted, filepath = line.split('\t')
            added = int(added)
            deleted = int(deleted)
            file_churn[filepath]["lines_added"] += added
            file_churn[filepath]["lines_deleted"] += deleted
            file_churn[filepath]["total_churn"] += added + deleted
            file_churn[filepath]["churn_over_time"].append((added, deleted))

    # Calculate churn ratio for each file
    for filepath, metrics in file_churn.items():
        deleted = metrics["lines_deleted"]
        metrics["churn_ratio"] = metrics["lines_added"] / deleted if deleted != 0 else "infinite"

    return dict(file_churn)

def calculate_commit_frequency(repo_dir):
    """Calculate commit frequency over time."""
    command = "git log --date=short --pretty=format:%ad"
    output = run_command(command, cwd=repo_dir)
    
    commit_dates = output.splitlines()
    commit_count = len(commit_dates)
    commit_series = pd.Series(commit_dates)
    
    # Calculate commit frequency per day, week, or month
    commit_frequency = commit_series.value_counts().sort_index()

    return commit_count, commit_frequency

def calculate_contributor_activity(repo_dir):
    """Calculate the number of commits by each contributor."""
    command = "git shortlog -s -n --all"
    output = run_command(command, cwd=repo_dir)

    contributor_activity = {}
    for line in output.splitlines():
        commits, contributor = line.strip().split('\t')
        contributor_activity[contributor.strip()] = int(commits)

    return contributor_activity

def calculate_file_changes(repo_dir):
    """Calculate how many times each file has been modified."""
    command = "git log --name-only --pretty=format:"
    output = run_command(command, cwd=repo_dir)

    file_changes = defaultdict(int)
    for line in output.splitlines():
        if line:
            file_changes[line] += 1

    return dict(file_changes)

def analyze_commit_messages(repo_dir):
    """Perform a simple keyword frequency analysis on commit messages."""
    command = "git log --pretty=format:%s"
    output = run_command(command, cwd=repo_dir)
    
    commit_messages = output.splitlines()
    keywords = ["fix",
                "bug",
                "feature",
                "refactor",
                "optimize",
                "delete",
                "add",
                "update",
                "remove",
                "security"]
    
    keyword_counter = Counter()
    for message in commit_messages:
        for keyword in keywords:
            if keyword.lower() in message.lower():
                keyword_counter[keyword] += 1

    return keyword_counter

