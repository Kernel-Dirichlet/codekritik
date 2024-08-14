import os
import json
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('../metrics')
from git_metrics_utils import (
    is_git_repo,
    calculate_code_churn_per_file,
    calculate_commit_frequency,
    calculate_contributor_activity,
    calculate_file_changes,
    analyze_commit_messages,
    get_all_files_in_repo
)

def main():
    parser = argparse.ArgumentParser(description="Calculate Git commit history metrics.")
    parser.add_argument("--dir", required=True, help="Path to the Git repository root directory.")
    parser.add_argument("--output", required=True, help="Path to the directory where metrics will be stored.")

    args = parser.parse_args()

    repo_dir = os.path.abspath(args.dir)
    output_dir = os.path.abspath(args.output)

    # Check if the directory is a valid Git repository
    if not is_git_repo(repo_dir):
        print(f"Error: The directory '{repo_dir}' is not a valid Git repository.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all files in the repository, including nested subdirectories
    all_files = get_all_files_in_repo(repo_dir)

    # Calculate global metrics
    commit_count, commit_frequency = calculate_commit_frequency(repo_dir)
    contributor_activity = calculate_contributor_activity(repo_dir)

    # Calculate file-specific metrics
    file_churn_metrics = calculate_code_churn_per_file(repo_dir)
    file_changes = calculate_file_changes(repo_dir)

    # Combine file-specific metrics
    file_metrics = {}
    for filepath in all_files:
        file_metrics[filepath] = {
            "code_churn": file_churn_metrics.get(filepath, {
                "lines_added": 0,
                "lines_deleted": 0,
                "total_churn": 0,
                "churn_ratio": 0,
                "churn_over_time": []
            }),
            "file_changes": file_changes.get(filepath, 0)
        }

    # Save global metrics and file metrics
    summary_metrics = {
        "commit_count": commit_count,
        "commit_frequency": commit_frequency.to_dict(),
        "contributor_activity": contributor_activity,
        "commit_message_analysis": analyze_commit_messages(repo_dir)
    }

    with open(os.path.join(output_dir, "summary_metrics.json"), "w") as f:
        json.dump(summary_metrics, f, indent=4)

    with open(os.path.join(output_dir, "files_metrics.json"), "w") as f:
        json.dump(file_metrics, f, indent=4)

    # Visualize metrics
    visualize_metrics(summary_metrics, output_dir)

def visualize_metrics(metrics, output_dir):
    # Code Churn over Time (Aggregated)
    churn_over_time = []
    for filepath, data in metrics.get('file_metrics', {}).items():
        churn_over_time.extend(data['code_churn']['churn_over_time'])
    
    if churn_over_time:
        churn_df = pd.DataFrame(churn_over_time, columns=["added", "deleted"])
        churn_df.plot(kind='line')
        plt.title('Code Churn Over Time (Aggregated)')
        plt.xlabel('Commit')
        plt.ylabel('Lines')
        plt.savefig(os.path.join(output_dir, 'code_churn_over_time.png'))
        plt.close()

    # Commit Frequency
    commit_frequency = pd.Series(metrics['commit_frequency'])
    commit_frequency.plot(kind='line')
    plt.title('Commit Frequency Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Commits')
    plt.savefig(os.path.join(output_dir, 'commit_frequency.png'))
    plt.close()
    # Contributor Activity
    contributor_activity = pd.Series(metrics['contributor_activity'])
    contributor_activity.plot(kind='barh')
    plt.title('Commits by Contributor')
    plt.xlabel('Number of Commits')
    plt.ylabel('Contributor')
    plt.savefig(os.path.join(output_dir, 'contributor_activity.png'))
    plt.close()
    # Commit Message Analysis
    commit_message_analysis = pd.Series(metrics['commit_message_analysis'])
    commit_message_analysis.plot(kind='barh')
    plt.title('Commit Message Keyword Frequency')
    plt.xlabel('Frequency')
    plt.ylabel('Keyword')
    plt.savefig(os.path.join(output_dir, 'commit_message_analysis.png'))
    plt.close()
    #plt.show()

if __name__ == "__main__":
    main()

