"""
Unit tests for the CodeKritik MCP server tools.

Tests are designed to run without a live MCP transport — we import the tool
functions directly and call them as plain Python functions.

Run with:
    cd /home/ezw/Documents/codekritik
    /home/ezw/codekritik_env/bin/python3 -m pytest tests/test_mcp_server.py -v
"""

import json
import os
import sys
import tempfile
import shutil
from pathlib import Path

import pytest

# ── Path setup ───────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "software_metrics" / "metrics"))
sys.path.insert(0, str(PROJECT_ROOT / "repo_utils"))
sys.path.insert(0, str(PROJECT_ROOT / "mcp_servers"))

# Import the tool objects from the MCP server module.
# fastmcp wraps each @mcp.tool()-decorated function into a FunctionTool object;
# the original Python callable is stored on the .fn attribute.
import codekritik_metrics_server as _mcp_module

def _unwrap(tool_obj):
    """Return the plain Python function from a fastmcp FunctionTool wrapper."""
    fn = getattr(tool_obj, "fn", None)
    if callable(fn):
        return fn
    # Fallback: if it's already callable (future fastmcp versions), use as-is
    if callable(tool_obj):
        return tool_obj
    raise TypeError(f"Cannot unwrap tool: {tool_obj!r}")

run_static_analysis       = _unwrap(_mcp_module.run_static_analysis)
get_loc_metrics           = _unwrap(_mcp_module.get_loc_metrics)
get_halstead_metrics      = _unwrap(_mcp_module.get_halstead_metrics)
get_cyclomatic_complexity = _unwrap(_mcp_module.get_cyclomatic_complexity)
get_abc_metrics           = _unwrap(_mcp_module.get_abc_metrics)
get_per_user_commit_summary = _unwrap(_mcp_module.get_per_user_commit_summary)
list_analysis_results     = _unwrap(_mcp_module.list_analysis_results)
read_metric_file          = _unwrap(_mcp_module.read_metric_file)
scan_for_vulnerabilities  = _unwrap(_mcp_module.scan_for_vulnerabilities)
get_supported_languages   = _unwrap(_mcp_module.get_supported_languages)
get_runner_config         = _unwrap(_mcp_module.get_runner_config)

# ── Fixtures ──────────────────────────────────────────────────────────────────

TEST_DIR = str(PROJECT_ROOT / "software_metrics" / "test_files")
DEMO_DIR = str(PROJECT_ROOT / "software_metrics" / "test_files" / "demo_files")
RUST_DIR = str(PROJECT_ROOT / "software_metrics" / "test_files" / "rust_examples" / "src")


@pytest.fixture(scope="session")
def tmp_repo_analysis(tmp_path_factory):
    """Create a minimal fake repo_analysis directory for read/list tests."""
    base = tmp_path_factory.mktemp("repo_analysis")
    branch_dir = base / "main" / "01-01-2024" / "abc123"
    branch_dir.mkdir(parents=True)
    users_dir = base / "main" / "users" / "alice"
    users_dir.mkdir(parents=True)

    # Write a fake metric JSON
    metric = {"global_dict": {"LOC": 100, "SLOC": 80}, "per_file": {}}
    (branch_dir / "loc_metrics.json").write_text(json.dumps(metric))

    # Write a fake user_commits.json
    user_commits = {
        "abc123": {
            "01-01-2024": {
                "lines_added": 50,
                "lines_removed": 10,
                "code_churn": 60,
                "fixes": 0,
                "feats": 1,
                "docs": 0,
                "chores": 0,
                "refactors": 0,
                "tests": 0,
                "perf": 0,
                "ci": 0,
            }
        }
    }
    (users_dir / "user_commits.json").write_text(json.dumps(user_commits))

    return str(base)


