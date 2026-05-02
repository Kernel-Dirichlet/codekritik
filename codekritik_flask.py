from flask import Flask, render_template, request, redirect, url_for
import subprocess
import sys
import os

app = Flask(__name__)

SCRIPT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "git_history_analysis.py")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "repo_analysis")


def build_tree(path):
    """Recursively build a directory tree dict for the browse view."""
    os.makedirs(path, exist_ok=True)
    tree = {"name": os.path.basename(path), "path": path, "dirs": [], "files": []}
    try:
        for entry in sorted(os.scandir(path), key=lambda e: (not e.is_dir(), e.name)):
            if entry.is_dir():
                tree["dirs"].append(build_tree(entry.path))
            else:
                tree["files"].append(entry.name)
    except PermissionError:
        pass
    return tree


@app.route("/browse")
def browse():
    tree = build_tree(OUTPUT_DIR)
    return render_template("browse.html", tree=tree)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        repo_url   = request.form.get("repo_url", "").strip()
        start_date = request.form.get("start_date", "").strip()
        end_date   = request.form.get("end_date", "").strip()

        if not repo_url or not start_date or not end_date:
            return render_template("index.html",
                                   error="All three fields (repo URL, start date, end date) are required.")

        # Run git_history_analysis.py using the same venv Python as Flask.
        # Capture combined stdout+stderr so we can surface errors to the user.
        result = subprocess.run(
            [
                sys.executable, SCRIPT_PATH,
                "--repo_url", repo_url,
                "--since",    start_date,
                "--until",    end_date,
            ],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__)),
        )

        combined_output = (result.stdout or "") + (result.stderr or "")

        if result.returncode != 0:
            # Surface the error to the user instead of silently showing an empty browse page.
            return render_template("index.html",
                                   error=_friendly_error(combined_output, repo_url),
                                   log_output=combined_output)

        return redirect(url_for("browse"))

    return render_template("index.html")


def _friendly_error(output: str, repo_url: str) -> str:
    """Return a human-readable error message based on the subprocess output."""
    low = output.lower()
    if "authentication failed" in low or "invalid username or token" in low or "could not read username" in low:
        return (
            f"Authentication failed for <code>{repo_url}</code>. "
            "This repository appears to be <strong>private</strong>. "
            "CodeKritik currently supports public repositories only. "
            "Please use a public GitHub/GitLab URL."
        )
    if "repository not found" in low or "not found" in low:
        return (
            f"Repository not found: <code>{repo_url}</code>. "
            "Please check the URL and try again."
        )
    if "could not resolve host" in low or "name or service not known" in low:
        return "Network error: could not reach the remote host. Check your internet connection."
    if "error parsing dates" in low or "strptime" in low:
        return "Invalid date format. Please use MM-DD-YYYY (e.g. 04-01-2026)."
    # Generic fallback
    return "Analysis failed. See the log output below for details."


@app.route("/view/<path:filename>")
def view_file(filename):
    full_path = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        return render_template("view.html", filename=filename, content=content)
    return f"File {filename} not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
