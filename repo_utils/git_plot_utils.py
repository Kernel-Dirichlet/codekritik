import matplotlib.pyplot as plt

def plot_user_commits_histogram(commit_data, output_filename='user_commits_histogram.png'):
    """
    Plot and save a histogram of the number of commits per user.
    
    Args:
    - commit_data: A dictionary {user: {date: [commit messages]}}
    - output_filename: The name of the PNG file to save the plot
    """
    # Extract users and their total commit counts
    users = []
    commit_counts = []
    
    for user, date_commits in commit_data.items():
        total_commits = sum(len(messages) for messages in date_commits.values())
        users.append(user)
        commit_counts.append(total_commits)
    
    # Plot the histogram
    plt.figure(figsize=(10, 6))
    plt.bar(users, commit_counts, color='skyblue')
    
    plt.xlabel('Users')
    plt.ylabel('Number of Commits')
    plt.title('Number of Commits per User')
    plt.xticks(rotation=45, ha='right')  # Rotate user names for better visibility

    # Save the plot as a PNG file
    plt.tight_layout()
    plt.savefig(output_filename)

    print(f"Histogram saved as {output_filename}")
    plt.close()

# Example usage with data from fetch_git_history
#git_history = fetch_git_history(local_path='/path/to/local/repo')  # or use a public repo URL
#plot_user_commits_histogram(git_history['commit_data'], 'user_commits_histogram.png')
