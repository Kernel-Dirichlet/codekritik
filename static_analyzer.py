import sys
import os

#script_dir = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(os.path.join(script_dir,'software_metrics','metrics','metrics_cfgs'))
sys.path.append('software_metrics/metrics')

from loc_utils import *
from utils_main import *
from abc_metric_utils import *
from halstead_metric_utils import *
from cyclomatic_complexity_utils import *
from mi_utils import *
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
                        default = "metrics_cfgs/program_file_exts_map.json",
                        help = "JSON file containing programming language to file extensions mapping.")

    parser.add_argument('--file_exts',
                        type = str,
                        default = "metrics_cfgs/program_file_exts.txt",
                        help = "Text file containing file extensions to count lines for.")
    
    parser.add_argument('--log',
                        type = bool,
                        default = True,
                        help = "whether or not to save LOC analysis to file")

    parser.add_argument('--runner_cfg',
                        type = str,
                        default = 'metrics_runner_cfg.txt',
                        help = 'path to the metrics_runner CFG file which specifies which metrics to compute or omit')


    args = parser.parse_args()
    runner_cfg = parse_runner_cfg(args.runner_cfg)
    extensions_map = read_valid_extensions(args.json_exts)
    extensions_to_count = read_extensions_to_count(args.file_exts)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_hash = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
    
    if args.log: 
        if not os.path.exists('logs_{}'.format(file_hash)):
            os.makedirs('logs_{}'.format(file_hash[:10]))

            if not os.path.exists('logs_{}/abc_metrics'.format(file_hash[:10])):
                os.makedirs('logs_{}/abc_metrics'.format(file_hash[:10]))

            if not os.path.exists('logs_{}/halstead_metrics'.format(file_hash[:10])):
                os.makedirs('logs_{}/halstead_metrics'.format(file_hash[:10]))

            if not os.path.exists('logs_{}/cyclomatic_complexity_metrics'.format(file_hash[:10])):
                os.makedirs('logs_{}/cyclomatic_complexity_metrics'.format(file_hash[:10]))

            if not os.path.exists('logs_{}/loc_metrics'.format(file_hash[:10])):
                os.makedirs('logs_{}/loc_metrics'.format(file_hash[:10]))


    if runner_cfg['LOC']:
        loc_dict = count_lines_of_code(directory = args.dir,
                                      extensions_to_count = extensions_to_count,
                                      extensions_map = extensions_map,
                                      hll_tokens = 'metrics_cfgs/hll_tokens.json',
                                      asm_tokens = 'metrics_cfgs/asm_tokens.json',
                                      ir_tokens = 'metrics_cfgs/ir_tokens.json')

        full_loc_dict = loc_full_analysis(loc_dict,extensions_map)
        final_loc_dict = append_timestamp_hash(full_dict = full_loc_dict,
                                               timestamp = current_time,
                                               hash_ = file_hash)

        _ = dump_final_jsons(prefix_path = './logs_{}/loc_metrics'.format(file_hash[:10]),
                         final_dicts = final_loc_dict)

    if runner_cfg['ABC']:
        abc_dict = abc_process_directory(directory = args.dir,
                                         extensions_to_count = extensions_to_count,
                                         extensions_map = extensions_map,
                                         hll_tokens = 'metrics_cfgs/hll_tokens.json',
                                         asm_tokens = 'metrics_cfgs/asm_tokens.json',
                                         ir_tokens = 'metrics_cfgs/ir_tokens.json')

        full_abc_dict = abc_full_analysis(abc_dict,extensions_map)
        final_abc_dict = append_timestamp_hash(full_dict = full_abc_dict,
                                               timestamp = current_time,
                                               hash_ = file_hash)

        _ = dump_final_jsons(prefix_path = './logs_{}/abc_metrics'.format(file_hash[:10]),
                                            final_dicts = final_abc_dict)

    
    if runner_cfg['Halstead']:
        halstead_metrics = halstead_process_directory(args.dir,
                                                      extensions_to_count,
                                                      extensions_map,
                                                      hll_tokens = 'metrics_cfgs/hll_tokens.json',
                                                      asm_tokens = 'metrics_cfgs/asm_tokens.json',
                                                      ir_tokens = 'metrics_cfgs/ir_tokens.json')
        
        full_halstead_dict = halstead_full_analysis(halstead_metrics,
                                                    extensions_map)

        final_halstead_dict = append_timestamp_hash(full_dict = full_halstead_dict,
                                                    timestamp = current_time,
                                                    hash_ = file_hash)

        _ = dump_final_jsons(prefix_path = './logs_{}/halstead_metrics'.format(file_hash[:10]),
                         final_dicts = final_halstead_dict)

        
    
    if runner_cfg['cyclomatic_complexity']:
        cc_metrics = cc_process_directory(args.dir,
                                          extensions_to_count,
                                          extensions_map,
                                          hll_tokens = 'metrics_cfgs/hll_tokens.json',
                                          asm_tokens = 'metrics_cfgs/asm_tokens.json',
                                          ir_tokens = 'metrics_cfgs/ir_tokens.json')

        full_cc_dict = cc_full_analysis(cc_metrics,extensions_map)
        final_cc_dict = append_timestamp_hash(full_dict = full_cc_dict,
                                              timestamp = current_time,
                                              hash_ = file_hash)
         
        _ = dump_final_jsons(prefix_path = './logs_{}/cyclomatic_complexity_metrics'.format(file_hash[:10]),
                             final_dicts = final_cc_dict)

    
    if runner_cfg['Maintainability_index']:
        assert 'cyclomatic_complexity' in runner_cfg.keys()
        assert 'Halstead' in runner_cfg.keys()
        assert 'LOC' in runner_cfg.keys()
        
        
        mi_metrics = full_maintainability_calc(full_halstead_dict = full_halstead_dict,
                                               full_cc_dict = full_cc_dict,
                                               full_loc_dict = full_loc_dict)
        
        final_mi_metrics = append_timestamp_hash(full_dict = mi_metrics,
                                                 timestamp = current_time,
                                                 hash_ = file_hash)
        json.dump(final_mi_metrics,open('./logs_{}/maintainability_metrics.json'.format(file_hash[:10]),'w'),indent = 4)
    print('metrics finished computing for {}!'.format(args.dir))



if __name__ == "__main__":

    main()
 

