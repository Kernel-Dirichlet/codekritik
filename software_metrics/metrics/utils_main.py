import os
import json


def append_timestamp_hash(full_dict,
                          timestamp,
                          hash_):

    new_dict = {'timestamp': timestamp,
                'hash': hash_}
    for key in full_dict.keys():
        new_dict[key] = full_dict[key]
    return new_dict

def dump_final_jsons(prefix_path,final_dicts):

    for key in final_dicts.keys():
        if key not in ['timestamp','hash']:

            parsed_name = key.split('_')
            json_name = parsed_name[0] + '_' + 'metrics.json'
            path = f"{prefix_path}/{json_name}"
            json.dump(final_dicts[key],open(path,'w'),indent = 4)
        else:
            continue


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

