from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import subprocess
import os

app = Flask(__name__)

SCRIPT_PATH = "git_history_analysis.py"  # hard-coded path
OUTPUT_DIR = "repo_analysis"

def build_tree(path):
    tree = {"name": os.path.basename(path), "path": path, "dirs": [], "files": []}
    try:
        for entry in os.scandir(path):
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
        repo_url = request.form.get("repo_url")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")

        # Run the external script with argparse arguments
        subprocess.run([
            "python3", SCRIPT_PATH,
            "--repo_url", repo_url,
            "--since", start_date,
            "--until", end_date
        ])

        return redirect(url_for("browse"))

    return render_template("./index.html")


@app.route("/view/<path:filename>")
def view_file(filename):
    full_path = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        return render_template("view.html", filename=filename, content=content)
    else:
        return f"File {filename} not found", 404
if __name__ == "__main__":
    app.run(host = '0.0.0.0',
            debug = True)