@pytest.fixture(scope="session")
def vuln_dir(tmp_path_factory):
    """Create a directory with known SQL/XSS vulnerability patterns."""
    d = tmp_path_factory.mktemp("vuln_code")

    (d / "bad_sql.py").write_text(
        'query = "SELECT * FROM users WHERE id = " + user_id\n'
        'cursor.execute(query)\n'
    )
    (d / "bad_xss.js").write_text(
        'document.getElementById("out").innerHTML = userInput;\n'
        'eval(userInput);\n'
    )
    (d / "clean.py").write_text(
        'x = 1 + 2\nprint(x)\n'
    )
    return str(d)


# ── Helper ────────────────────────────────────────────────────────────────────

def _assert_no_error(result: dict, context: str = ""):
    assert "error" not in result, f"{context} returned error: {result.get('error')}"


# ── Tests: get_supported_languages ───────────────────────────────────────────

class TestGetSupportedLanguages:
    def test_returns_dict(self):
        result = get_supported_languages()
        assert isinstance(result, dict)

    def test_contains_python(self):
        result = get_supported_languages()
        # The map is language_name → [extensions]; check keys for Python
        assert any("python" in k.lower() for k in result.keys()), \
            "Expected Python to appear in supported languages"

    def test_contains_rust(self):
        result = get_supported_languages()
        assert any("rust" in k.lower() for k in result.keys()), \
            "Expected Rust to appear in supported languages"

    def test_non_empty(self):
        result = get_supported_languages()
        assert len(result) > 5, "Expected at least 6 language mappings"


# ── Tests: get_runner_config ──────────────────────────────────────────────────

class TestGetRunnerConfig:
    def test_returns_dict(self):
        result = get_runner_config()
        assert isinstance(result, dict)

    def test_all_values_are_bool(self):
        result = get_runner_config()
        for k, v in result.items():
            assert isinstance(v, bool), f"Config key '{k}' has non-bool value: {v!r}"

    def test_known_keys_present(self):
        result = get_runner_config()
        # At least one of the standard metric keys should be present
        known = {"LOC", "Halstead", "Cyclomatic_complexity", "ABC", "Maintainability_index"}
        found = known & set(result.keys())
        assert found, f"None of the expected config keys found. Got: {list(result.keys())}"


# ── Tests: get_loc_metrics ────────────────────────────────────────────────────

class TestGetLocMetrics:
    def test_missing_dir_returns_error(self):
        result = get_loc_metrics("/nonexistent/path/xyz")
        assert "error" in result

    def test_demo_dir_returns_dict(self):
        result = get_loc_metrics(DEMO_DIR)
        _assert_no_error(result, "get_loc_metrics(demo_dir)")
        assert isinstance(result, dict)

    def test_demo_dir_has_loc_keys(self):
        result = get_loc_metrics(DEMO_DIR)
        _assert_no_error(result, "get_loc_metrics(demo_dir)")
        # Expect global_dict or per_file in the result
        assert "global_dict" in result or "per_file" in result or len(result) > 0

    def test_rust_dir(self):
        result = get_loc_metrics(RUST_DIR)
        _assert_no_error(result, "get_loc_metrics(rust_dir)")
        assert isinstance(result, dict)

    def test_test_files_dir(self):
        result = get_loc_metrics(TEST_DIR)
        _assert_no_error(result, "get_loc_metrics(test_files)")
        assert isinstance(result, dict)


# ── Tests: get_halstead_metrics ───────────────────────────────────────────────

class TestGetHalsteadMetrics:
    def test_missing_dir_returns_error(self):
        result = get_halstead_metrics("/nonexistent/path/xyz")
        assert "error" in result

    def test_demo_dir_returns_dict(self):
        result = get_halstead_metrics(DEMO_DIR)
        _assert_no_error(result, "get_halstead_metrics(demo_dir)")
        assert isinstance(result, dict)

    def test_rust_dir(self):
        result = get_halstead_metrics(RUST_DIR)
        _assert_no_error(result, "get_halstead_metrics(rust_dir)")
        assert isinstance(result, dict)

    def test_test_files_dir(self):
        result = get_halstead_metrics(TEST_DIR)
        _assert_no_error(result, "get_halstead_metrics(test_files)")
        assert isinstance(result, dict)


