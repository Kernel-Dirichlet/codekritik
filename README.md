# Codemetrics
This repository aims to provide a suite of static analysis tools to analyze code complexity. This is currently mostly a collection of heuristics, but will evolve with time. This repository also computes software complexity by *language* not simply an aggregate complexity across languages (which it also computes). It is also easy to add support for additional languages beyond the 20 currently included. 

## Usage

Usage is simple, simply pass in a directory as a command-line argument to `/software_metrics/metrics/run_metrics/runner.py --dir <directory>`

This will create a directory called `logs` and will include at the bare minimum a log file which has the calculated software complexity metrics. If the `software_metrics/run_metrics/metrics_cfgs` also includes
the Halstead Complexity metrics, there will also be a JSON file which has the Halstead Complexity metrics broken down for each language desired as well as an aggregate score across all languages. 

Under `software_metrics/metrics/metrics_cfgs` there are three files -
  1) `lang_regexes.json`. This file contains operators, keywords etc. which allow for pattern matching. This makes extending the complexity metrics calculation across languages trivial (even experimental ones) - simply add another key to the JSON file containing the patterns for all syntatic tokens of interest. 
  2) `program_file_exts.txt` - a file containing the extensions that the runner should consider when computing complexity. This can be easily be modified to ignore specific file exts
  3) `program_file_exts_map.json` - this file is a JSON which maps language -> List[allowable extensions]. This is also a key component in making the software complexity calculations extendable to other languages, and can be applied to novel languages as seamlessly as well-established ones.

### Experimental features

The metrics used here are themselves not novel, and fall under the umbrella of static analysis code tools. That said, higher abstraction constructs like relationships between objects, functions, and polymorphic types deserve further exploration. The current version has a file under `/software_metrics/experimental/func_programming_utils.py` which inputs a python file, and does the following
1) Computes number of higher order functions
2) Degree of each higher order function
3) ASCII diagrams showing relationships between the functions in the file
4) In-degree and out-degree using the Network-X Graph Library.

More sophisticated features will be added in future releases, like object dependency injections, as well as code which will automatically perform dependency inversion and Inversion-of-Control (IoC) for classes


### TODO

1) Make the lang_regexes and program_file_exts_map have the same number of languages, not every language is included.
2) Add unit tests for all languages included in the lang_regexes file to ensure the code works as intended.
3) Add helpful visualizations for code complexity
4) Add cyclomatic complexity and a few other metrics not yet included.
5) Flesh out the experimental features
