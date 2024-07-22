import sys
sys.path.append('../metrics')
from loc_utils import *
from utils_main import *
from abc_metric_utils import *
from halstead_metric_utils import *
import argparse
from datetime import datetime
import hashlib 
import random

def main():

    parser = argparse.ArgumentParser(description="Count lines of code (LOC) for specific file extensions.")
    
    parser.add_argument('--dir',
                        type = str,
                        required = True,
                        help = "Directory to start counting LOC from.")

    parser.add_argument('--json_exts',
                        type = str,
                        default = "./metrics_cfgs/program_file_exts_map.json",
                        help = "JSON file containing programming language to file extensions mapping.")

    parser.add_argument('--file_exts',
                        type = str,
                        default = "./metrics_cfgs/program_file_exts.txt",
                        help = "Text file containing file extensions to count lines for.")
    
    parser.add_argument('--log',
                        type = bool,
                        default = True,
                        help = "whether or not to save LOC analysis to file")

    parser.add_argument('--runner_cfg',
                        type = str,
                        default = '../metrics_runner_cfg.txt',
                        help = 'path to the metrics_runner CFG file which specifies which metrics to compute or omit')


    args = parser.parse_args()
    runner_cfg = parse_runner_cfg(args.runner_cfg)
    extensions_map = read_valid_extensions(args.json_exts)
    extensions_to_count = read_extensions_to_count(args.file_exts)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_hash = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    if args.log: 
        if not os.path.exists('logs'):
            os.makedirs('logs')
        f = open('./logs/runner_log_{}.txt'.format(file_hash[:8],file_hash[:8]),'w')
        f.write('CODE ANALYSIS FOR DIR: {}\n'.format(args.dir))
        f.write('TIME: {}\n'.format(current_time))
        f.write('HASH: {}\n'.format(file_hash))
    if runner_cfg['LOC']:
        loc_by_language, total_lines = count_lines_of_code(args.dir, extensions_to_count, extensions_map) #check upper and lowercase bool
        print_loc_percentage(loc_by_language, total_lines)
        if args.log: 
            langs = list(loc_by_language.keys())
            f.write('LOC: {}\n'.format(total_lines))
            for lang in langs:
                loc_lang = loc_by_language[lang]
                f.write('{}: {}\n'.format(lang,loc_lang))
        

    if runner_cfg['ABC']:
        #TODO add print statements
        abc_code_metrics = get_abc_metrics(args.dir,
                                           extensions_to_count,
                                           extensions_map)
        abc_summary_metrics = get_abc_summary_metrics(abc_code_metrics)
        if args.log:
            f.write('ABC_SCORE: {}\n'.format(abc_summary_metrics['global']['abc_metric']))
            f.write('Assignments: {}\n'.format(abc_summary_metrics['global']['assignments']))
            f.write('Branches: {}\n'.format(abc_summary_metrics['global']['branches']))
            f.write('Conditions: {}\n'.format(abc_summary_metrics['global']['conditions']))
            for lang in langs: 
                f.write('ABC_SCORE - {}: {}\n'.format(lang,abc_summary_metrics[lang]['total_abc_metric']))
                f.write('Assignments - {}: {}\n'.format(lang,abc_summary_metrics[lang]['total_assignments']))
                f.write('Branches - {}: {}\n'.format(lang,abc_summary_metrics[lang]['total_branches']))
                f.write('Conditions - {}: {}\n'.format(lang,abc_summary_metrics[lang]['total_conditions']))
            
    
    if runner_cfg['Halstead']:
        
        #TODO add print statements
        halstead_metrics = halstead_process_directory(args.dir,
                                                      extensions_to_count,
                                                      extensions_map)
        halstead_file_path = './logs/halstead_metrics_{}.json'.format(file_hash[:8])
        json.dump(halstead_metrics,open(halstead_file_path,'w'))
        f.write('Halstead_metrics JSON path: {}\n'.format(halstead_file_path))

    if runner_cfg['ipl_estimation']:
        #TODO add print statements
        assert runner_cfg['ABC'] is True
        global_assignments = abc_summary_metrics['global']['assignments']
        global_branches = abc_summary_metrics['global']['branches']
        global_conditions = abc_summary_metrics['global']['conditions']

        global_ipl_estimate = estimate_ipl(assignments = global_assignments,
                                           branches = global_branches,
                                           conditions = global_conditions)
        if args.log:
            f.write('Instruction Path Length (IPL) estimate: {} <= IPL <= {}\n'.format(global_ipl_estimate['lower'],global_ipl_estimate['upper']))
        
            for lang in langs:
                lang_assignments = abc_summary_metrics[lang]['total_assignments']
                lang_branches = abc_summary_metrics[lang]['total_branches']
                lang_conditions = abc_summary_metrics[lang]['total_conditions']

                lang_ipl_estimate = estimate_ipl(assignments = lang_assignments,
                                                branches = lang_branches,
                                                conditions = lang_conditions)

                f.write('Instruction Path Length (IPL) estimate - {}: {} <= IPL <= {}\n'.format(lang,
                                                                                                lang_ipl_estimate['lower'],
                                                                                                lang_ipl_estimate['upper']))
    
    if args.log:
        f.close()


if __name__ == "__main__":

    main()

