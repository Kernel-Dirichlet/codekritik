# CodeKritik


## Version 0.2.0

As of 10/25/2024, this project aims to provide a comprehensive suite of software analysis tools that will exceed that of [Sonarqube](https://www.sonarsource.com/products/sonarqube/) and be easy to integrate into LLM/AI agent workflows. **This project's goals are evolving somewhat along with the version number. Every effort will be made to provide as much documentation as time permits on current functionality, known bugs, and future plans.**

The software analysis is broken down into three primary stages, with each stage building on the preceeding one: 

1) **Static Analysis** - This suite of tools uses common known code complexity metrics/heuristics like ABC score, cyclomatic complexity, and others for **arbitrary** programming languages with little to no configuration. In addition to the well-known measures, there will be experimental features to measure how well code adheres to functional programming (FP) and Object-Oriented Programming (OOP) principles. These features are useful because they can be combined with code linters to perform dependency inversion in the case of OOP, and monad construction in the case of FP. These additional features will be an optional flag that will not run by default. Code linters to actually transform code may or may not be within the scope of this project and will be revisited at a later time. 

2) **Git history analysis** - This provides tools for analyzing git branches and git hashes for arbitrary commits. This works by either pointing to a github accessible via URL or a git repository accessible from a local host. This works by running the static analysis tools on specified git branches and/or commits, allowing users to chart out the complexity of a software over time. In addition to calculating code complexiy for any git project at any point in its history, additional metrics analyzing project contributor stats are also provided. Metrics like code churn, average length of time for a MR, and longest time between commits are tracked for *every* user as well as globally. End users of Codekritik will then be provided with aggregate information giving them deep insights into current and future maintability of a project from a code standpoint and a maintainer standpoint. 

3) **ML analysis** - The purpose of ML in this project is to compute a "Temporal Maintainability Metric" (TMI) which will be a project's maintainability over time. This metric is meant to inform how attractive a code base is as a dependency in other projects, ease of use etc. Unlike the well known code complexity metrics found in the static analysis tools, TMI aims to be a data-driven metric rather than a manual collection of heuristics. A neural network will compute TMI as a non-linear mapping of static code heuristics to TMI. The model itself can be serialized and can be run as a linux service or cronjob in the deployment stage for inference.


### Dynamic Analysis?? ###

There may be tools to create virtualized environments and trace out a program execution. If this is to be undertaken, it will also provide Big-O run-time of algorithms it can detect, and perhaps refactor that code in simple enough cases. If this is done, it will be in Codekritik v2.0.0 or greater. 


### Overview 

Unlike other code metrics related repos at the time of writing, this one computes software complexity by *file* and *language* in addition to a global aggregate score across all files & languages in a given codebase. There is support for over 20 languages, including low-level assembly languages like MIPS, ARM and PowerPC. **Please note this is release 0.2.0 and is *not* recommended for production (yet)**

CodeKritik provides some support for running metrics on arbitrary Git repositories via URL and locally. The idea is the complexity metrics are computed across *every* hash within a specified date range, *and will soon provide a breakdown of git stats by users*. Refer to documentation below. 

| Level       | Languages                     |
|-------------|---------------------------------- |
| High-level  | 1. Python <br> 2. Julia <br> 3. Go <br> 4. Java <br> 5. JavaScript <br> 6. TypeScript <br> 7. C <br> 8. C++ <br> 9. C# <br> 10. Objective-C <br> 11. Haskell <br> 12. Rust <br> 13. BASH <br> 14. COBOL <br> 15. FORTRAN <br> 16. R <br> 17. PHP <br> 18. Clojure <br> 19. Lisp <br> 20. Scala <br>|
| IR          | 1. LLVM <br> 2. Gimple (not fully tested) <br>  |
| Low-level   | 1. x86 <br> 2. ARM <br> 3. MIPS <br> 4. PowerPC <br> 5. RISC-V <br> 6. SPARC <br> 7. Z80 <br> |

## Usage

