import os
import json
import re
import numpy as np
from utils_main import * 
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

    return {"assignments": assignment_count, "branches": branch_count, "conditionals": conditional_count}


def get_abc_metrics(directory, 
                    extensions_to_count,
                    extensions_map,
                    hll_tokens = '../run_metrics/metrics_cfgs/hll_tokens.json',
                    asm_tokens = '../run_metrics/metrics_cfgs/asm_tokens.json',
                    llvm_tokens = '../run_metrics/metrics_cfgs/llvm_tokens.json'):

    code_metrics = {}
    langs = []
    for root, _, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension in extensions_to_count:
                language = get_language_for_extension(extensions_map, extension)
                langs.append(language)
                if language != "Unknown":
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding = 'utf-8') as f:
                        lines = f.readlines()
                        #assignments = sum(line.count('=') for line in lines) 
                        #branches = sum(1 for line in lines if re.search(r'\b(if|for|while|elif|else:|switch|case|else if|elseif)\b', line))
                        #conditions = sum(1 for line in lines if re.search(r'\b(if|elif|else:|switch|case)\b', line))
                        if extension in ['.asm','.a']:
                            abc_dict = get_abcs(json_file = asm_tokens,
                                                language = language,
                                                lines = lines)
                        if extension == '.ll':
                            abc_dict = get_abcs(json_file = llvm_tokens,
                                                language = language,
                                                lines = lines)
                        else:
                            abc_dict = get_abcs(json_file = hll_tokens,
                                                language = language,
                                                lines = lines)

                        assignments = abc_dict['assignments']
                        branches = abc_dict['branches']
                        conditionals = abc_dict['conditionals']
                        abc_metric = np.sqrt(assignments + branches + conditionals) #ABC metric computation
                        #note the ABC score is rounded to the nearest tenth by convention
                        code_metrics[filepath] = {'language': language,
                                                  'assignments': assignments,
                                                  'branches': branches,
                                                  'conditionals': conditionals,
                                                  'abc_metric': round(abc_metric,1).item(),
                                                  'langs': langs}
    return code_metrics

def get_abc_summary_metrics(abc_code_metrics):
    '''
    function to summarize metrics across language
    '''
    summary = {}  # Initialize the summary dictionary
    for filepath, metrics in abc_code_metrics.items():
        language = metrics['language']

        # Initialize language entry if it doesn't exist in summary
        if language not in summary:
            summary[language] = {
                'total_assignments': 0,
                'total_branches': 0,
                'total_conditionals': 0,
                'total_abc_metric': 0
            }
        
        # Sum the metrics for the current file to the language totals
        summary[language]['total_assignments'] += metrics['assignments']
        summary[language]['total_branches'] += metrics['branches']
        summary[language]['total_conditionals'] += metrics['conditionals']
        summary[language]['total_abc_metric'] += metrics['abc_metric']

    global_abc_metrics = {}
    assignments = 0
    branches = 0 
    conditionals = 0
    abc_score = 0
    for lang, abc_dict in summary.items():
        assignments += abc_dict['total_assignments']
        branches += abc_dict['total_branches']
        conditionals += abc_dict['total_conditionals']
        abc_score += abc_dict['total_abc_metric']

    global_abc_metrics['assignments'] = assignments
    global_abc_metrics['branches'] = branches
    global_abc_metrics['conditionals'] = conditionals
    global_abc_metrics['abc_metric'] = abc_score
    summary['global'] = global_abc_metrics
    return summary

def estimate_ipl(assignments,branches,conditionals): 

    lower_bnd = assignments + branches
    upper_bnd = lower_bnd + conditionals
    bounds = {'upper': upper_bnd,
              'lower': lower_bnd}
    return bounds 


