# CodeKritik
## Version 1.0.0
This repository aims to provide a suite of static analysis tools to analyze code complexity. This is currently a collection of known heuristics, but will evolve with time to include aggregate metrics which take into account lower level metrics. 

Unlike other code metrics related repos at the time of writing, this one computes software complexity by *file* and *language* in addition to a global aggregate score across all files & languages in a given codebase. There is support for over 20 languages, including low-level assembly languages like MIPS, ARM and PowerPC. Please note this is release 1.0.0 and is *not* recommended for production (yet). 

| Level       | Languages                     |
|-------------|---------------------------------- |
| High-level  | 1. Python <br> 2. Julia <br> 3. Go <br> 4. Java <br> 5. JavaScript <br> 6. TypeScript <br> 7. C <br> 8. C++ <br> 9. C# <br> 10. Objective-C <br> 11. Haskell <br> 12. Rust <br> 13. BASH <br> 14. COBOL <br> 15. FORTRAN <br> 16. R <br> 17. PHP <br> 18. Clojure <br> 19. Lisp <br> 20. Scala <br>|
| IR          | 1. LLVM <br> 2. Gimple (not fully tested) <br>  |
| Low-level   | 1. x86 <br> 2. ARM <br> 3. MIPS <br> 4. PowerPC <br> 5. RISC-V <br> 6. SPARC <br> 7. Z80 <br> |

## Usage

Usage is simple, simply pass in a directory as a command-line argument to `runner.py --dir <directory>`

This creats a directory `logs_<hash>` and under each of those, there is a directory for each metric, further broken down by file and language. The exception to this is the maintainability index which is directly under `logs`. 

Under `metrics_cfgs` there are several key files -
  1) `lang_regexes.json`. This file contains operators, keywords etc. which allow for pattern matching. This makes extending the complexity metrics calculation across languages trivial (even experimental ones) - simply add another key to the JSON file containing the patterns for all syntatic tokens of interest. 
  2) `program_file_exts.txt` - a file containing the extensions that the runner should consider when computing complexity. This can be easily be modified to ignore specific file exts. 
  3) `program_file_exts_map.json` - this file is a JSON which maps language -> List[allowable extensions]. This is also a key component in making the software complexity calculations extendable to other languages, and can be applied to novel languages as seamlessly as well-established ones.
  4) `generate_hll_tokens.py` - this file is responsible for auto-generating a JSON file which contains the assignments, branches, conditional, loop keywords, and comments which are used to calculate metrics. This allows the computations to be language agnostic and simply operate over syntactic tokens of interest. This file is for high-level languages like Python, Go, C++ etc. The generated file will be called `hll_tokens.json`. 
  5) `generate_lll_tokens.py` - similarly, this file is responsible for auto-generating a JSON file which contains the assignments, branches, conditional and loop keywords along with comment tokens for assembly-level languages like x86 and ARM.
  6) `generate_ir_tokens.py` - like above, but for middle-end Intermediate Representation (IR) languages like LLVM and Gimble.


### Current Metrics

1) ABC Metrics
2) Halstead Complexity
3) Cyclomatic Complexity - this also includes a crude ASCII Control-Flow Graph (CFG) of a given program 
4) LOC (broken down into source, comment, and blank lines of code)
5) Maintainability index (MI)
   
### Experimental features

The metrics used here are themselves not novel, and fall under the umbrella of static analysis code tools. That said, higher abstraction constructs like relationships between objects, functions, and polymorphic types deserve further exploration. The current version has a file under `/software_metrics/experimental/func_programming_utils.py` which inputs a python file, and does the following
1) Computes number of higher order functions
2) Degree of each higher order function
3) ASCII diagrams showing relationships between the functions in the file
4) In-degree and out-degree using the Network-X Graph Library.

More sophisticated features will be added in future releases, like object dependency injections, as well as code which will automatically perform dependency inversion and Inversion-of-Control (IoC) for classes

### Interpretation of Metrics

Despite software metrics being quantifiable and determinsitic, interpretation of the results is non-trivial. As a quick example, MI heavily relies on LOC, which artificially reduces the score for more verbose (usually strongly typed) languages even when the algorithm(s) implemented is/are identical. 

Despite known limitations, software metrics provide a way to analyze code objectively and serve as some basis for understanding how complex a code base is, which in turn tells developers and managers the expected cost of refactoring, maintenance, learning curves for new developers etc. Additionally, since all metrics are broken down by file and language, this provides a more granular understanding of the codebase, allowing developers to focus on certain portions more than others. 

### Use Cases

1) **Reward function for AI Agents** -> Agents which use some combination of classic RL w/ LLMs can use the software metrics here as a reward function. In this setup, an RL episode may include code generation, and through iterative refinement of some policy function, the agent is rewarded for both correct and less complex code.

2) **GitHub Actions & MR denial/approval** -> When someone submits an MR, it is possible to set up a git diff between the branch of interest and the MR branch and automatically deny an MR if the MR adds too much complexity to the codebase. In conjunction with established best practices, this can significantly improve long term maintainability of large scale projects. A simple GitHub action for CI can be setup to enforce this policy 
3) **Downstream automated code tooling** -> because CodeKritik provides complexity metrics at the file, language and global level, tools that automatically generate unit tests, code linters, and LLM powered refactoring tools can focus on relevant subsets of the codebase. 

### Roadmap to 1.1.0

1) Proper unit tests for all metrics across all languages
2) When computing metrics for IR, ensure Gimble, not just LLVM is supported
3) Create GitHub action so this code can be run as part of CI
4) Include Git repository metrics like churn 
5) Additional Documentation
6) Dockerization
7) Development of more informative metrics which intelligently aggregate and built on the existing ones 
