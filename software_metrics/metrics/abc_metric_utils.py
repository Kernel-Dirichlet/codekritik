import os
import json
import re
import numpy as np
from utils_main import *
from loc_utils import fetch_lines
import json
import re

def get_abcs(json_file, language, lines):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)    
    # Fetch the lists of operators for assignments, branches, and conditionals
    assignments = data[language]['assignments']
    branches = data[language]['branches']
    conditionals = data[language]['conditionals']
    
    # Compile the regex patterns
    # The regex pattern matches any word followed by one of the operators and some value.
    # \b\w+\b matches a whole word (variable name or label) with word boundaries
    # \s* matches any whitespace characters (zero or more)
    # (operator) matches one of the operators
    # .+ matches one or more of any character (the assigned value or target label)
    
    # Compile patterns for assignments
    escaped_assignments = [re.escape(op) for op in assignments]
    assignment_pattern = re.compile(r'(\b\w+\b\s*' + r'|'.join(escaped_assignments) + r'\s*.+)')
    
    # Compile patterns for branches
    escaped_branches = [re.escape(op) for op in branches]
    branch_pattern = re.compile(r'(\b' + r'|'.join(escaped_branches) + r'\b)')
    
    # Compile patterns for conditionals
    escaped_conditionals = [re.escape(op) for op in conditionals]
    conditional_pattern = re.compile(r'(\b' + r'|'.join(escaped_conditionals) + r'\b)')

    # Search through lines for matching patterns and count them
    assignment_count = 0
    branch_count = 0
    conditional_count = 0

    for line in lines:
        if assignment_pattern.search(line):
            assignment_count += 1
        if branch_pattern.search(line):
            branch_count += 1
        if conditional_pattern.search(line):
            conditional_count += 1

    return {"assignments": assignment_count,
            "branches": branch_count,
            "conditionals": conditional_count}

def abc_process_directory(directory,
                          extensions_to_count,
                          extensions_map,
                          hll_tokens = '../run_metrics/metrics_cfgs/hll_tokens.json',
                          asm_tokens = '../run_metrics/metrics_cfgs/asm_tokens.json',
                          ir_tokens = '../run_metrics/metrics_cfgs/ir_tokens.json'):
    langs = []
    abc_metrics = {}
    for root, dirs, files in os.walk(directory):
        for file in files: 
            extension = '.' + file.split('.')[-1]
            language = get_language_for_extension(extensions_map,extension)
            langs.append(language)
            if language == 'Unknown':
                continue
            else:
                file_path = os.path.join(root,file)
            try:
                with open(file_path,'r') as code_file:
                    code_lines = code_file.readlines()
                    # import pdb ; pdb.set_trace()
                    if language == 'Assembly':
                        comments_json = asm_tokens
                    if language in ['LLVM','IR_GROUP']:
                        comments_json = ir_tokens
                    else:
                        comments_json = hll_tokens
                    source_code_lines = fetch_lines(lines = code_lines,
                                                    language = language,
                                                    comments_json = comments_json,
                                                    mode = 'source')
            except:
                print(f'error reading file {file_path}, skipping...')
                continue
            if language == 'Assembly':
                abc_dict = get_abcs(json_file = asm_tokens,
                                    language = language,
                                    lines = source_code_lines)
                
            if language in ['LLVM', 'IR_GROUP']:
                abc_dict = get_abcs(json_file = ir_tokens,
                                    language = language,
                                    lines = source_code_lines)
            else:
                abc_dict = get_abcs(json_file = hll_tokens,
                                    language = language,
                                    lines = source_code_lines)

            a = abc_dict['assignments']
            b = abc_dict['branches']
            c = abc_dict['conditionals']
            abc_score = np.sqrt(a + b + c)
            abc_dict['abc_score'] = round(abc_score,1).item()
            abc_metrics[file_path] = abc_dict
            
    
    return abc_metrics


def abc_full_analysis(abc_dict,
                      extensions_map,
                      output_dir='repo_analysis'):
    lang_dict = {}
    files = list(abc_dict.keys())
    for i,file in enumerate(files):
        ext = '.' + file.split('.')[-1]
        lang = get_language_for_extension(extensions_map,ext)
        if lang == 'Unknown':
            continue
        if lang not in lang_dict.keys():
            lang_dict[lang] = {'assignments': 0,
                               'branches': 0,
                               'conditionals': 0,
                               'abc_score': 0}
        if lang in lang_dict.keys():
            for key in abc_dict[file].keys():
                lang_dict[lang][key] += abc_dict[file][key]

    global_dict = {'assignments': 0,
                   'branches': 0,
                   'conditionals': 0,
                   'abc_score': 0}

    for lang in lang_dict.keys():
        for key in lang_dict[lang].keys():
            global_dict[key] += lang_dict[lang][key]
    abc_full_dict = {'global_dict': global_dict,
                     'language_dict': lang_dict,
                     'file_dict': abc_dict}

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write results to repo_analysis/abc_full_analysis.json
    output_path = os.path.join(output_dir, 'abc_full_analysis.json')
    with open(output_path, 'w') as f:
        json.dump(abc_full_dict, f, indent=2)

    return abc_full_dict


def estimate_ipl(assignments,branches,conditionals): 

    lower_bnd = assignments + branches
    upper_bnd = lower_bnd + conditionals
    bounds = {'upper': upper_bnd,
              'lower': lower_bnd}
    return bounds