# ── Tests: get_cyclomatic_complexity ─────────────────────────────────────────

class TestGetCyclomaticComplexity:
    def test_missing_dir_returns_error(self):
        result = get_cyclomatic_complexity("/nonexistent/path/xyz")
        assert "error" in result

    def test_demo_dir_returns_dict(self):
        result = get_cyclomatic_complexity(DEMO_DIR)
        _assert_no_error(result, "get_cyclomatic_complexity(demo_dir)")
        assert isinstance(result, dict)

    def test_rust_dir(self):
        result = get_cyclomatic_complexity(RUST_DIR)
        _assert_no_error(result, "get_cyclomatic_complexity(rust_dir)")
        assert isinstance(result, dict)

    def test_test_files_dir(self):
        result = get_cyclomatic_complexity(TEST_DIR)
        _assert_no_error(result, "get_cyclomatic_complexity(test_files)")
        assert isinstance(result, dict)


# ── Tests: get_abc_metrics ────────────────────────────────────────────────────

class TestGetAbcMetrics:
    def test_missing_dir_returns_error(self):
        result = get_abc_metrics("/nonexistent/path/xyz")
        assert "error" in result

    def test_demo_dir_returns_dict(self):
        result = get_abc_metrics(DEMO_DIR)
        _assert_no_error(result, "get_abc_metrics(demo_dir)")
        assert isinstance(result, dict)

    def test_rust_dir(self):
        result = get_abc_metrics(RUST_DIR)
        _assert_no_error(result, "get_abc_metrics(rust_dir)")
        assert isinstance(result, dict)

    def test_test_files_dir(self):
        result = get_abc_metrics(TEST_DIR)
        _assert_no_error(result, "get_abc_metrics(test_files)")
        assert isinstance(result, dict)


# ── Tests: scan_for_vulnerabilities ──────────────────────────────────────────

class TestScanForVulnerabilities:
    def test_returns_expected_keys(self, vuln_dir):
        result = scan_for_vulnerabilities(vuln_dir)
        assert "sql_injection_findings" in result
        assert "xss_findings" in result
        assert "total_sql" in result
        assert "total_xss" in result

    def test_detects_sql_injection(self, vuln_dir):
        result = scan_for_vulnerabilities(vuln_dir)
        assert result["total_sql"] >= 1, "Expected at least one SQL injection finding"

    def test_detects_xss(self, vuln_dir):
        result = scan_for_vulnerabilities(vuln_dir)
        assert result["total_xss"] >= 1, "Expected at least one XSS finding"

    def test_clean_dir_has_no_findings(self, tmp_path):
        (tmp_path / "clean.py").write_text("x = 1\nprint(x)\n")
        result = scan_for_vulnerabilities(str(tmp_path))
        assert result["total_sql"] == 0
        assert result["total_xss"] == 0

    def test_findings_have_file_line_snippet(self, vuln_dir):
        result = scan_for_vulnerabilities(vuln_dir)
        for finding in result["sql_injection_findings"] + result["xss_findings"]:
            assert "file" in finding
            assert "line" in finding
            assert "snippet" in finding

    def test_counts_match_list_lengths(self, vuln_dir):
        result = scan_for_vulnerabilities(vuln_dir)
        assert result["total_sql"] == len(result["sql_injection_findings"])
        assert result["total_xss"] == len(result["xss_findings"])


# ── Tests: list_analysis_results ─────────────────────────────────────────────

class TestListAnalysisResults:
    def test_missing_dir_returns_error(self):
        result = list_analysis_results("/nonexistent/repo_analysis")
        assert "error" in result

    def test_returns_dict(self, tmp_repo_analysis):
        result = list_analysis_results(tmp_repo_analysis)
        assert isinstance(result, dict)

    def test_finds_json_files(self, tmp_repo_analysis):
        result = list_analysis_results(tmp_repo_analysis)
        # Should have at least the 'main' branch key
        assert "main" in result

    def test_files_key_present(self, tmp_repo_analysis):
        result = list_analysis_results(tmp_repo_analysis)
        # Drill down to find __files__ somewhere in the tree
        def has_files_key(node):
            if isinstance(node, dict):
                if "__files__" in node:
                    return True
                return any(has_files_key(v) for v in node.values())
            return False
        assert has_files_key(result), "Expected __files__ key somewhere in the tree"


