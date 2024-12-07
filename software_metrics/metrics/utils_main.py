import os
import json
import re

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

def detect_assembly_language(content):
    # Define regex patterns for each architecture
    architecture_patterns = {
        "x86": re.compile(r"\b(eax|ebx|ecx|edx|esp|ebp|esi|edi|mov|int|push|pop|jmp|ret)\b",
                          re.IGNORECASE),
        "ARM": re.compile(r"\b(r\d+|ldr|str|b\w*|bl|cmp|add|sub|swi|mov|bx|pop|push)\b",
                          re.IGNORECASE),
        "MIPS": re.compile(r"\b(\$zero|\$t\d+|\$s\d+|\$ra|\$sp|lw|sw|add|sub|j|jal|beq|bne)\b",
                           re.IGNORECASE),
        "RISC-V": re.compile(r"\b(x\d+|addi|lw|sw|beq|jalr|slli|xor|and|auipc|ecall)\b",
                             re.IGNORECASE),
        "PowerPC": re.compile(r"\b(r\d+|li|lwz|stw|addi|b|blr|mtlr|mflr|cmpw|bne|beq)\b",
                              re.IGNORECASE),
        "Z80": re.compile(r"\b(a|b|c|d|e|h|l|af|bc|de|hl|ix|iy|ld|jp|jr|call|ret|inc|dec)\b",
                          re.IGNORECASE),
	"SPARC": re.compile(r"""
        \b(
            add|sub|mul|div|ld|st|cmp|bne|beq|blt|bgt|br|jmp|ret|call|nop|mov|set|or|and|xor|sll|srl|sra
        )\b
        \s+
        (
            %\w+
            |
            [a-zA-Z_]\w*
            |
            [-+]?\d+
            |
            0x[0-9a-fA-F]+
        )+
        \s*
    """, re.VERBOSE | re.IGNORECASE)
    }

    try:
        for architecture, pattern in architecture_patterns.items():
            if pattern.search(content):
                return architecture

    except Exception as e:
        return f"Error processing file: {e}"

def detect_ir_language(content):
    """
    Detects the intermediate representation (IR) language based on provided lines of text.
    :param lines: List of strings representing lines of text or a single string.
    :return: The detected IR language as a string.
    """
    # Patterns for LLVM IR
    llvm_ir_patterns = [
        re.compile(r"\bdefine\b"),       # Function definition
        re.compile(r"%\d+\s*="),        # LLVM typed variables
        re.compile(r"@[\w.]+"),         # Global variables/constants
        re.compile(r"\b(add|sub|mul|div|br|phi|ret|call|load|store)\b"),  # Common instructions
    ]

    # Patterns for SPIR-V
    spirv_patterns = [
        re.compile(r"Op\w+"),           # SPIR-V instructions
        re.compile(r"SPIR-V")           # SPIR-V marker
    ]

    # Patterns for WebAssembly IR
    wasm_patterns = [
        re.compile(r"\(module\b"),      # Module start
        re.compile(r"\(func\b"),        # Function definition
    ]

    # Patterns for GIMPLE
    gimple_patterns = [
        re.compile(r"\b(goto|return|if|label)\b"),  # Common control flow keywords
        re.compile(r"\b[a-z_]\w*_\d+\b"),          # SSA variables like `a_1`, `b_2`
        re.compile(r"\{[^}]*\}"),                  # Function bodies
        re.compile(r"\bint\b.*\("),                # Function header
    ]

    # Check for LLVM IR
    if any(pattern.search(content) for pattern in llvm_ir_patterns):
        return "LLVM"

    # Check for SPIR-V
    if any(pattern.search(content) for pattern in spirv_patterns):
        return "SPIR-V"

    # Check for WebAssembly IR
    if any(pattern.search(content) for pattern in wasm_patterns):
        return "WebAssembly"

    # Check for GIMPLE
    if any(pattern.search(content) for pattern in gimple_patterns):
        return "GIMPLE"

    return "Unknown Intermediate Representation"

