import os
import json
import re
import numpy as np
from utils_main import * 


def get_abc_metrics(directory, extensions_to_count, extensions_map):
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
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        assignments = sum(line.count('=') for line in lines)
                        branches = sum(1 for line in lines if re.search(r'\b(if|for|while|elif|else:|switch|case|else if|elseif)\b', line))
                        conditions = sum(1 for line in lines if re.search(r'\b(if|elif|else:|switch|case)\b', line))
                        abc_metric = np.sqrt(assignments + branches + conditions) #ABC metric computation
                        code_metrics[filepath] = {'language': language,
                                                  'assignments': assignments,
                                                  'branches': branches,
                                                  'conditions': conditions,
                                                  'abc_metric': abc_metric,
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
                'total_conditions': 0,
                'total_abc_metric': 0
            }

        # Sum the metrics for the current file to the language totals
        summary[language]['total_assignments'] += metrics['assignments']
        summary[language]['total_branches'] += metrics['branches']
        summary[language]['total_conditions'] += metrics['conditions']
        summary[language]['total_abc_metric'] += metrics['abc_metric']

    global_abc_metrics = {}
    assignments = 0
    branches = 0 
    conditions = 0
    abc_score = 0
    for lang, abc_dict in summary.items():
        assignments += abc_dict['total_assignments']
        branches += abc_dict['total_branches']
        conditions += abc_dict['total_conditions']
        abc_score += abc_dict['total_abc_metric']

    global_abc_metrics['assignments'] = assignments
    global_abc_metrics['branches'] = branches
    global_abc_metrics['conditions'] = conditions
    global_abc_metrics['abc_metric'] = abc_score
    summary['global'] = global_abc_metrics
    return summary

def estimate_ipl(assignments,branches,conditions): 

    lower_bnd = assignments + branches
    upper_bnd = lower_bnd + conditions
    bounds = {'upper': upper_bnd,
              'lower': lower_bnd}
    return bounds 


