import argparse
import os
import shutil
import sys
import subprocess
from datetime import datetime
from repo_utils.git_code_utils import (
    fetch_git_history_between_dates,
    clone_repository,
    get_all_branches
)

def main():
    # Argparse setup
    parser = argparse.ArgumentParser(description="Analyze commits in a git repository within a specified date range.")
    parser.add_argument('--since',
                        required = True,
                        help = "Start date in the format MM-DD-YYYY")

    parser.add_argument('--until',
                        required = True,
                        help = "End date in the format MM-DD-YYYY")

    parser.add_argument('--branch',
                        default = 'main',
                        help = "Branch name. Use 'all' to loop over all branches (default is 'main')")

    parser.add_argument('--repo_url',
                        help = "The URL of the remote git repository")

    parser.add_argument('--local_path',
                        help = "The local path to the git repository (if using a local repository)")

    args = parser.parse_args()

    # Parse and validate dates
    try:
        since_date = datetime.strptime(args.since, '%m-%d-%Y')
        until_date = datetime.strptime(args.until, '%m-%d-%Y')
    except ValueError as e:
        print(f"Error parsing dates: {e}")
        sys.exit(1)

    # Ensure 'since' date is before 'until' date
    if since_date > until_date:
        print("Error: 'since' date must be earlier than 'until' date.")
        sys.exit(1)

    start_date = since_date.strftime('%m-%d-%Y')
    end_date = until_date.strftime('%m-%d-%Y')

    branch_name = args.branch
    repo_url = args.repo_url
    local_path = args.local_path

    # Ensure STATIC_ANALYZER_PATH is correctly set
    ORIGINAL_WORKING_DIR = os.getcwd()
    STATIC_ANALYZER_DIR = ORIGINAL_WORKING_DIR
    STATIC_ANALYZER_PATH = os.path.join(STATIC_ANALYZER_DIR, 'static_analyzer.py')

    # Hard-code the repo_stats_base path
    REPO_STATS_BASE = './repo_stats'  #i Ensure this directory exists or can be created and is writable

    # Informative print statements
    print(f"\n========== Git Commit Analysis ==========")
    print(f"START DATE      : {start_date}")
    print(f"END DATE        : {end_date}")
    print(f"BRANCH          : {branch_name}")
    print(f"REPO URL        : {repo_url if repo_url else 'Using local repository'}")
    print(f"LOCAL PATH      : {local_path if local_path else 'None'}")
    print(f"REPO_STATS_BASE : {REPO_STATS_BASE}")
    print("==========================================\n")

    # Get list of branches
    if branch_name == 'all':
        if repo_url:
            # Clone the repository to get the list of branches
            temp_repo_path = "/tmp/git_repo_clone_temp"
            if os.path.exists(temp_repo_path):
                shutil.rmtree(temp_repo_path)
            clone_repository(repo_url, temp_repo_path)
            branches = get_all_branches(temp_repo_path)
            shutil.rmtree(temp_repo_path)
        elif local_path:
            branches = get_all_branches(local_path)
        else:
            raise ValueError("Either repo_url or local_path must be provided.")
    else:
        branches = [branch_name]

    # Process each branch
    for branch in branches:
        print(f"\nProcessing branch: {branch}")

        # Fetch git history for the branch
        if repo_url:
            # Clone the repository into a temporary directory for the branch
            branch_repo_path = f"./tmp/git_repo_branch_{branch}"
            if os.path.exists(branch_repo_path):
                shutil.rmtree(branch_repo_path)
            clone_repository(repo_url, branch_repo_path)

            # Checkout the branch
            subprocess.run(['git', 'checkout', branch], check=True, cwd=branch_repo_path)

            git_history, _ = fetch_git_history_between_dates(
                start_date, end_date, branch, repo_url=None, local_path=branch_repo_path
            )
        elif local_path:
            # Use the local repository path
            branch_repo_path = local_path
            # Checkout the branch
            subprocess.run(['git', 'checkout', branch], check=True, cwd=branch_repo_path)
            git_history, _ = fetch_git_history_between_dates(
                start_date, end_date, branch, repo_url=None, local_path=branch_repo_path
            )
        else:
            raise ValueError("Either repo_url or local_path must be provided.")

        # Process each commit in the branch
        for line in git_history:
            if '|' in line:
                commit_hash, author, date_str, message = line.strip().split('|', 3)
                # Parse the commit date
                commit_datetime = datetime.strptime(date_str.strip(), '%a %b %d %H:%M:%S %Y %z')
                commit_date = commit_datetime.strftime('%m-%d-%Y')
                print(f"\nProcessing commit {commit_hash} by {author} on {commit_date}")

                try:
                    # Clone the repository for this commit
                    commit_repo_path = f"/tmp/git_repo_commit_{commit_hash}"
                    if os.path.exists(commit_repo_path):
                        shutil.rmtree(commit_repo_path)
                    clone_repository(repo_url, commit_repo_path)

                    # Checkout the specific commit
                    subprocess.run(['git', 'checkout', commit_hash], check=True, cwd=commit_repo_path)

                    # Verify the current commit
                    result = subprocess.run(
                        ['git', 'rev-parse', 'HEAD'],
                        capture_output=True,
                        text=True,
                        cwd=commit_repo_path
                    )
                    current_commit = result.stdout.strip()
                    if current_commit != commit_hash:
                        print(f"Error: Expected commit {commit_hash}, but got {current_commit}")
                        continue  # Skip to the next commit
                    else:
                        print(f"Verified commit: {current_commit}")

                    # Clean up any previous logs
                    for item in os.listdir(STATIC_ANALYZER_DIR):
                        if item.startswith('logs_'):
                            item_path = os.path.join(STATIC_ANALYZER_DIR, item)
                            if os.path.isdir(item_path):
                                shutil.rmtree(item_path)

                    # Create the /repo_stats/<branch>/<date>/<hash> directory for the logs
                    commit_stats_dir = os.path.join(REPO_STATS_BASE, branch, commit_date, commit_hash)
                    os.makedirs(commit_stats_dir, exist_ok=True)

                    # Prepare environment variables
                    env = os.environ.copy()
                    env['PYTHONPATH'] = STATIC_ANALYZER_DIR

                    # Run static_analyzer.py from its own directory
                    subprocess.run(
                        ['python', STATIC_ANALYZER_PATH, '--dir', commit_repo_path],
                        check=True,
                        cwd=STATIC_ANALYZER_DIR,
                        env=env
                    )

                    # Move logs from where static_analyzer.py outputs them to commit_stats_dir
                    for item in os.listdir(STATIC_ANALYZER_DIR):
                        if item.startswith('logs_'):
                            item_path = os.path.join(STATIC_ANALYZER_DIR, item)
                            if os.path.isdir(item_path):
                                shutil.move(item_path, commit_stats_dir)
                                print(f"Logs moved to: {commit_stats_dir}")

                    # Clean up the cloned repository for this commit
                    shutil.rmtree(commit_repo_path)

                except Exception as e:
                    print(f"Error processing commit {commit_hash}: {e}")

        # Clean up the cloned repository for the branch
        if repo_url and os.path.exists(branch_repo_path):
            shutil.rmtree(branch_repo_path)

    print("\nAnalysis complete.")

if __name__ == "__main__":
    main()

