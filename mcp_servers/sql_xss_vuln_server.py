import os
from fastmcp import FastMCP

mcp = FastMCP(name="security-repo-scanner")

@mcp.tool(
    name="scan_directory_for_vulnerabilities",
    description="Scans a directory for potential SQL injection and XSS vulnerabilities using language-agnostic heuristics."
)
def scan_directory_for_vulnerabilities(root_dir: str) -> dict:
    sql_findings = []
    xss_findings = []

    sql_keywords = ["SELECT", "INSERT", "UPDATE", "DELETE"]
    sql_concat_indicators = ["+", "format(", "%s", "%("]

    xss_sinks = [
        "innerHTML",
        "outerHTML",
        "document.write",
        "<script"
    ]

    for root, _, files in os.walk(root_dir):
        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                with open(file_path, "r", errors="ignore") as f:
                    lines = f.readlines()
            except Exception:
                continue  # unreadable / binary file

            # --- SQL Injection Scan ---
            for idx, line in enumerate(lines):
                upper = line.upper()
                if any(k in upper for k in sql_keywords) and any(c in line for c in sql_concat_indicators):
                    sql_findings.append({
                        "file": file_path,
                        "start_line": idx + 1,
                        "end_line": idx + 1
                    })

            # --- XSS Scan ---
            for idx, line in enumerate(lines):
                if any(sink in line for sink in xss_sinks):
                    xss_findings.append({
                        "file": file_path,
                        "start_line": idx + 1,
                        "end_line": idx + 1
                    })

    return {
        "sql_injections": sql_findings,
        "xss": xss_findings
    }

if __name__ == "__main__":
    mcp.run()
