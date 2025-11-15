import os
import json
from utils_main import * 


def fetch_lines(lines,
                language,
                comments_json,
                mode = 'count'):
    
    assert mode in ['count','source'] 

    with open(comments_json, 'r') as f:
        comment_data = json.load(f)
    single_line_comment = comment_data[language]['comments'][0]
    multi_line_comment_start = comment_data[language]['comments'][1] if len(comment_data[language]['comments']) > 1 else None
    multi_line_comment_end = comment_data[language]['comments'][2] if len(comment_data[language]['comments']) > 2 else None
    
    total_lines = 0
    comment_lines = 0
    source_lines = 0
    blank_lines = 0
    in_multi_line_comment = False
    if mode == 'source': 
        sloc = []
        
    for line in lines:
        total_lines += 1
        stripped_line = line.strip()

        if not stripped_line:
            blank_lines += 1
            continue

        if in_multi_line_comment:
            comment_lines += 1
            if multi_line_comment_end and multi_line_comment_end in stripped_line:
                in_multi_line_comment = False
            continue

        if stripped_line.startswith(single_line_comment):
            comment_lines += 1
        elif multi_line_comment_start and multi_line_comment_start in stripped_line:
            comment_lines += 1
            if not multi_line_comment_end or multi_line_comment_end not in stripped_line:
                in_multi_line_comment = True
        else:
            source_lines += 1
            if mode == 'source': 
                sloc.append(line)
    
    if mode == 'source':
        return sloc

    if mode == 'count':
        loc_dict = {'loc': total_lines,
                    'cloc': comment_lines,
                    'sloc': source_lines,
                    'bloc': blank_lines}
        return loc_dict



def count_lines_of_code(directory, 
                        extensions_to_count,
                        extensions_map,
                        mode = 'count',
                        hll_tokens = '../run_metrics/metrics_cfgs/hll_tokens.json',
                        asm_tokens = '../run_metrics/metrics_cfgs/asm_tokens.json',
                        ir_tokens = '../run_metrics/metrics_cfgs/ir_tokens.json'):

    langs = []
    loc_file_dict = {}

    for root, _, files in os.walk(directory):
        for file in files:
            extension = '.' + file.split('.')[-1] 
            if extension in extensions_to_count:
                language = get_language_for_extension(extensions_map, extension)
                if language == "Unknown":
                    continue
                else:
                    file_path = os.path.join(root,file)
                try:
                    with open(file_path,'r') as code_file:
                        code_lines = code_file.readlines()
                except:
                    print(f'error reading file {file_path}, skipping...')
                    continue
                if language == 'Assembly':
                    #no comments allowed in assembly files
                    lang = detect_assembly_language(' '.join(code_lines))
                    loc_dict = fetch_lines(lines = code_lines,
                                           language = lang,
                                           comments_json = asm_tokens,
                                           mode = mode)
                    
                if language in ['LLVM', 'IR_GROUP']:
                    #no comments allowed in IR files
                    lang = detect_ir_language(' '.join(code_lines))
                    loc_dict = fetch_lines(lines = code_lines,
                                           language = lang,
                                           comments_json = ir_tokens,
                                           mode = mode)
                
                if language not in ['Assembly', 'IR_GROUP','LLVM']:
                    lang = language
                    loc_dict = fetch_lines(lines = code_lines,
                                           language = lang,
                                           comments_json = hll_tokens,
                                           mode = mode)
                loc_file_dict[file] = loc_dict
    return loc_file_dict

                    
def loc_full_analysis(loc_dict,
                      extensions_map):
    lang_dict = {}
    files = list(loc_dict.keys())
    for i,file in enumerate(files):
        ext = '.' + file.split('.')[-1]
        lang = get_language_for_extension(extensions_map,ext)
        if lang == 'Unknown':
            continue
        if lang not in lang_dict.keys():
            lang_dict[lang] = {'loc': 0,
                               'bloc': 0,
                               'sloc': 0,
                               'cloc': 0}
            
        if lang in lang_dict.keys():
            for key in loc_dict[file].keys():
                lang_dict[lang][key] += loc_dict[file][key]

    global_dict = {k: 0 for k in lang_dict[lang]}
    for lang in lang_dict.keys():
        for key in lang_dict[lang].keys():
            global_dict[key] += lang_dict[lang][key]
    
    percentage_dict = {}
    
    for lang in lang_dict.keys():
        percentage_dict[lang] = {}
        for key in global_dict.keys():
            percentage_dict[lang][key] = (lang_dict[lang][key] / global_dict[key]) * 100
        
         
    #now get LOC percentage per language
    loc_full_dict = {'global_dict': global_dict,
                     'language_dict': lang_dict,
                     'file_dict': loc_dict,
                     'percentage_dict': percentage_dict}

    return loc_full_dict

