# CodeKritik


## Version 0.2.1

As of 11/15/2025, this project aims to provide a comprehensive suite of software analysis tools that will exceed that of [Sonarqube](https://www.sonarsource.com/products/sonarqube/) and be easy to integrate into LLM/AI agent workflows. **This project's goals are evolving somewhat along with the version number. Every effort will be made to provide as much documentation as time permits on current functionality, known bugs, and future plans.**

The software analysis is broken down into three primary stages, with each stage building on the preceeding one: 

1) **Static Analysis** - This suite of tools uses common known code complexity metrics/heuristics like ABC score, cyclomatic complexity, and others for **arbitrary** programming languages with little to no configuration. In addition to the well-known measures, there will be experimental features to measure how well code adheres to functional programming (FP) and Object-Oriented Programming (OOP) principles. These features are useful because they can be combined with code linters to perform dependency inversion in the case of OOP, and monad construction in the case of FP. These additional features will be an optional flag that will not run by default. Code linters to actually transform code may or may not be within the scope of this project and will be revisited at a later time. 

2) **Git history analysis** - This provides tools for analyzing git branches and git hashes for arbitrary commits. This works by pointing to a repo accessible via URL. 

This works by running the static analysis tools on specified, allowing users to chart out the complexity of a software over time (charts will be provided on a subsequent release). In addition to calculating code complexiy for any git project at any point in its history, additional metrics analyzing project contributor stats are also provided. Metrics like code churn, average length of time for a MR, and longest time between commits are tracked for *every* user as well as globally. End users of Codekritik will then be provided with aggregate information giving them deep insights into current and future maintability of a project from a code standpoint and a maintainer standpoint. 

3) **MCP Integration** - There will be supported added to make the execution CodeKritik's core functionality an agentic tool which can be incorporated into various workflows. One example can be providing alerts as to when refactors of code are likely needed rather than adding more features in an effort to minimize technical debt. 


### Overview 

Unlike other code metrics related repos at the time of writing, this one computes software complexity by *file* and *language* in addition to a global aggregate score across all files & languages in a given codebase. There is support for over 20 languages, including experimental support for low-level assembly languages like MIPS, ARM and PowerPC. **Please note this is release 0.2.0 and is *not* recommended for production (yet)**


| Level       | Languages                     |
|-------------|---------------------------------- |
| High-level  | 1. Python <br> 2. Julia <br> 3. Go <br> 4. Java <br> 5. JavaScript <br> 6. TypeScript <br> 7. C <br> 8. C++ <br> 9. C# <br> 10. Objective-C <br> 11. Haskell <br> 12. Rust <br> 13. BASH <br> 14. COBOL <br> 15. FORTRAN <br> 16. R <br> 17. PHP <br> 18. Clojure <br> 19. Lisp <br> 20. Scala <br>|
| IR          | 1. LLVM <br> 2. Gimple (not fully tested) <br>  |
| Low-level   | 1. x86 <br> 2. ARM <br> 3. MIPS <br> 4. PowerPC <br> 5. RISC-V <br> 6. SPARC <br> 7. Z80 <br> |

## Usage

Usage is simple, simply pass in a directory as a command-line argument to `python3 static_analyzer.py --dir <directory>` when running on a local directory.


When evaluating across git history, execute

`python3 git_history_analysis.py --repo_url <git_url> --since MM-DD-YYYY --until MM-DD-YYYY --branch <branch of choice>`. 

Under the hood, this calls the `static_analyzer.py` file on the checked out code for all commits within the specified date range on the given branch. The repo is cloned and the HEAD is shifted across commits. 

**KNOWN BUGS**:  There is a known bug where this code will fail if the target branch/repository does not contain *any* of the 20 languages. Additionally, there are some parsing issues with low-level languages and the distinction between the high, IR, and low-level will likely be removed for simplicity. 

A directory of the form `logs_<hash>` is created when running `static_analyzer.py`

Under each of these, there is a directory for each metric, broken down at three levels of granularity - file, language, and global. The exception to this is the maintainability index which is directly under `logs`. When running across history, the directory structure becomes

