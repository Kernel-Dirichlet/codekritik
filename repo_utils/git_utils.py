import subprocess
import os
import shutil
from collections import defaultdict

def fetch_git_history(repo_url=None, local_path=None):
    """
    Fetch Git history from a local repository or a public repository.
    
    Args:
    - repo_url: URL of the public git repository (Optional)
    - local_path: Path to the local repository (Optional)
    
    Returns:
    - result_dict: Dictionary containing:
        - 'num_pushes': Total number of commits (pushes)
        - 'commit_data': {user: {date: [commit messages]}}
    """

    if repo_url:
        # Clone the public repository into a temporary directory
        temp_dir = 'temp_repo'
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        subprocess.run(['git', 'clone', repo_url, temp_dir], check=True)
        os.chdir(temp_dir)
    elif local_path:
        # Use the specified local repository path
        os.chdir(local_path)
    else:
        raise ValueError("Either 'repo_url' or 'local_path' must be provided.")

    # Get the entire git history using git log
    result = subprocess.run(['git', 'log', '--pretty=format:%H|%an|%ad|%s', '--date=short'], capture_output=True, text=True)
    
    if result.returncode != 0:
        raise Exception("Failed to fetch git history")
    
    git_logs = result.stdout.splitlines()
    
    num_pushes = len(git_logs)  # Each commit is considered a push here
    
    user_commit_data = defaultdict(lambda: defaultdict(list))  # {user: {date: [commit messages]}}

    for log in git_logs:
        commit_hash, author_name, date, message = log.split('|')
        user_commit_data[author_name][date].append(message)

    # If we cloned a public repo, clean up by removing the temporary directory
    if repo_url:
        os.chdir('..')
        shutil.rmtree(temp_dir)

    # Prepare the return dictionary
    result_dict = {
        'num_pushes': num_pushes,
        'commit_data': dict(user_commit_data)  # Convert defaultdict to dict for returning
    }

    return result_dict
