import os
import json


def read_valid_extensions(file_path): 
    extensions = json.load(open(file_path,'r'))
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

def read_lang_regex_json(file_path):

    lang_regex_dict = json.load(open(file_path,'r'))
    import pdb ; pdb.set_trace()

def parse_runner_cfg(file_path):
    mapping = {}  # Initialize an empty dictionary to store the key-value mappings
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading and trailing whitespaces
                if line:  # Skip empty lines
                    parts = line.split(':')
                    if len(parts) == 2:
                        key = parts[0].strip()  # Extract the key
                        value = bool(parts[1].strip())  # Convert the value to a boolean
                        mapping[key] = value  # Add the key-value pair to the dictionary
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    return mapping

