import json
import re
import os
from utils_main import * 

def dfs(node,visited,graph):
    stack = [node]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current])

def count_connected_components(nodes,edges):
    graph  = {node: [] for node,_ in nodes}
    for from_node, to_node, _ in edges:
        graph[from_node].append(to_node)
        graph[to_node].append(from_node)
    visited = set()
    connected_components = 0
    for node in graph:
        if node not in visited:
            dfs(node,visited,graph)
            connected_components += 1
    return connected_components


def compile_patterns(constructs):
    assignment_pattern = re.compile('|'.join(re.escape(token) for token in constructs["assignments"]))
    branch_pattern = re.compile('|'.join(re.escape(token) for token in constructs["branches"]))
    conditional_pattern = re.compile('|'.join(re.escape(token) for token in constructs["conditionals"]))
    loop_pattern = re.compile('|' .join(re.escape(token) for token in constructs["loops"]))
    pattern_dict = {'assignment_pattern': assignment_pattern,
                    'branch_pattern': branch_pattern,
                    'conditional_pattern': conditional_pattern,
                    'loop_pattern': loop_pattern}

    return pattern_dict

def add_node(nodes, label, node_counter):
    node = f"N{node_counter}"
    nodes.append((node, label))
    return node, node_counter + 1

def add_edge(edges, from_node, to_node, direction):
    edges.append((from_node, to_node, direction))

def analyze_code_lines(code_lines, patterns):

    assignment_pattern = patterns['assignment_pattern']
    branch_pattern = patterns['branch_pattern']
    conditional_pattern = patterns['conditional_pattern']
    loop_pattern = patterns['loop_pattern']

    nodes = []
    edges = []
    node_counter = 0

    current_node, node_counter = add_node(nodes, "start", node_counter)

    for line in code_lines:
        stripped_line = line.strip()

        if assignment_pattern.search(stripped_line):
            next_node, node_counter = add_node(nodes, "assign", node_counter)
            add_edge(edges, current_node, next_node, "right")
            current_node = next_node
        if branch_pattern.search(stripped_line):
            next_node, node_counter = add_node(nodes, "branch", node_counter)
            add_edge(edges, current_node, next_node, "right")
            current_node = next_node
        if conditional_pattern.search(stripped_line):
            next_node, node_counter = add_node(nodes, "conditional", node_counter)
            add_edge(edges, current_node, next_node, "right")
            current_node = next_node
        if loop_pattern.search(stripped_line):
            next_node, node_counter = add_node(nodes, "loop", node_counter)
            add_edge(edges, current_node, next_node, "right")
            current_node = next_node

    end_node, node_counter = add_node(nodes, "end", node_counter)
    add_edge(edges, current_node, end_node, "right")

    return nodes, edges

def build_cfg_ascii(nodes, edges):
    node_positions = {node: i for i, (node, _) in enumerate(nodes)}
    max_position = max(node_positions.values())
    
    cfg_ascii = [""] * (max_position + 1)
    for node, label in nodes:
        pos = node_positions[node]
        cfg_ascii[pos] += f"{node} [{label}]"
    
    for from_node, to_node, direction in edges:
        from_pos = node_positions[from_node]
        to_pos = node_positions[to_node]
        
        if direction == "right":
            cfg_ascii[from_pos] += " -> " + cfg_ascii[to_pos]
        elif direction == "left":
            cfg_ascii[to_pos] = cfg_ascii[from_pos] + " <- " + cfg_ascii[to_pos]
        elif direction == "up":
            cfg_ascii[to_pos] = f" ^\n| \n{cfg_ascii[to_pos]}"
        elif direction == "down":
            cfg_ascii[from_pos] += f"\n|\nv \n{cfg_ascii[to_pos]}"
    
    return "\n".join(cfg_ascii)

def compute_cyclomatic_complexity(code_lines,
                                  language,
                                  lang_dict):
        
    patterns = compile_patterns(lang_dict[language])
    nodes, edges = analyze_code_lines(code_lines, patterns)
    
    cfg_ascii = build_cfg_ascii(nodes, edges)
    
    #Here we use DFS on the CFG to accurately fetch the number of connected components

    cyclomatic_complexity = len(edges) - len(nodes) + (2*count_connected_components(nodes,edges))

    return {
        "cyclomatic_complexity": cyclomatic_complexity,
        "cfg": cfg_ascii
    }

def cc_process_directory(directory,
                         extensions_to_count,
                         extensions_map,
                         hll_tokens = '../run_metrics/metrics_cfgs/hll_tokens.json',
                         asm_tokens = '../run_metrics/metrics_cfgs/asm_tokens.json',
                         llvm_tokens = '../run_metrics/metrics_cfgs/llvm_tokens.json'):

    langs, cc_dict = [], {}
    for root,dirs,files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension in extensions_to_count: 
                language = get_language_for_extension(extensions_map,extension)
                langs.append(language)
                if language != 'unknown':
                    file_path = os.path.join(root,file)
                    with open(file_path,'r') as code_file:
                        code_lines = code_file.readlines()
                    if language == 'Assembly':
                        lang_dict = json.load(open(asm_tokens))
                    if language == 'LLVM':
                        lang_dict = json.load(open(llvm_tokens))
                    else:
                        lang_dict = json.load(open(hll_tokens))

                    results = compute_cyclomatic_complexity(code_lines = code_lines,
                                                            language = language,
                                                            lang_dict = lang_dict)
                    cc_dict[file_path] = results
    return cc_dict

def cc_full_analysis(cc_dict,extensions_map):

    files = list(cc_dict.keys())
    lang_dict = {}
    for i,file in enumerate(files):
        ext = '.' + file.split('.')[-1] 
        lang = get_language_for_extension(extensions_map,ext)
        if lang not in lang_dict.keys():
            lang_dict[lang] = {'cyclomatic_complexity': 0}
        else:
            lang_dict[lang]['cyclomatic_complexity'] += cc_dict[file]['cyclomatic_complexity']

    total_complexity = 0
    for lang in lang_dict.keys():
        total_complexity += lang_dict[lang]['cyclomatic_complexity']
    global_dict = {'cyclomatic_complexity': total_complexity}

    full_dict = {'file_dict': cc_dict,
                 'language_dict': lang_dict,
                 'global_dict': global_dict}
    return full_dict





