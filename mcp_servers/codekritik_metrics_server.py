"""
CodeKritik MCP Server — exposes static analysis and git history metrics
as MCP tools so that AI assistants can query repository data directly.

Usage:
    python mcp_servers/codekritik_metrics_server.py

Requires: fastmcp  (pip install fastmcp)
"""

import os
import json
import subprocess
import shutil
import sys
from pathlib import Path
from typing import Optional

from fastmcp import FastMCP

# ── Resolve project root (one level up from this file) ──────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "software_metrics" / "metrics"))
sys.path.insert(0, str(PROJECT_ROOT / "repo_utils"))

mcp = FastMCP(name="codekritik-metrics")

# ── Helpers ──────────────────────────────────────────────────────────────────

def _load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def _extensions_map() -> dict:
    return _load_json(str(PROJECT_ROOT / "metrics_cfgs" / "program_file_exts_map.json"))

def _extensions_list() -> list:
    with open(str(PROJECT_ROOT / "metrics_cfgs" / "program_file_exts.txt")) as f:
        return [line.strip() for line in f if line.strip()]

def _token_paths() -> dict:
    return {
        "hll": str(PROJECT_ROOT / "metrics_cfgs" / "hll_tokens.json"),
        "asm": str(PROJECT_ROOT / "metrics_cfgs" / "asm_tokens.json"),
        "ir":  str(PROJECT_ROOT / "metrics_cfgs" / "ir_tokens.json"),
    }

def _runner_cfg() -> dict:
    cfg = {}
    cfg_path = PROJECT_ROOT / "metrics_runner_cfg.txt"
    with open(cfg_path) as f:
        for line in f:
            line = line.strip()
            if line and ":" in line:
                k, v = line.split(":", 1)
                cfg[k.strip()] = v.strip().lower() == "true"
    return cfg

# ── Tool: run_static_analysis ────────────────────────────────────────────────

@mcp.tool(
    name="run_static_analysis",
    description=(
        "Run CodeKritik static analysis on a local directory. "
        "Computes LOC, Halstead, Cyclomatic Complexity, ABC, and Maintainability Index. "
        "Returns a summary dict with per-language and global metrics."
    )
)
def run_static_analysis(directory: str, runner_cfg_path: Optional[str] = None) -> dict:
    """
    Parameters
    ----------
    directory : str
        Absolute or relative path to the directory to analyse.
    runner_cfg_path : str, optional
        Path to a metrics_runner_cfg.txt override. Defaults to the project default.
    """
    if not os.path.isdir(directory):
        return {"error": f"Directory not found: {directory}"}

    cfg_path = runner_cfg_path or str(PROJECT_ROOT / "metrics_runner_cfg.txt")
    cmd = [
        sys.executable,
        str(PROJECT_ROOT / "static_analyzer.py"),
        "--dir", directory,
        "--runner_cfg", cfg_path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))
    if result.returncode != 0:
        return {"error": result.stderr or result.stdout}

    # Collect the most recent logs_ directory
    logs_dirs = sorted(
        [d for d in os.listdir(PROJECT_ROOT) if d.startswith("logs_")],
        key=lambda d: os.path.getmtime(os.path.join(PROJECT_ROOT, d)),
        reverse=True,
    )
    if not logs_dirs:
        return {"error": "No logs directory found after analysis."}

    logs_path = PROJECT_ROOT / logs_dirs[0]
    summary = {}
    for metric_dir in logs_path.iterdir():
        if metric_dir.is_dir():
            for json_file in metric_dir.glob("*.json"):
                try:
                    summary[json_file.stem] = _load_json(str(json_file))
                except Exception as e:
                    summary[json_file.stem] = {"error": str(e)}

    return {"logs_dir": str(logs_path), "metrics": summary}


# ── Tool: get_loc_metrics ────────────────────────────────────────────────────

@mcp.tool(
    name="get_loc_metrics",
    description=(
        "Compute Lines-of-Code metrics (LOC, SLOC, CLOC, BLOC) for a directory. "
        "Returns per-file, per-language, and global counts."
    )
)
def get_loc_metrics(directory: str) -> dict:
    if not os.path.isdir(directory):
        return {"error": f"Directory not found: {directory}"}

    from loc_utils import count_lines_of_code, loc_full_analysis
    from utils_main import get_language_for_extension

    tokens = _token_paths()
    ext_map = _extensions_map()
    ext_list = _extensions_list()

    try:
        loc_dict = count_lines_of_code(
            directory=directory,
            extensions_to_count=ext_list,
            extensions_map=ext_map,
            hll_tokens=tokens["hll"],
            asm_tokens=tokens["asm"],
            ir_tokens=tokens["ir"],
        )
        full = loc_full_analysis(loc_dict, ext_map)
        return full
    except Exception as e:
        return {"error": str(e)}


