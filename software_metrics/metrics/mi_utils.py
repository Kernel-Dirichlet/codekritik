import math 


def calculate_maintainability_index(halstead_volume,
                                    cyclomatic_complexity,
                                    sloc,
                                    cloc):

    V = float(halstead_volume)
    cc = int(cyclomatic_complexity)
    effective_loc = sloc + cloc
    comment_percentage = (cloc / effective_loc) * 100 if effective_loc > 0 else 0 
    mi_raw = 171 - 5.2 * math.log(V) - 0.23 * cc - 16.2 * math.log(effective_loc) + 50 * math.sin(math.sqrt(2.4 * comment_percentage))
    mi_normalized = max(0,min(100,mi_raw * (100/171)))
    return mi_normalized

def full_maintainability_calc(full_halstead_dict,
                              full_cc_dict,
                              full_loc_dict):

    #keys are the file paths
    #NOTE: Maintainability is calculated w/SLOC rather than LOC
    mi_lang_dict = {}
    for lang in full_halstead_dict['language_dict'].keys():
        
        lang_halstead_vol = full_halstead_dict['language_dict'][lang]['volume']
        lang_cc = full_cc_dict['language_dict'][lang]['cyclomatic_complexity']
        lang_sloc = full_loc_dict['language_dict'][lang]['sloc']
        lang_cloc = full_loc_dict['language_dict'][lang]['cloc']

        mi_lang_dict[lang] = calculate_maintainability_index(halstead_volume = lang_halstead_vol,
                                                             cyclomatic_complexity = lang_cc,
                                                             sloc = lang_sloc,
                                                             cloc = lang_cloc)
    
    global_halstead_vol = full_halstead_dict['global_dict']['volume']
    global_cc = full_cc_dict['global_dict']['cyclomatic_complexity']
    global_sloc = full_loc_dict['global_dict']['sloc']
    global_cloc = full_loc_dict['global_dict']['cloc']

    
    global_mi = calculate_maintainability_index(halstead_volume = global_halstead_vol,
                                                cyclomatic_complexity = global_cc,
                                                sloc = global_sloc,
                                                cloc = global_cloc)

    full_mi_dict = {'language_dict': mi_lang_dict,
                    'global_dict': global_mi}

    return full_mi_dict

