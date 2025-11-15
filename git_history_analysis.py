import argparse
import json
import os
import shutil
import sys
import subprocess
from datetime import datetime
from repo_utils.git_code_utils import (
    fetch_git_history_between_dates,
    clone_repository,
    get_all_branches,
)

from repo_utils.git_utils import get_active_users, create_user_commit_jsons

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
                        required = True,
                        help = "The URL of the remote git repository")

    parser.add_argument('--write-user-info',
                        action='store_true',
                        help='Write per-user lines added/removed info to user_info.json')

    parser.add_argument('--user-info-output',
                        default='./repo_analysis/user_info.json',
                        help='Path to write the user info JSON file (default: ./repo_analysis/user_info.json)')

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
    # Base path for storing analysis outputs
    REPO_ANALYSIS_BASE = './repo_analysis'  # Ensure this directory exists or can be created and is writable

    # Optionally build per-user commit dicts (in-memory) and write per-user JSONs
    if args.write_user_info:
        branch_for_info = branch_name if branch_name != 'all' else 'main'
        print(f"Building per-user commit data for branch '{branch_for_info}' (in-memory) and writing to {os.path.join(REPO_ANALYSIS_BASE, 'users')}...")
        try:
            user_commit_dicts = create_user_commit_jsons(repo_url=repo_url, branch=branch_for_info, since=args.since, until=args.until)
            # write per-user files
            users_base = os.path.join(REPO_ANALYSIS_BASE, 'users')
            os.makedirs(users_base, exist_ok=True)
            for author, commits in user_commit_dicts.items():
                safe = ''.join(c if c.isalnum() or c in '._-' else '_' for c in author)
                user_dir = os.path.join(users_base, safe)
                os.makedirs(user_dir, exist_ok=True)
                out_path = os.path.join(user_dir, 'user_commits.json')
                try:
                    with open(out_path, 'w') as fh:
                        json.dump({'user': author, 'commits': commits}, fh, indent=2)
                except Exception as e:
                    print(f"Failed to write user commits for {author}: {e}")
        except Exception as e:
            print(f"Failed to create per-user commit JSONs: {e}")

    # Ensure STATIC_ANALYZER_PATH is correctly set
    ORIGINAL_WORKING_DIR = os.getcwd()
    STATIC_ANALYZER_DIR = ORIGINAL_WORKING_DIR
    STATIC_ANALYZER_PATH = os.path.join(STATIC_ANALYZER_DIR, 'static_analyzer.py')

    # Hard-code the repo_analysis path
    REPO_ANALYSIS_BASE = './repo_analysis'  # Ensure this directory exists or can be created and is writable

    # Informative print statements
    print(f"\n========== Git Commit Analysis ==========")
    print(f"START DATE      : {start_date}")
    print(f"END DATE        : {end_date}")
    print(f"BRANCH          : {branch_name}")
    print(f"REPO URL        : {repo_url}")
    print(f"REPO_ANALYSIS_BASE : {REPO_ANALYSIS_BASE}")
    print("==========================================\n")

    # Get list of branches
    if branch_name == 'all':
        # Clone the repository to get the list of branches
        temp_repo_path = "/tmp/git_repo_clone_temp"
        if os.path.exists(temp_repo_path):
            shutil.rmtree(temp_repo_path)
        clone_repository(repo_url, temp_repo_path)
        branches = get_all_branches(temp_repo_path)
        shutil.rmtree(temp_repo_path)
    else:
        branches = [branch_name]

    # Process each branch
    for branch in branches:
        print(f"\nProcessing branch: {branch}")
        
        # Clone the repository into a temporary directory for the branch
        branch_repo_path = f"./tmp/_{branch}"
        if os.path.exists(branch_repo_path):
            shutil.rmtree(branch_repo_path)
        clone_repository(repo_url, branch_repo_path)

        # Checkout the branch
        subprocess.run(['git', 'checkout', branch], check=True, cwd=branch_repo_path)

        git_history, _ = fetch_git_history_between_dates(
            start_date, end_date, branch, repo_url=None, local_path=branch_repo_path
        )

        # Process each commit in the branch
        for line in git_history:
            if '|' in line:
                commit_hash, author, date_str, message = line.strip().split('|', 3)
                # Parse the commit date
                commit_datetime = datetime.strptime(date_str.strip(), '%a %b %d %H:%M:%S %Y %z')
                commit_date = commit_datetime.strftime('%m-%d-%Y')
                print(f"\nProcessing commit {commit_hash} by {author} on {commit_date}")

                try:
                    # Checkout the specific commit in the branch repo
                    subprocess.run(['git', 'checkout', commit_hash], check=True, cwd=branch_repo_path)

                    # Verify the current commit
                    result = subprocess.run(
                        ['git', 'rev-parse', 'HEAD'],
                        capture_output=True,
                        text=True,
                        cwd=branch_repo_path
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

                    # Create the /repo_analysis/<branch>/<date>/<hash> directory for the logs
                    commit_analysis_dir = os.path.join(REPO_ANALYSIS_BASE, branch, commit_date, commit_hash)
                    os.makedirs(commit_analysis_dir, exist_ok=True)

                    # Prepare environment variables
                    env = os.environ.copy()
                    env['PYTHONPATH'] = STATIC_ANALYZER_DIR

                    # Run static_analyzer.py from its own directory
                    subprocess.run(
                        ['python', STATIC_ANALYZER_PATH, '--dir', branch_repo_path],
                        check=True,
                        cwd=STATIC_ANALYZER_DIR,
                        env=env
                    )

                    # Move logs from where static_analyzer.py outputs them to commit_analysis_dir
                    for item in os.listdir(STATIC_ANALYZER_DIR):
                        if item.startswith('logs_'):
                            item_path = os.path.join(STATIC_ANALYZER_DIR, item)
                            if os.path.isdir(item_path):
                                shutil.move(item_path, commit_analysis_dir)
                                print(f"Logs moved to: {commit_analysis_dir}")

                except Exception as e:
                    print(f"Error processing commit {commit_hash}: {e}")
        
        users = get_active_users(branch_repo_path, start_date, end_date, branch)
        formatted_users = [user.replace(' ','_').lower() for user in users]
        
        human_users = [user for user in formatted_users if "[bot]" not in user]
        bots = [user for user in formatted_users if "[bot]" in user]
        formatted_bots = [bot.split('[')[0].strip() for bot in bots]
        for user in human_users:
            if not os.path.exists(os.path.join(REPO_ANALYSIS_BASE, branch, 'users')):
                os.makedirs(os.path.join(REPO_ANALYSIS_BASE, branch, 'users'))
                os.makedirs(os.path.join(REPO_ANALYSIS_BASE, branch, 'users', user))
        
        for bot in formatted_bots:
            if not os.path.exists(os.path.join(REPO_ANALYSIS_BASE, branch, 'bots')):
                os.makedirs(os.path.join(REPO_ANALYSIS_BASE, branch, 'bots'))
                os.makedirs(os.path.join(REPO_ANALYSIS_BASE, branch, 'bots', bot))
           
        # Build per-user commit JSONs for this branch and write them into the branch-specific users directory
        try:
            per_user_commits = create_user_commit_jsons(local_path = branch_repo_path,
                                                        branch = branch, 
                                                        since = args.since, until=args.until)
            #import pdb ; pdb.set_trace()
            users_base_branch = os.path.join(REPO_ANALYSIS_BASE,
             branch,
             'users')
            os.makedirs(users_base_branch, exist_ok=True)
            for author, commits in per_user_commits.items():
                if '[bot]' in author:
                    formatted_author = author.split('[')[0].strip()
                    user_dir = os.path.join(REPO_ANALYSIS_BASE, branch, 'bots', formatted_author)
                    #import pdb ; pdb.set_trace()
                    os.makedirs(user_dir, exist_ok=True)
                else:
                    #import pdb ; pdb.set_trace()
                    formatted_author = author.replace(' ','_').lower()
                    safe = ''.join(c if c.isalnum() or c in '._-' else '_' for c in formatted_author)
                    user_dir = os.path.join(users_base_branch, safe)
                    #import pdb ; pdb.set_trace()
                    os.makedirs(user_dir, exist_ok=True)
                out_path = os.path.join(user_dir, 'user_commits.json')
                try:
                    with open(out_path, 'w') as fh:
                        json.dump({'user': formatted_author, 'commits': commits}, fh, indent=2)
                except Exception as e:
                    print(f"Failed to write per-branch user commits for {author}: {e}")
        except Exception as e:
            print(f"Failed to build per-user commits for branch {branch}: {e}")
        if os.path.exists(branch_repo_path):
            shutil.rmtree(branch_repo_path)
       
        
if __name__ == "__main__":
    main()

