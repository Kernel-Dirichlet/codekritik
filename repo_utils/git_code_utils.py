import subprocess
import os
import shutil

def clone_repository(repo_url, clone_path):
    """
    Clone a remote git repository to a specified directory.
    If the directory exists, delete it to start fresh.
    """
    if os.path.exists(clone_path):
        print(f"Directory {clone_path} already exists. Removing it for a fresh clone.")
        shutil.rmtree(clone_path)

    subprocess.run(['git', 'clone', repo_url, clone_path], check=True)
    print(f"Cloned repository from {repo_url} to {clone_path}")

def fetch_git_history_between_dates(start_date, end_date, branch_name='main', repo_url=None, local_path=None):
    """
    Fetch git history for a specific branch between start_date and end_date.
    """
    clone_dir = "/tmp/git_repo_clone"
    if repo_url:
        clone_repository(repo_url, clone_dir)
        repo_path = clone_dir
    elif local_path:
        repo_path = local_path
    else:
        raise ValueError("Either repo_url or local_path must be provided.")

    # Checkout the specified branch
    subprocess.run(['git', 'checkout', branch_name], check=True, cwd=repo_path)

    git_command = [
        'git', 'log',
        f'--since={start_date}',
        f'--until={end_date}',
        '--numstat',
        '--pretty=format:%H|%an|%ad|%s'
    ]

    result = subprocess.run(git_command, capture_output=True, text=True, cwd=repo_path)

    if result.returncode != 0:
        raise Exception("Failed to fetch git history")

    return result.stdout.splitlines(), repo_path

def checkout_commit(commit_hash, repo_path):
    """
    Checkout a specific commit in the Git repository.
    """
    try:
        subprocess.run(['git', 'checkout', commit_hash], check=True, cwd=repo_path)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error during checkout of commit {commit_hash}: {e}")

def create_repo_stats_directory(base_dir, commit_date, commit_hash):
    """
    Create the necessary directory structure under /repo_stats/<date>/<hash>
    """
    repo_stats_dir = os.path.join(base_dir, commit_date, commit_hash)
    os.makedirs(repo_stats_dir, exist_ok=True)
    return repo_stats_dir

def analyze_with_runner(directory, commit_date, commit_hash, static_analyzer_path, repo_stats_base):
    """
    Call the external Python script static_analyzer.py with --dir argument.
    """
    # Create the /repo_stats/<date>/<hash> directory for the logs
    commit_stats_dir = create_repo_stats_directory(
        repo_stats_base, commit_date, commit_hash
    )

    try:
        # Run `static_analyzer.py` using the provided path and pass the cloned directory as the --dir argument
        # Set cwd to commit_stats_dir so logs are saved there
        subprocess.run(['python', static_analyzer_path, '--dir', directory], check=True, cwd=commit_stats_dir)

        # The logs should now be in commit_stats_dir
        log_filename = f"logs_{commit_hash}"
        log_filepath = os.path.join(commit_stats_dir, log_filename)

        if os.path.exists(log_filepath):
            print(f"Logs successfully found in: {commit_stats_dir}")
        else:
            print(f"Warning: Log file {log_filename} not found in {commit_stats_dir}")

    except subprocess.CalledProcessError as e:
        print(f"Error running static_analyzer script: {e}")

def restore_branch(branch_name, repo_path):
    """
    Restore the branch to its original state after analyzing commits.
    """
    subprocess.run(['git', 'checkout', branch_name], check=True, cwd=repo_path)

def get_all_branches(repo_path):
    """
    Get a list of all branch names in the repository.
    """
    result = subprocess.run(['git', 'branch', '-r'], capture_output=True, text=True, cwd=repo_path)
    if result.returncode != 0:
        raise Exception("Failed to get branch list")

    branches = [branch.strip().replace('origin/', '') for branch in result.stdout.splitlines()]
    return branches

def process_commits_on_branch(start_date, end_date, branch_name, repo_url=None, local_path=None, static_analyzer_path=None, repo_stats_base=None):
    """
    Process the commits on a specific branch.
    """
    print(f"Processing branch: {branch_name}")
    git_history, repo_path = fetch_git_history_between_dates(
        start_date, end_date, branch_name, repo_url=repo_url, local_path=local_path
    )

    for line in git_history:
        if '|' in line:
            commit_hash, author, date, message = line.split('|', 3)
            commit_date = date.split(' ')[0]  # Extract the date (YYYY-MM-DD)
            print(f"Processing commit {commit_hash} by {author} on {commit_date}")

            # Checkout the specific commit
            try:
                checkout_commit(commit_hash, repo_path)

                # Call analyze_with_runner with the static_analyzer_path and repo_stats_base
                analyze_with_runner(
                    repo_path,
                    commit_date,
                    commit_hash,
                    static_analyzer_path,
                    repo_stats_base
                )

            except Exception as e:
                print(f"Error processing commit {commit_hash}: {e}")

    # Restore the branch after processing
    if branch_name != 'all':
        restore_branch(branch_name, repo_path)