# ── Tool: get_halstead_metrics ───────────────────────────────────────────────

@mcp.tool(
    name="get_halstead_metrics",
    description=(
        "Compute Halstead complexity metrics for a directory. "
        "Returns vocabulary size, program length, volume, difficulty, effort, and estimated bugs."
    )
)
def get_halstead_metrics(directory: str) -> dict:
    if not os.path.isdir(directory):
        return {"error": f"Directory not found: {directory}"}

    from halstead_metric_utils import halstead_process_directory, halstead_full_analysis

    tokens = _token_paths()
    ext_map = _extensions_map()
    ext_list = _extensions_list()

    try:
        raw = halstead_process_directory(
            directory=directory,
            extensions_to_count=ext_list,
            extensions_map=ext_map,
            hll_tokens=tokens["hll"],
            asm_tokens=tokens["asm"],
            ir_tokens=tokens["ir"],
        )
        full = halstead_full_analysis(raw, ext_map)
        return full
    except Exception as e:
        return {"error": str(e)}


# ── Tool: get_cyclomatic_complexity ──────────────────────────────────────────

@mcp.tool(
    name="get_cyclomatic_complexity",
    description=(
        "Compute McCabe Cyclomatic Complexity for every source file in a directory. "
        "Returns per-file complexity scores and a global/language summary."
    )
)
def get_cyclomatic_complexity(directory: str) -> dict:
    if not os.path.isdir(directory):
        return {"error": f"Directory not found: {directory}"}

    from cyclomatic_complexity_utils import cc_process_directory, cc_full_analysis

    tokens = _token_paths()
    ext_map = _extensions_map()
    ext_list = _extensions_list()

    try:
        raw = cc_process_directory(
            directory=directory,
            extensions_to_count=ext_list,
            extensions_map=ext_map,
            hll_tokens=tokens["hll"],
            asm_tokens=tokens["asm"],
            ir_tokens=tokens["ir"],
        )
        # Strip CFG ASCII to keep response compact
        compact = {f: {"cyclomatic_complexity": v["cyclomatic_complexity"]} for f, v in raw.items()}
        full = cc_full_analysis(compact, ext_map)
        return full
    except Exception as e:
        return {"error": str(e)}


# ── Tool: get_abc_metrics ────────────────────────────────────────────────────

@mcp.tool(
    name="get_abc_metrics",
    description=(
        "Compute ABC (Assignments, Branches, Conditionals) metrics for a directory. "
        "Returns per-file ABC scores and a global/language summary."
    )
)
def get_abc_metrics(directory: str) -> dict:
    if not os.path.isdir(directory):
        return {"error": f"Directory not found: {directory}"}

    from abc_metric_utils import abc_process_directory, abc_full_analysis

    tokens = _token_paths()
    ext_map = _extensions_map()
    ext_list = _extensions_list()

    try:
        raw = abc_process_directory(
            directory=directory,
            extensions_to_count=ext_list,
            extensions_map=ext_map,
            hll_tokens=tokens["hll"],
            asm_tokens=tokens["asm"],
            ir_tokens=tokens["ir"],
        )
        full = abc_full_analysis(raw, ext_map)
        return full
    except Exception as e:
        return {"error": str(e)}


# ── Tool: get_git_commit_stats ───────────────────────────────────────────────

@mcp.tool(
    name="get_git_commit_stats",
    description=(
        "Fetch and summarise git commit statistics for a repository between two dates. "
        "Returns per-author stats, commit frequency, churn rate, and commit type breakdown."
    )
)
def get_git_commit_stats(
    repo_url: str,
    since: str,
    until: str,
    branch: str = "main",
) -> dict:
    """
    Parameters
    ----------
    repo_url : str   GitHub/GitLab URL or local path.
    since    : str   Start date MM-DD-YYYY.
    until    : str   End date MM-DD-YYYY.
    branch   : str   Branch name (default: main).
    """
    from git_utils import create_user_commit_jsons, get_active_users

    try:
        user_commits = create_user_commit_jsons(
            repo_url=repo_url,
            branch=branch,
            since=since,
            until=until,
        )
        return {"user_commits": user_commits}
    except Exception as e:
        return {"error": str(e)}


# ── Tool: get_per_user_commit_summary ────────────────────────────────────────