`/repo_stats/<branch>/<date>/<commit_hash>/logs_<hash>/...`

Under `metrics_cfgs` there are several key files -
  1) `lang_regexes.json`. This file contains operators, keywords etc. which allow for pattern matching. This makes extending the complexity metrics calculation across languages trivial (even experimental ones) - simply add another key to the JSON file containing the patterns for all syntatic tokens of interest. 
  2) `program_file_exts.txt` - a file containing the extensions that the runner should consider when computing complexity. This can be easily be modified to ignore specific file exts. 
  3) `program_file_exts_map.json` - this file is a JSON which maps language -> List[allowable extensions]. This is also a key component in making the software complexity calculations extendable to other languages, and can be applied to novel languages as seamlessly as well-established ones.
  4) `generate_hll_tokens.py` - this file is responsible for auto-generating a JSON file which contains the assignments, branches, conditional, loop keywords, and comments which are used to calculate metrics. This allows the computations to be language agnostic and simply operate over syntactic tokens of interest. This file is for high-level languages like Python, Go, C++ etc. The generated file will be called `hll_tokens.json`. 
  5) `generate_lll_tokens.py` - similarly, this file is responsible for auto-generating a JSON file which contains the assignments, branches, conditional and loop keywords along with comment tokens for assembly-level languages like x86 and ARM. 
  6) `generate_ir_tokens.py` - like above, but for middle-end Intermediate Representation (IR) languages like LLVM and Gimble.

  **Once again, note that the LLL and IR tokens will be likely rolled into the HLL tokens**


### Current Metrics

1) ABC Metrics
2) Halstead Complexity
3) Cyclomatic Complexity - this also includes a crude ASCII Control-Flow Graph (CFG) of a given program 
4) LOC (broken down into source, comment, and blank lines of code)
5) Maintainability index (MI)
   
### Experimental features

The metrics used here are themselves not novel, and fall under the umbrella of static analysis code tools. That said, higher abstraction constructs like relationships between objects, functions, and polymorphic types deserve further exploration. These will be found under `software_metrics/metrics/experimental`

More sophisticated features will be added in future releases, like object dependency injections, as well as code which will automatically perform dependency inversion and Inversion-of-Control (IoC) for classes. 

### Interpretation of Metrics

Despite software metrics being quantifiable and determinsitic, interpretation of the results is non-trivial. As a quick example, MI heavily relies on LOC, which artificially reduces the score for more verbose (usually strongly typed) languages even when the algorithm(s) implemented is/are identical. 

Despite known limitations, software metrics provide a way to analyze code objectively and aids in understanding how complex a codebase is, which in turn tells developers and managers the expected cost of refactoring, maintenance, learning curves for new developers etc. Additionally, since all metrics are broken down by file and language, this provides a more granular understanding of the codebase, allowing developers to focus on certain portions more than others. 

### Use Cases

1) **Reward function for AI Agents** -> Agents which use some combination of classic RL w/ LLMs can use the software metrics here as a reward function. In this setup, an RL episode may include code generation, and through iterative refinement of some policy function, the agent is rewarded for both correct and less complex code.

2) **GitHub Actions & MR denial/approval** -> When someone submits an MR, it is possible to set up a git diff between the branch of interest and the MR branch and automatically deny an MR if the MR adds too much complexity to the codebase. In conjunction with established best practices, this can significantly improve long term maintainability of large scale projects. A simple GitHub action for CI can be setup to enforce this policy. 

3) **Downstream automated code tooling** -> because CodeKritik provides complexity metrics at the file, language and global level, tools that automatically generate unit tests, code linters, and LLM powered refactoring tools can focus on relevant subsets of the codebase. 

### Roadmap to 0.3.0

1) Proper unit tests for all metrics across all languages
2) Fixing issue with IR and Assembly-level language parsing
3) Add in MCP support

### Roadmap to 0.4.0

1) Dockerization
2) Creation of GitHub CI action

### Roadmap to 1.0.0

1) Unit tests
2) Issues template
3) PR template

## License

Codekritik is now permanently under the MIT license.