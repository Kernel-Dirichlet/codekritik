"""
CodeKritik × Ollama — MCP tool-calling client example
======================================================

This script shows how to wire an Ollama local model to the CodeKritik
MCP server so the model can autonomously call static-analysis and
git-history tools.

Prerequisites
-------------
1. Ollama running locally:   ollama serve
2. A tool-capable model:     ollama pull qwen2.5:7b   (or llama3.1, mistral-nemo, etc.)
3. MCP server running:       python mcp_servers/codekritik_metrics_server.py --transport http
4. Python packages:          pip install ollama mcp fastmcp

Usage
-----
    python mcp_servers/ollama_mcp_client.py \
        --model qwen2.5:7b \
        --server http://127.0.0.1:8000 \
        --prompt "Analyse the cyclomatic complexity of /path/to/my/project"
"""

import argparse
import asyncio
import json
import sys

import ollama
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


# ── Helpers ──────────────────────────────────────────────────────────────────

def _mcp_tool_to_ollama(tool) -> dict:
    """Convert an MCP ToolInfo object to the Ollama tool-calling schema."""
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description or "",
            "parameters": tool.inputSchema if tool.inputSchema else {"type": "object", "properties": {}},
        },
    }


async def run_agent(model: str, server_url: str, user_prompt: str) -> None:
    """
    Connect to the CodeKritik MCP server, discover its tools, then run an
    Ollama model in an agentic loop that calls tools until the model produces
    a final text answer.
    """
    async with streamablehttp_client(server_url) as (read, write, _):
        async with ClientSession(read, write) as session:
            # ── 1. Initialise MCP session & discover tools ────────────────
            await session.initialize()
            tools_response = await session.list_tools()
            ollama_tools = [_mcp_tool_to_ollama(t) for t in tools_response.tools]

            print(f"[codekritik-mcp] Connected to {server_url}")
            print(f"[codekritik-mcp] {len(ollama_tools)} tools available: "
                  f"{[t['function']['name'] for t in ollama_tools]}\n")

            # ── 2. Agentic loop ───────────────────────────────────────────
            messages = [{"role": "user", "content": user_prompt}]
            client = ollama.AsyncClient()

            while True:
                response = await client.chat(
                    model=model,
                    messages=messages,
                    tools=ollama_tools,
                )
                msg = response.message

                # No tool calls → model produced a final answer
                if not msg.tool_calls:
                    print("\n── Model response ──────────────────────────────")
                    print(msg.content)
                    break

                # Append the assistant turn (with tool_calls) to history
                messages.append({"role": "assistant", "content": msg.content or "", "tool_calls": msg.tool_calls})

                # ── 3. Dispatch each tool call to the MCP server ──────────
                for tool_call in msg.tool_calls:
                    fn_name = tool_call.function.name
                    fn_args = tool_call.function.arguments or {}

                    print(f"[tool call] {fn_name}({json.dumps(fn_args, indent=2)})")

                    try:
                        result = await session.call_tool(fn_name, fn_args)
                        tool_output = json.dumps(result.content[0].text if result.content else {})
                    except Exception as exc:
                        tool_output = json.dumps({"error": str(exc)})

                    print(f"[tool result] {tool_output[:300]}{'...' if len(tool_output) > 300 else ''}\n")

                    messages.append({
                        "role": "tool",
                        "content": tool_output,
                    })


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="CodeKritik × Ollama MCP client")
    parser.add_argument("--model",  default="qwen2.5:7b",
                        help="Ollama model name (must support tool calling)")
    parser.add_argument("--server", default="http://127.0.0.1:8000",
                        help="URL of the running CodeKritik MCP server")
    parser.add_argument("--prompt", required=True,
                        help="Natural-language prompt for the agent")
    args = parser.parse_args()

    asyncio.run(run_agent(args.model, args.server, args.prompt))


if __name__ == "__main__":
    main()
