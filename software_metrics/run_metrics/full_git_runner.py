import os
import subprocess
import argparse
import shutil
import sys
sys.path.append('../metrics')
from loc_utils import * 
from abc_metric_utils import * 
from halstead_metric_utils import * 
from cyclomatic_complexity_utils import * 
from mi_utils import * 
from git_metrics_utils import * 
from utils_main import * 

def run_command(command, cwd=None):
    """Helper function to run a shell command and return the output."""
    result = subprocess.run(command, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr.decode())
        exit(1)
    return result.stdout.decode().strip()

def get_git_commits(repo_dir):
    """Get a list of all commit hashes in the repository, starting from the most recent."""
    command = "git rev-list --all"
    commits = run_command(command, cwd=repo_dir)
    return commits.splitlines()

def checkout_commit(repo_dir, commit):
    """Checkout a specific commit in the Git repository."""
    command = f"git checkout {commit}"
    run_command(command, cwd=repo_dir)

def run_runner_for_commit(repo_dir, output_dir, runner_script):
    """Run the runner.py script for the current commit."""
    command = f"python {runner_script} --dir {repo_dir}"
    run_command(command, cwd=repo_dir)

    # Move the logs directory to the output directory with the commit hash
    commit_hash = run_command("git rev-parse HEAD", cwd=repo_dir)
    commit_logs_dir = os.path.join(output_dir, f"logs_{commit_hash}")

    if os.path.exists(commit_logs_dir):
        shutil.rmtree(commit_logs_dir)

    logs_dir = os.path.join(repo_dir, f"logs_{commit_hash}")
    shutil.move(logs_dir, commit_logs_dir)

def main():
    parser = argparse.ArgumentParser(description="Run runner.py for each commit in a Git repository.")
    parser.add_argument("--repo", required=True, help="Path to the Git repository root directory.")
    parser.add_argument("--runner", required=True, help="Path to the runner.py script.")
    parser.add_argument("--output", required=True, help="Path to the directory where logs will be stored.")

    args = parser.parse_args()

    repo_dir = os.path.abspath(args.repo)
    runner_script = os.path.abspath(args.runner)
    output_dir = os.path.abspath(args.output)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get all commits
    commits = get_git_commits(repo_dir)

    # Iterate over each commit
    for commit in commits:
        print(f"Processing commit: {commit}")

        # Checkout the commit
        checkout_commit(repo_dir, commit)

        # Run the runner.py script and save the logs
        run_runner_for_commit(repo_dir, output_dir, runner_script)

    # Checkout back to the original branch
    run_command("git checkout -", cwd=repo_dir)
    print("Finished processing all commits.")

if __name__ == "__main__":
    main()

