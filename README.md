# CodeKritik
This repository aims to provide a suite of static analysis tools to analyze code complexity. This is currently mostly a collection of heuristics, but will evolve with time.
Unlike other code metrics related repos at the time of writing, this one computes software complexity by *file* and *language* in addition to an aggregate score across all files & languages. There is support for over 20 languages, including low-level assembly languages like MIPS. Please note this is release 0.0.1, and is *not* suitable for production. Example directories are provided for the reader's viewing pleasure, but will probably go away in a later version. 

## Usage

Usage is simple, simply pass in a directory as a command-line argument to `/software_metrics/metrics/run_metrics/runner.py --dir <directory>`

This creats a directory `logs_<hash>` and under each of those, there is a directory for each metric, further broken down by file and language. The exception to this is the maintainability index which is directly under `logs`. 

Under `software_metrics/metrics/metrics_cfgs` there are many key files -
  1) `lang_regexes.json`. This file contains operators, keywords etc. which allow for pattern matching. This makes extending the complexity metrics calculation across languages trivial (even experimental ones) - simply add another key to the JSON file containing the patterns for all syntatic tokens of interest. 
  2) `program_file_exts.txt` - a file containing the extensions that the runner should consider when computing complexity. This can be easily be modified to ignore specific file exts. NOTE - BEHAVIOR OF THIS IS NOT YET TESTED! 
  3) `program_file_exts_map.json` - this file is a JSON which maps language -> List[allowable extensions]. This is also a key component in making the software complexity calculations extendable to other languages, and can be applied to novel languages as seamlessly as well-established ones.
  4) `generate_hll_tokens.py` - this file is responsible for auto-generating a JSON file which contains the assignments, branches, conditional, loop keywords, and comments which are used to calculate metrics. This allows the computations to be language agnostic and simply operate over syntactic tokens of interest. This file is for high-level languages like Python, Go, C++ etc. The generated file will be called `hll_tokens.json`. 
  5) `generate_lll_tokens.py` - similarly, this file is responsible for auto-generating a JSON file which contains assignments, branches, conditionals, loop keywords and comments for *low-level* languages. This python program actually generates two files, one for LLVM and one for assembly languages. The files are `asm_tokens.json` and `llvm_tokens.json`. **NOTE - Additional Intermediate Representations besided LLVM will be added in the future**. When this occurs, there will be a `generate_hll_tokens.py` file, a `generate_lll_tokens.py` file (which will then only generated Assembly language tokens) and a `generate_ir_tokens.py` which will dump to a file called `ir_tokens.json` which will repace the `llvm_tokens.json` in future releases. 


### Current Metrics

1) ABC Metrics
2) Halstead Complexity
3) Cyclomatic Complexity - this also includes a crude ASCII Control-Flow Graph (CFG) of a given program 
4) LOC (broken down into source, comment, and blank lines of code)
5) Maintainability index
### Experimental features

The metrics used here are themselves not novel, and fall under the umbrella of static analysis code tools. That said, higher abstraction constructs like relationships between objects, functions, and polymorphic types deserve further exploration. The current version has a file under `/software_metrics/experimental/func_programming_utils.py` which inputs a python file, and does the following
1) Computes number of higher order functions
2) Degree of each higher order function
3) ASCII diagrams showing relationships between the functions in the file
4) In-degree and out-degree using the Network-X Graph Library.

More sophisticated features will be added in future releases, like object dependency injections, as well as code which will automatically perform dependency inversion and Inversion-of-Control (IoC) for classes

**KNOWN ISSUES** : 

1) Meta-referencing tokens - In a given language (ex. Python), if comments contain syntatic keywords for loops, assignments, branches etc. the counter(s) will include those inside the calculation. This is also true if the *exact* match of the keyword is a string (but not substring). An example - `my_list = ['something','if']` will count the `if` as an additional branch. Fortunately, this does not occur when `my_list = ['something','if_in_a_string']`. 
In general, this can be easily fixed with better regex/pattern matching to filter out comments and then only pattern match over source. Code already exists to parse source from comments, but the logic for filtering out the syntatic keywords is not yet in the repository.

### TODO
2) Improper handling of all file types - in particular, binary file exceptions are not fully handled, but will be fixed shortly.

1) Proper unit tests for all metrics across all languages
2) Additional Documentation
3) Dockerization
4) Development of more informative metrics which intelligently aggregate and built on the existing ones 
