# CodeKritik

## Version 0.3.0

CodeKritik is an open-source, language-agnostic static analysis and git history metrics platform. It aims to exceed the functionality of tools like [SonarQube](https://www.sonarsource.com/products/sonarqube/) while being trivially easy to integrate into LLM/AI agent workflows via its built-in MCP server.

The analysis pipeline has three stages, each building on the previous:

1. **Static Analysis** — Computes LOC, Halstead complexity, Cyclomatic complexity, ABC score, and Maintainability Index for any source file across 20+ languages, including Assembly and IR.
2. **Git History Analysis** — Runs static analysis across every commit in a date range, tracking per-user and global metrics over time.
3. **MCP Integration** — Exposes all analysis capabilities as MCP tools so any LLM agent (Ollama, Claude, GPT-4, etc.) can query repository data autonomously.

---

## Language Support

| Level      | Languages |
|------------|-----------|
| High-level | Python, Julia, Go, Java, JavaScript, TypeScript, C, C++, C#, Objective-C, Haskell, Rust, BASH, COBOL, FORTRAN, R, PHP, Clojure, Lisp, Scala |
| IR         | LLVM, GIMPLE |
| Low-level  | x86, ARM, MIPS, PowerPC, RISC-V, SPARC, Z80 |

---

## Installation

```bash
git clone https://github.com/Kernel-Dirichlet/codekritik.git
cd codekritik
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

### 1. Static analysis on a local directory

```bash
python3 static_analyzer.py --dir /path/to/your/project
```

Output is written to `logs_<hash>/` with subdirectories for each metric at three levels of granularity: **file**, **language**, and **global**.

### 2. Git history analysis

Analyse every commit in a date range on a public GitHub/GitLab repository:

```bash
python3 git_history_analysis.py \
    --repo_url https://github.com/pallets/click.git \
    --since 04-01-2026 \
    --until 05-02-2026 \
    --branch main
```

Results are written to:
```
repo_analysis/<repo_name>/<branch>/<date>/<commit_hash>/logs_<hash>/
```

Per-user commit stats are written to:
```
repo_analysis/<repo_name>/<branch>/users/<author>/user_commits.json
```

> **Note:** Only public repositories are supported. Private repositories require a personal access token embedded in the URL (`https://<token>@github.com/owner/repo.git`).

### 3. Web UI

Start the Flask front-end to submit analyses and browse results in a browser:

```bash
python3 codekritik_flask.py
# Open http://localhost:5000
```

The UI accepts a GitHub URL and date range, shows a loading spinner while the analysis runs, and displays a detailed error banner (with collapsible log output) if anything goes wrong.

---

## MCP Server

CodeKritik ships a [FastMCP](https://gofastmcp.com) server that exposes all analysis capabilities as callable tools for LLM agents.

### Available tools

| Tool | Description |
|------|-------------|
| `run_static_analysis` | Run full static analysis on a local directory |
| `get_loc_metrics` | Lines-of-code breakdown (LOC / SLOC / CLOC / BLOC) |
| `get_halstead_metrics` | Halstead volume, difficulty, effort, estimated bugs |
| `get_cyclomatic_complexity` | McCabe complexity per file + global summary |
| `get_abc_metrics` | Assignments / Branches / Conditionals per file |
| `get_git_commit_stats` | Per-author commit stats for a repo + date range |
| `get_per_user_commit_summary` | Roll-up of user_commits.json files in repo_analysis |
| `list_analysis_results` | Tree of all JSON result files in repo_analysis |
| `read_metric_file` | Read a specific metric JSON file |
| `scan_for_vulnerabilities` | Heuristic SQL injection + XSS scanner |
| `get_supported_languages` | List all supported languages and file extensions |
| `get_runner_config` | Show which metrics are enabled/disabled |

### Starting the MCP server

**HTTP transport** (recommended — works with any MCP client over the network):

```bash
# In the codekritik directory
python mcp_servers/codekritik_metrics_server.py
```

By default FastMCP uses **stdio** transport. To expose it over HTTP on port 8000, edit the bottom of `codekritik_metrics_server.py`:

```python
if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)
```

Then start it:

```bash
python mcp_servers/codekritik_metrics_server.py
# Server listening on http://127.0.0.1:8000
```

---

## Using the MCP Server with Ollama (full example)

This section shows how to connect a local Ollama model to the CodeKritik MCP server so the model can autonomously call analysis tools.

### Prerequisites

```bash
# 1. Install and start Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama serve &

# 2. Pull a tool-capable model (any of these work)
ollama pull qwen2.5:7b        # recommended — excellent tool calling
# ollama pull llama3.1:8b
# ollama pull mistral-nemo

# 3. Install Python dependencies
pip install ollama mcp fastmcp
```

### Step 1 — Start the MCP server over HTTP

```bash
cd /path/to/codekritik

# Edit the last line of mcp_servers/codekritik_metrics_server.py to use HTTP:
#   mcp.run(transport="http", host="127.0.0.1", port=8000)

python mcp_servers/codekritik_metrics_server.py
# [codekritik-mcp] Listening on http://127.0.0.1:8000
```

### Step 2 — Run the bundled Ollama client

A ready-to-use client is provided at `mcp_servers/ollama_mcp_client.py`:

```bash
python mcp_servers/ollama_mcp_client.py \
    --model qwen2.5:7b \
    --server http://127.0.0.1:8000 \
    --prompt "What is the cyclomatic complexity of /path/to/my/project? Summarise the top 5 most complex files."
```

**Example session output:**

```
[codekritik-mcp] Connected to http://127.0.0.1:8000
[codekritik-mcp] 12 tools available: ['run_static_analysis', 'get_loc_metrics', ...]

[tool call] get_cyclomatic_complexity({
  "directory": "/path/to/my/project"
})
[tool result] {"global": {"mean_cc": 4.2, "max_cc": 18}, "per_file": {...}}...

── Model response ──────────────────────────────
Here are the 5 most complex files in your project:

1. src/parser.py        — CC 18  (high risk, consider refactoring)
2. src/codegen.py       — CC 14
3. tests/test_parser.py — CC 11
4. src/optimizer.py     — CC 9
5. src/lexer.py         — CC 7

The global mean cyclomatic complexity is 4.2, which is within acceptable
bounds, but `parser.py` and `codegen.py` are candidates for decomposition.
```

### Step 3 — Write your own client (minimal example)

```python
import asyncio, json, ollama
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    async with streamablehttp_client("http://127.0.0.1:8000") as (r, w, _):
        async with ClientSession(r, w) as session:
            await session.initialize()

            # Discover tools and convert to Ollama schema
            tools = await session.list_tools()
            ollama_tools = [
                {
                    "type": "function",
                    "function": {
                        "name": t.name,
                        "description": t.description,
                        "parameters": t.inputSchema or {},
                    },
                }
                for t in tools.tools
            ]

            messages = [{"role": "user", "content": "How many lines of code are in /tmp/myproject?"}]
            client = ollama.AsyncClient()

            while True:
                resp = await client.chat(model="qwen2.5:7b", messages=messages, tools=ollama_tools)
                msg = resp.message

                if not msg.tool_calls:
                    print(msg.content)   # final answer
                    break

                messages.append({"role": "assistant", "content": msg.content or "", "tool_calls": msg.tool_calls})

                for call in msg.tool_calls:
                    result = await session.call_tool(call.function.name, call.function.arguments or {})
                    messages.append({"role": "tool", "content": json.dumps(result.content[0].text)})

asyncio.run(main())
```

### Models known to support tool calling with Ollama

| Model | Pull command | Notes |
|-------|-------------|-------|
| `qwen2.5:7b` | `ollama pull qwen2.5:7b` | Best overall tool-calling accuracy |
| `llama3.1:8b` | `ollama pull llama3.1:8b` | Good general purpose |
| `mistral-nemo` | `ollama pull mistral-nemo` | Fast, good for structured output |
| `qwen2.5-coder:7b` | `ollama pull qwen2.5-coder:7b` | Best for code-specific prompts |

> Models must support the `tools` parameter in `ollama chat`. Run `ollama show <model>` and look for `tools` in the capabilities list to verify.

---

## Configuration

### `metrics_runner_cfg.txt`

Controls which metrics are computed:

```
loc: true
halstead: true
cyclomatic_complexity: true
abc: true
maintainability_index: true
```

### `metrics_cfgs/program_file_exts.txt`

List of file extensions the runner considers. Edit to ignore specific types.

### `metrics_cfgs/program_file_exts_map.json`

Maps language name → list of allowed extensions. Add new languages here.

### `metrics_cfgs/hll_tokens.json` / `asm_tokens.json` / `ir_tokens.json`

Token definitions (operators, keywords, comment markers) used for metric computation. Regenerate with:

```bash
python metrics_cfgs/generate_hll_tokens.py   # high-level languages
python metrics_cfgs/generate_lll_tokens.py   # assembly
python metrics_cfgs/generate_ir_tokens.py    # LLVM / GIMPLE
```

---

## Output Structure

```
repo_analysis/
└── <repo_name>/
    └── <branch>/
        ├── <MM-DD-YYYY>/
        │   └── <commit_hash>/
        │       └── logs_<hash>/
        │           ├── loc/
        │           │   ├── loc_per_file.json
        │           │   ├── loc_per_language.json
        │           │   └── loc_global.json
        │           ├── halstead/
        │           ├── cyclomatic_complexity/
        │           ├── abc/
        │           └── maintainability_index.json
        └── users/
            └── <author>/
                └── user_commits.json
```

---

## Current Metrics

| Metric | Description |
|--------|-------------|
| **LOC** | Source, comment, and blank lines per file/language/global |
| **Halstead** | Vocabulary, length, volume, difficulty, effort, estimated bugs |
| **Cyclomatic Complexity** | McCabe CC + ASCII control-flow graph |
| **ABC Score** | Assignments, Branches, Conditionals |
| **Maintainability Index** | MI score (0–100) combining LOC, Halstead, and CC |

---

## Use Cases

1. **Reward function for RL agents** — Use MI and CC as reward signals for code-generation agents that iteratively refine code toward correctness *and* simplicity.

2. **GitHub Actions / MR gating** — Automatically deny a merge request if it increases cyclomatic complexity or reduces MI below a threshold. A simple CI action can enforce this policy.

3. **Downstream automated tooling** — Feed per-file complexity scores into unit-test generators, LLM-powered refactoring tools, or documentation generators to focus effort on the highest-risk files.

4. **Technical debt tracking** — Run CodeKritik across the full git history of a project to chart complexity trends over time and identify when debt accumulation accelerated.

---

## Roadmap

### v0.3.0 ✅ (current)
- [x] MCP server with 12 tools
- [x] Ollama integration example
- [x] Fixed ASM / IR low-level language metrics
- [x] Dark-theme web UI with error handling
- [x] `COMMIT_TYPE_RULES` single source of truth for commit classification
- [x] `sys.executable` venv-safe subprocess calls throughout

### v0.4.0
- [ ] Dockerisation
- [ ] GitHub Actions CI template
- [ ] Complexity trend charts in the web UI

### v1.0.0
- [ ] Full unit test suite across all languages
- [ ] Issue and PR templates
- [ ] Production-ready deployment guide

---

## Adding a New Language

CodeKritik is designed so that adding a new language requires **no Python code changes** — only JSON/text config edits. There are exactly three files to update.

### Overview of the three config files

| File | Purpose |
|------|---------|
| `metrics_cfgs/program_file_exts_map.json` | Maps language name → list of file extensions |
| `metrics_cfgs/program_file_exts.txt` | Flat list of every extension the runner should scan |
| `metrics_cfgs/hll_tokens.json` | Per-language token definitions used to compute metrics |

---

### Step 1 — Register the file extensions

**`metrics_cfgs/program_file_exts_map.json`** — add a new key with the language name and its extensions:

```json
{
  "Python":  [".py"],
  "Go":      [".go"],
  "Kotlin":  [".kt", ".kts"]   ← add your language here
}
```

The key (e.g. `"Kotlin"`) is the canonical name used in all metric output files. It must be unique.

---

### Step 2 — Add the extensions to the flat scanner list

**`metrics_cfgs/program_file_exts.txt`** — append each new extension on its own line:

```
.py
.go
.kt        ← add
.kts       ← add
```

The runner uses this file to decide which files to open. Any extension not listed here is silently skipped.

---

### Step 3 — Define the language tokens

**`metrics_cfgs/hll_tokens.json`** — add a new top-level key matching the name you used in Step 1. The value is an object with five required arrays:

| Key | What to put here |
|-----|-----------------|
| `assignments` | Assignment operators (`=`, `+=`, `:=`, etc.) |
| `branches` | Branch keywords (`if`, `else`, `when`, etc.) |
| `conditionals` | Comparison operators (`==`, `!=`, `<`, `>`, etc.) |
| `loops` | Loop keywords (`for`, `while`, `do`, etc.) |
| `comments` | Comment markers (`//`, `/*`, `*`, `#`, etc.) |

**Example — adding Kotlin:**

```json
{
  "Python": { "...": "..." },
  "Go":     { "...": "..." },

  "Kotlin": {
    "assignments": [
      "=", "+=", "-=", "*=", "/=", "%=",
      "and=", "or=", "xor=", "shl=", "shr="
    ],
    "branches": [
      "if", "else", "when", "else if"
    ],
    "conditionals": [
      "==", "!=", "<", ">", "<=", ">=",
      "===", "!==", "in", "!in", "is", "!is"
    ],
    "loops": [
      "for", "while", "do"
    ],
    "comments": [
      "//", "/*", "*", "*/"
    ]
  }
}
```

> **Tip:** The token lists are used for substring matching against each line of source code. Include all syntactic forms you want counted — the more complete the lists, the more accurate the Halstead, ABC, and Cyclomatic Complexity scores will be.

---

### Step 4 — Verify

Run the static analyser on a directory containing files of your new language:

```bash
python3 static_analyzer.py --dir /path/to/kotlin/project
```

Check the output logs:

```
logs_<hash>/
├── loc/
│   ├── loc_per_file.json       ← should show .kt files
│   ├── loc_per_language.json   ← should show "Kotlin" key
│   └── loc_global.json
├── halstead/
│   └── halstead_per_language.json   ← "Kotlin" entry
...
```

If `"Kotlin"` does not appear in the per-language output, double-check that:
1. The key in `program_file_exts_map.json` exactly matches the key in `hll_tokens.json` (case-sensitive).
2. The extensions in `program_file_exts.txt` include the ones you added to the map.
3. The target directory actually contains files with those extensions.

---

### Assembly and IR languages

Assembly (`.asm`, `.s`) and IR (`.ll`, `.gimple`) languages use **separate token files** — `asm_tokens.json` and `ir_tokens.json` respectively — and are detected automatically by `detect_assembly_language()` / `detect_ir_language()`. To add a new assembly dialect or IR format, follow the same three-step process but edit `asm_tokens.json` or `ir_tokens.json` instead of `hll_tokens.json`, and add the extension to the `"Assembly"` or `"IR_GROUP"` key in `program_file_exts_map.json`.

---

## License

CodeKritik is permanently under the [MIT License](LICENSE).