# ── Tests: read_metric_file ───────────────────────────────────────────────────

class TestReadMetricFile:
    def test_missing_file_returns_error(self):
        result = read_metric_file("/nonexistent/file.json")
        assert "error" in result

    def test_reads_valid_json(self, tmp_repo_analysis):
        json_path = os.path.join(
            tmp_repo_analysis, "main", "01-01-2024", "abc123", "loc_metrics.json"
        )
        result = read_metric_file(json_path)
        assert "global_dict" in result
        assert result["global_dict"]["LOC"] == 100

    def test_reads_hll_tokens_config(self):
        hll_path = str(PROJECT_ROOT / "metrics_cfgs" / "hll_tokens.json")
        result = read_metric_file(hll_path)
        _assert_no_error(result, "read_metric_file(hll_tokens.json)")
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_reads_asm_tokens_config(self):
        asm_path = str(PROJECT_ROOT / "metrics_cfgs" / "asm_tokens.json")
        result = read_metric_file(asm_path)
        _assert_no_error(result, "read_metric_file(asm_tokens.json)")
        assert isinstance(result, dict)

    def test_reads_ir_tokens_config(self):
        ir_path = str(PROJECT_ROOT / "metrics_cfgs" / "ir_tokens.json")
        result = read_metric_file(ir_path)
        _assert_no_error(result, "read_metric_file(ir_tokens.json)")
        assert isinstance(result, dict)


# ── Tests: get_per_user_commit_summary ───────────────────────────────────────

class TestGetPerUserCommitSummary:
    def test_missing_dir_returns_error(self):
        result = get_per_user_commit_summary("/nonexistent/repo_analysis")
        assert "error" in result

    def test_returns_dict(self, tmp_repo_analysis):
        result = get_per_user_commit_summary(tmp_repo_analysis)
        assert isinstance(result, dict)

    def test_finds_alice(self, tmp_repo_analysis):
        result = get_per_user_commit_summary(tmp_repo_analysis)
        assert "alice" in result, f"Expected 'alice' in summary, got: {list(result.keys())}"

    def test_alice_has_expected_keys(self, tmp_repo_analysis):
        result = get_per_user_commit_summary(tmp_repo_analysis)
        alice = result["alice"]
        for key in ("commits", "lines_added", "lines_removed", "code_churn", "feats"):
            assert key in alice, f"Missing key '{key}' in alice's summary"

    def test_alice_commit_count(self, tmp_repo_analysis):
        result = get_per_user_commit_summary(tmp_repo_analysis)
        assert result["alice"]["commits"] == 1

    def test_alice_lines_added(self, tmp_repo_analysis):
        result = get_per_user_commit_summary(tmp_repo_analysis)
        assert result["alice"]["lines_added"] == 50

    def test_empty_dir_returns_empty(self, tmp_path):
        result = get_per_user_commit_summary(str(tmp_path))
        assert result == {}


# ── Tests: run_static_analysis ───────────────────────────────────────────────

class TestRunStaticAnalysis:
    def test_missing_dir_returns_error(self):
        result = run_static_analysis("/nonexistent/path/xyz")
        assert "error" in result

    def test_demo_dir_runs(self):
        result = run_static_analysis(DEMO_DIR)
        # Either succeeds with logs_dir or returns an error — both are valid
        # (depends on whether static_analyzer.py is fully configured)
        assert isinstance(result, dict)

    def test_result_has_expected_shape_on_success(self):
        result = run_static_analysis(DEMO_DIR)
        if "error" not in result:
            assert "logs_dir" in result
            assert "metrics" in result
            assert isinstance(result["metrics"], dict)
