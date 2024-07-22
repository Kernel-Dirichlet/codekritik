import os
import json
from collections import defaultdict
from utils_main import * 
'''
def read_valid_extensions(file_path):
    with open(file_path, 'r') as f:
        extensions = json.load(f)
    return extensions

def read_extensions_to_count(file_path):
    with open(file_path, 'r') as f:
        extensions = [line.strip() for line in f if line.strip()]
    return extensions

def get_language_for_extension(extensions_map, extension):
    for language, ext_list in extensions_map.items():
        if extension in ext_list:
            return language
    return "Unknown"
'''
def count_lines_of_code(directory, extensions_to_count, extensions_map):
    loc_by_language = defaultdict(int)
    total_lines = 0

    for root, _, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            if extension in extensions_to_count:
                language = get_language_for_extension(extensions_map, extension)
                if language != "Unknown":
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        loc_by_language[language] += len(lines)
                        total_lines += len(lines)

    return loc_by_language, total_lines

def print_loc_percentage(loc_by_language, total_lines):
    print("Lines of Code (LOC) by Language:\n")
    for language, loc in loc_by_language.items():
        percentage = (loc / total_lines) * 100 if total_lines > 0 else 0
        print(f"{language}: {loc} lines ({percentage:.2f}%)\n")
    print(f"LOC: {total_lines}\n")