Usage is simple, simply pass in a directory as a command-line argument to `python3 static_analyzer.py --dir <directory>` when running on a local directory.


When evaluating across git history, execute

`python3 git_history_analysis.py --repo_url <git_url> --since MM-DD-YYYY --until MM-DD-YYYY --branch <branch of choice>`. 

Under the hood, this calls the `static_analyzer.py` file on the checked out code for all commits within the specified date range on the given branch. 

**KNOWN BUGS**:  There is a known bug where this code will fail if the target branch/repository does not contain *any* of the 20 languages. Specifically, if none of the file extensions match to a language, the code fails. There is also a division-by-zero error which sometimes occurs. These issues will be both be fixed by version 0.2.2. These bugs are not the most exhaustive, but are by far the most common. A detailed bugs section will be added to the README in a future release. 

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


### Current Metrics

1) ABC Metrics
2) Halstead Complexity
3) Cyclomatic Complexity - this also includes a crude ASCII Control-Flow Graph (CFG) of a given program 
4) LOC (broken down into source, comment, and blank lines of code)
5) Maintainability index (MI)
   
### Experimental features

The metrics used here are themselves not novel, and fall under the umbrella of static analysis code tools. That said, higher abstraction constructs like relationships between objects, functions, and polymorphic types deserve further exploration. These will be found under `software_metrics/metrics/experimental`

More sophisticated features will be added in future releases, like object dependency injections, as well as code which will automatically perform dependency inversion and Inversion-of-Control (IoC) for classes

### Interpretation of Metrics

Despite software metrics being quantifiable and determinsitic, interpretation of the results is non-trivial. As a quick example, MI heavily relies on LOC, which artificially reduces the score for more verbose (usually strongly typed) languages even when the algorithm(s) implemented is/are identical. 

Despite known limitations, software metrics provide a way to analyze code objectively and serve as some basis for understanding how complex a code base is, which in turn tells developers and managers the expected cost of refactoring, maintenance, learning curves for new developers etc. Additionally, since all metrics are broken down by file and language, this provides a more granular understanding of the codebase, allowing developers to focus on certain portions more than others. 

### Use Cases

1) **Reward function for AI Agents** -> Agents which use some combination of classic RL w/ LLMs can use the software metrics here as a reward function. In this setup, an RL episode may include code generation, and through iterative refinement of some policy function, the agent is rewarded for both correct and less complex code.

2) **GitHub Actions & MR denial/approval** -> When someone submits an MR, it is possible to set up a git diff between the branch of interest and the MR branch and automatically deny an MR if the MR adds too much complexity to the codebase. In conjunction with established best practices, this can significantly improve long term maintainability of large scale projects. A simple GitHub action for CI can be setup to enforce this policy 
3) **Downstream automated code tooling** -> because CodeKritik provides complexity metrics at the file, language and global level, tools that automatically generate unit tests, code linters, and LLM powered refactoring tools can focus on relevant subsets of the codebase. 

### Roadmap to 0.3.0

1) Proper unit tests for all metrics across all languages
2) When computing metrics for IR, ensure Gimble, not just LLVM is supported
3) Create GitHub action so this code can be run as part of CI
4) Include user Git metrics like code churn
5) Dockerization

 
## License

This software is available under a **dual-license** model:

1. **GNU Affero General Public License (AGPL) v3**:
   - This software is open-source and licensed under the AGPL v3.
   - You are free to use, modify, and distribute the software in open-source and non-commercial projects, provided that any modifications are also distributed under the AGPL license and made available to the public.

   For more details, see the [LICENSE](./LICENSE) file.

2. **Commercial License**:
   - If you intend to use this software in a **commercial application** or as part of a proprietary product, you must obtain a commercial license.
   - The commercial license allows you to use the software without the obligation to release your modifications under the AGPL.

   To inquire about commercial licensing, please contact:

   - **Email**: elliottdev93@gmail.com
   - **Website**: TBD

By using this software for commercial purposes without a commercial license, you are in violation of the terms of this repository.