@mcp.tool(
    name="get_per_user_commit_summary",
    description=(
        "Aggregate per-user commit metrics from a repo_analysis directory. "
        "Reads all user_commits.json files and returns a rolled-up summary per author."
    )
)
def get_per_user_commit_summary(repo_analysis_dir: str) -> dict:
    """
    Parameters
    ----------
    repo_analysis_dir : str
        Path to the repo_analysis output directory (e.g. './repo_analysis').
    """
    base = Path(repo_analysis_dir)
    if not base.is_dir():
        return {"error": f"Directory not found: {repo_analysis_dir}"}

    summary = {}
    for user_json in base.rglob("user_commits.json"):
        try:
            data = _load_json(str(user_json))
            # Derive author name from directory structure
            author = user_json.parent.name
            totals = {
                "commits": 0,
                "lines_added": 0,
                "lines_removed": 0,
                "code_churn": 0,
                "fixes": 0,
                "feats": 0,
                "docs": 0,
                "chores": 0,
                "refactors": 0,
                "tests": 0,
                "perf": 0,
                "ci": 0,
            }
            for commit_hash, date_metrics in data.items():
                for date_key, metrics in date_metrics.items():
                    totals["commits"] += 1
                    for k in totals:
                        if k != "commits" and k in metrics:
                            totals[k] += metrics[k]
            summary[author] = totals
        except Exception as e:
            summary[str(user_json)] = {"error": str(e)}

    return summary


# ── Tool: list_analysis_results ──────────────────────────────────────────────

@mcp.tool(
    name="list_analysis_results",
    description=(
        "List all available analysis result files in the repo_analysis directory. "
        "Returns a nested dict of branch → date → commit → metric files."
    )
)
def list_analysis_results(repo_analysis_dir: str = "./repo_analysis") -> dict:
    base = Path(repo_analysis_dir)
    if not base.is_dir():
        return {"error": f"Directory not found: {repo_analysis_dir}"}

    tree = {}
    for path in sorted(base.rglob("*.json")):
        rel = path.relative_to(base)
        parts = rel.parts
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node.setdefault("__files__", []).append(parts[-1])

    return tree


# ── Tool: read_metric_file ────────────────────────────────────────────────────

@mcp.tool(
    name="read_metric_file",
    description=(
        "Read and return the contents of a specific metric JSON file from repo_analysis."
    )
)
def read_metric_file(file_path: str) -> dict:
    if not os.path.isfile(file_path):
        return {"error": f"File not found: {file_path}"}
    try:
        return _load_json(file_path)
    except Exception as e:
        return {"error": str(e)}


# ── Tool: scan_for_vulnerabilities ───────────────────────────────────────────

@mcp.tool(
    name="scan_for_vulnerabilities",
    description=(
        "Scan a directory for potential SQL injection and XSS vulnerabilities "
        "using language-agnostic heuristics. Returns findings with file paths and line numbers."
    )
)
def scan_for_vulnerabilities(root_dir: str) -> dict:
    sql_findings = []
    xss_findings = []

    sql_keywords = ["SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "EXEC"]
    sql_concat_indicators = ["+", "format(", "%s", "%(", "f\"", "f'", ".format("]

    xss_sinks = [
        "innerHTML",
        "outerHTML",
        "document.write",
        "<script",
        "eval(",
        "setTimeout(",
        "setInterval(",
    ]

    for root, _, files in os.walk(root_dir):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, "r", errors="ignore") as f:
                    lines = f.readlines()
            except Exception:
                continue

            for idx, line in enumerate(lines):
                upper = line.upper()
                if any(k in upper for k in sql_keywords) and any(c in line for c in sql_concat_indicators):
                    sql_findings.append({"file": file_path, "line": idx + 1, "snippet": line.strip()})

            for idx, line in enumerate(lines):
                if any(sink in line for sink in xss_sinks):
                    xss_findings.append({"file": file_path, "line": idx + 1, "snippet": line.strip()})

    return {
        "sql_injection_findings": sql_findings,
        "xss_findings": xss_findings,
        "total_sql": len(sql_findings),
        "total_xss": len(xss_findings),
    }


# ── Tool: get_supported_languages ────────────────────────────────────────────

@mcp.tool(
    name="get_supported_languages",
    description="Return the list of programming languages and file extensions supported by CodeKritik."
)
def get_supported_languages() -> dict:
    return _extensions_map()


# ── Tool: get_runner_config ───────────────────────────────────────────────────

@mcp.tool(
    name="get_runner_config",
    description="Return the current metrics runner configuration (which metrics are enabled/disabled)."
)
def get_runner_config() -> dict:
    return _runner_cfg()


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
