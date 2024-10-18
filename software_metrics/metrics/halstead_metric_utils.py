from utils_main import *
from loc_utils import fetch_lines
import numpy as np
import math
import re
 
def parse_assignment(lines, assignment_tokens):
    unique_operators = set()
    unique_operands = set()
    total_operators = 0
    total_operands = 0

    # Build regex pattern from assignment tokens
    assignment_pattern = '|'.join(re.escape(token) for token in assignment_tokens)
    
    for line in lines:
        # Check for any assignment token in the line
        match = re.search(assignment_pattern, line)
        if match:
            token = match.group()
            # Split the statement into LHS and RHS using the assignment token
            lhs, rhs = line.split(token, 1)
            lhs = lhs.strip()
            rhs = rhs.strip()

            # Identify operators and operands in RHS
            operator_pattern = re.compile(r'[+\-*/%&|^<>]=?|==|!=|<=|>=|&&|\|\||!')
            operators = operator_pattern.findall(rhs)
            operands = operator_pattern.split(rhs)
            operands = [operand.strip() for operand in operands if operand.strip()]

            # Add LHS, operators, and operands to their respective sets
            unique_operands.add(lhs)
            unique_operators.update(operators)
            unique_operands.update(operands)

            # Count total operators and operands
            total_operators += len(operators) + 1  # +1 for the assignment operator
            total_operands += len(operands) + 1  # +1 for the LHS operand
        else:
            # Handle lines without assignment tokens to capture standalone operators and operands
            operator_pattern = re.compile(r'[+\-*/%&|^<>]=?|==|!=|<=|>=|&&|\|\||!')
            operators = operator_pattern.findall(line)
            operands = operator_pattern.split(line)
            operands = [operand.strip() for operand in operands if operand.strip()]

            unique_operators.update(operators)
            unique_operands.update(operands)

            total_operators += len(operators)
            total_operands += len(operands)

    return {
        "unique_operators": unique_operators,
        "unique_operands": unique_operands,
        "total_operators": total_operators,
        "total_operands": total_operands
    }

def compute_halstead_metrics(metrics):
    unique_operators_count = len(metrics["unique_operators"])
    unique_operands_count = len(metrics["unique_operands"])
    total_operators_count = metrics["total_operators"]
    total_operands_count = metrics["total_operands"]

    vocabulary_size = unique_operators_count + unique_operands_count
    program_length = total_operators_count + total_operands_count

    if vocabulary_size == 0:  # To avoid division by zero
        return None

    volume = program_length * math.log2(vocabulary_size)
    difficulty = (unique_operators_count / 2) * (total_operands_count / unique_operands_count) if unique_operands_count != 0 else 0
    effort = difficulty * volume
    estimated_bugs = int(volume // 3000) 
    return {
        "unique_operators": unique_operators_count,
        "unique_operands": unique_operands_count,
        "total_operators": total_operators_count,
        "total_operands": total_operands_count,
        "vocabulary_size": vocabulary_size,
        "program_length": program_length,
        "volume": volume,
        "difficulty": difficulty,
        "effort": effort,
        "estimated_bugs": estimated_bugs,
    }

def halstead_process_directory(directory,
                               extensions_to_count,
                               extensions_map,
                               hll_tokens = '../run_metrics/metrics_cfgs/hll_tokens.json',
                               asm_tokens = '../run_metrics/metrics_cfgs/asm_tokens.json',
                               ir_tokens = '../run_metrics/metrics_cfgs/ir_tokens.json'):

    """Processes files in the specified directory and computes Halstead metrics."""
    langs = []
    halstead_metrics = {}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension in extensions_to_count:
                language = get_language_for_extension(extensions_map,extension)
                langs.append(language)
                if language != 'unknown':
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as code_file:
                        code_lines = code_file.readlines()
                    if language == 'Assembly':
                        regexes = json.load(open(asm_tokens))
                        comments_json = asm_tokens
                    if language == 'LLVM':
                        regexes = json.load(open(ir_tokens))
                        comments_json = ir_tokens
                    else:
                        regexes = json.load(open(hll_tokens))
                        comments_json = hll_tokens
                        
                source_code_lines = fetch_lines(lines = code_lines,
                                                language = language,
                                                comments_json = comments_json,
                                                mode = 'source')
                assignment_tokens = regexes[language]['assignments']
                
                ops_dict = parse_assignment(lines = source_code_lines,
                                            assignment_tokens = assignment_tokens)

                halstead_results = compute_halstead_metrics(ops_dict)
                halstead_metrics[file_path] = halstead_results
    
    return halstead_metrics

def halstead_full_analysis(halstead_dict,extensions_map):

    lang_dict = {}
    files = list(halstead_dict.keys())
    for i,file in enumerate(files):
        ext = '.' + file.split('.')[-1]
        lang = get_language_for_extension(extensions_map,ext)
        if lang == 'Unknown':
            continue
        if lang not in lang_dict.keys():
            lang_dict[lang] = {'unique_operators': 0,

                               'unique_operands': 0,
                               'total_operators': 0,
                               'total_operands': 0,
                               'vocabulary_size': 0,
                               'program_length': 0,
                               'volume': 0,
                               'difficulty': 0,
                               'effort': 0,
                               'estimated_bugs': 0}

        if lang in lang_dict.keys():
            for key in halstead_dict[file].keys():
                lang_dict[lang][key] += halstead_dict[file][key]
        
    global_dict = {k: 0 for k in lang_dict[lang]}
    for lang in lang_dict.keys():
        for key in lang_dict[lang].keys():
            global_dict[key] += lang_dict[lang][key]
    halstead_full_dict = {'global_dict': global_dict,
                          'language_dict': lang_dict,
                          'file_dict': halstead_dict}
    return halstead_full_dict
