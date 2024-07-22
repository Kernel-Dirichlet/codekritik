from utils_main import *
import numpy as np 
def halstead_process_directory(directory,
                               extensions_to_count,
                               extensions_map):

    """Processes files in the specified directory and computes Halstead metrics."""

    #lang_halstead_metrics = {lang: {'metrics': [], 'global_metrics': None} for lang in lang_extension_map.keys()}
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
                        code = code_file.read()
                        halstead_results = compute_halstead_metrics(code)
                        halstead_metrics[language] = halstead_results
    
    return halstead_metrics


def compute_halstead_metrics(code):
    # Initialize dictionaries to track operators and operands
    operators = {}
    operands = {}

    # Tokenize the code into individual tokens (words)
    tokens = code.split()

    for token in tokens:
        if token.isidentifier():
            # If the token is an identifier (variable), add it to operands dictionary
            if token not in operands:
                operands[token] = 1
            else:
                operands[token] += 1
        else:
            # If the token is an operator, add it to operators dictionary
            if token not in operators:
                operators[token] = 1
            else:
                operators[token] += 1

    # Calculate Halstead metrics using the formulas
    unique_operators = len(operators)
    unique_operands = len(operands)
    total_operators = sum(operators.values())
    total_operands = sum(operands.values())
    program_length = total_operators + total_operands
    vocabulary_size = unique_operators + unique_operands
    difficulty = (unique_operators / 2) * (total_operands / unique_operands)
    volume = program_length * np.log2(vocabulary_size)
    effort = difficulty * volume
    bugs = volume / 3000  # Estimated bugs based on volume

    # Construct a dictionary containing both Halstead metrics and variable tracking
    halstead_metrics = {
        'unique_operators': unique_operators,
        'unique_operands': unique_operands,
        'total_operators': total_operators,
        'total_operands': total_operands,
        'program_length': program_length,
        'vocabulary_size': vocabulary_size,
        'difficulty': difficulty,
        'volume': volume,
        'effort': effort,
        'bugs': bugs,
        'variables': operands  # Include the variables tracking in the metrics dictionary
    }

    return halstead_metrics
