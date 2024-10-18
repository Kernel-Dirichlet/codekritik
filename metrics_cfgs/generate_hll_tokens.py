import json


# ===================================================================================================

PYTHON_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "//=", "**=", "&=", "|=", "^=", ">>=", "<<="]
PYTHON_BRANCHES = ["if", "elif", "else"]
PYTHON_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "and", "or", "not"]
PYTHON_LOOPS = ["for","while"]
PYTHON_COMMENTS = ['#','"""',"'''"]

# ===================================================================================================

JULIA_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "//=", "^=", "%=", "&=", "|=", "$=", "<<=", ">>="]
JULIA_BRANCHES = ["if", "elseif", "else"]
JULIA_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&&", "||", "!"]
JULIA_LOOPS = ["for","while"]
JULIA_COMMENTS = ['#','#=','=#']

# ===================================================================================================

RUST_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="]
RUST_BRANCHES = ["if", "else if", "else", "match"]
RUST_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&&", "||", "!"]
RUST_LOOPS = ["for","while","loop"]
RUST_COMMENTS = ['//','/*','*/']

# ===================================================================================================

BASH_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", ">>=", "<<="]
BASH_BRANCHES = ["if", "elif", "else", "case", "select"]
BASH_CONDITIONALS = ["-eq", "-ne", "-lt", "-le", "-gt", "-ge", "&&", "||", "!"]
BASH_LOOPS = ["for","while","until"]
BASH_COMMENTS = ['#',': \'','\'','<<\'EOF\'','EOF']

# ===================================================================================================

C_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="]
C_BRANCHES = ["if", "else if", "else", "switch", "case", "default"]
C_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&&", "||", "!"]
C_LOOPS = ["for","while","do"]
C_COMMENTS = ['//','/*','*/']

# ===================================================================================================

CPP_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="]
CPP_BRANCHES = ["if", "else if", "else", "switch", "case", "default"]
CPP_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&&", "||", "!"]
CPP_LOOPS = ["for","while","do"]
CPP_COMMENTS = ['//','/*','*/']

# ===================================================================================================

CSHARP_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="]
CSHARP_BRANCHES = ["if", "else if", "else", "switch", "case", "default"]
CSHARP_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&&", "||", "!"]
CSHARP_LOOPS = ["for","while","do","foreach"]
CSHARP_COMMENTS = ['//','/*','*/']

# ===================================================================================================

OBJC_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="]
OBJC_BRANCHES = ["if", "else if", "else", "switch", "case", "default"]
OBJC_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&&", "||", "!"]
OBJC_LOOPS = ["for","while","do"]
OBJC_COMMENTS = ['//','/*','*/']

# ===================================================================================================

JAVA_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="]
JAVA_BRANCHES = ["if", "else if", "else", "switch", "case", "default"]
JAVA_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&&", "||", "!"]
JAVA_LOOPS = ["for","while","do"]
JAVA_COMMENTS = ['//','/*','*/']

# ===================================================================================================

JAVASCRIPT_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", ">>>="]
JAVASCRIPT_BRANCHES = ["if", "else if", "else", "switch", "case", "default"]
JAVASCRIPT_CONDITIONALS = ["==", "!=", "===", "!==", "<", "<=", ">", ">=", "&&", "||", "!"]
JAVASCRIPT_LOOPS = ["for","while","do","foreach"]
JAVASCRIPT_COMMENTS = ['//','/*','*/']

# ===================================================================================================

TYPESCRIPT_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", ">>>="]
TYPESCRIPT_BRANCHES = ["if", "else if", "else", "switch", "case", "default"]
TYPESCRIPT_CONDITIONALS = ["==", "!=", "===", "!==", "<", "<=", ">", ">=", "&&", "||", "!"]
TYPESCRIPT_LOOPS = ["for","while","do"] 
TYPESCRIPT_COMMENTS = ['//','/*','*/']

# ===================================================================================================

HASKELL_ASSIGNMENTS = ["="]
HASKELL_BRANCHES = ["if", "then", "else", "case", "of"]
HASKELL_CONDITIONALS = ["==", "/=", "<", "<=", ">", ">=", "&&", "||", "not"]
HASKELL_LOOPS = []
HASKELL_COMMENTS = ['--','{-','-}']

# ===================================================================================================
GO_ASSIGNMENTS = ["=", ":=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="]
GO_BRANCHES = ["if", "else if", "else", "switch", "case", "default"]
GO_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&&", "||", "!"]
GO_LOOPS = ["for"]
GO_COMMENTS = ['//','/*','*/']

# ===================================================================================================
FORTRAN_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/="]
FORTRAN_BRANCHES = ["if", "else if", "else", "select case", "case", "default"]
FORTRAN_CONDITIONALS = [".eq.", ".ne.", ".lt.", ".le.", ".gt.", ".ge.", ".and.", ".or.", ".not."]
FORTRAN_LOOPS = ["DO","DO WHILE","FORALL"]
FORTRAN_COMMENTS = ['!']

# ===================================================================================================

COBOL_ASSIGNMENTS = ["MOVE"]
COBOL_BRANCHES = ["IF", "ELSE", "ELSE IF", "EVALUATE", "WHEN", "PERFORM", "END-IF"]
COBOL_CONDITIONALS = ["=", "NOT =", "<", "<=", ">", ">=", "AND", "OR", "NOT"]
COBOL_LOOPS = ["PERFORM","PERFORM UNTIL","PERFORM VARYING"]
COBOL_COMMENTS = ['*','*>']

# ===================================================================================================

R_ASSIGNMENTS = ["<-", "<<-", "=", "->", "->>"]
R_BRANCHES = ["if", "else", "else if", "for", "while", "repeat", "switch"]
R_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&", "&&", "|", "||", "!"]
R_LOOPS = ["for","while","repeat"]
R_COMMENTS = ['#']

# ===================================================================================================

LISP_ASSIGNMENTS = ["setq", "setf", "defparameter", "defvar"]
LISP_BRANCHES = ["if", "cond", "when", "unless", "case", "ecase", "typecase", "etypecase"]
LISP_CONDITIONALS = ["eq", "eql", "equal", "=", "/=", "<", "<=", ">", ">=", "and", "or", "not"]
LISP_LOOPS = ["loop","do","dotimes","dolist"]
LISP_COMMENTS = [';']

# ===================================================================================================

PHP_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", "=>"]
PHP_BRANCHES = ["if", "else", "else if", "elseif", "switch", "case", "default"]
PHP_CONDITIONALS = ["==", "!=", "===", "!==", "<", "<=", ">", ">=", "&&", "||", "!"]
PHP_LOOPS = ["for","while","do","foreach"]
PHP_COMMENTS = ['//','#','/*','*/']

# ===================================================================================================

CLOJURE_ASSIGNMENTS = ["def", "let", "defn", "defmacro", "set!"]
CLOJURE_BRANCHES = ["if", "if-not", "when", "when-not", "cond", "case"]
CLOJURE_CONDITIONALS = ["=", "not=", "<", "<=", ">", ">=", "and", "or", "not"]
CLOJURE_LOOPS = ["loop","for","while","doseq","dotimes","recur"]
CLOJURE_COMMENTS = [';']

# ===================================================================================================

SCALA_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", "var", "val"]
SCALA_BRANCHES = ["if", "else", "else if", "for", "while", "match", "case", "do", "yield"]
SCALA_CONDITIONALS = ["==", "!=", "<", "<=", ">", ">=", "&&", "||", "!"]
SCALA_LOOPS = ["for","while","do"]
SCALA_COMMENTS = ['//','/*','*/']

# ===================================================================================================

hll_instructions = {
    "Python": {
        "assignments": PYTHON_ASSIGNMENTS,
        "branches": PYTHON_BRANCHES,
        "conditionals": PYTHON_CONDITIONALS,
        "loops": PYTHON_LOOPS,
        "comments": PYTHON_COMMENTS,
    },
    "Julia": {
        "assignments": JULIA_ASSIGNMENTS,
        "branches": JULIA_BRANCHES,
        "conditionals": JULIA_CONDITIONALS,
        "loops": JULIA_LOOPS,
        "comments": JULIA_COMMENTS,
    },
    "Rust": {
        "assignments": RUST_ASSIGNMENTS,
        "branches": RUST_BRANCHES,
        "conditionals": RUST_CONDITIONALS,
        "loops": RUST_LOOPS,
        "comments": RUST_COMMENTS,
    },
    "Bash": {
        "assignments": BASH_ASSIGNMENTS,
        "branches": BASH_BRANCHES,
        "conditionals": BASH_CONDITIONALS,
        "loops": BASH_LOOPS,
        "comments": BASH_COMMENTS,
    },
    "C": {
        "assignments": C_ASSIGNMENTS,
        "branches": C_BRANCHES,
        "conditionals": C_CONDITIONALS,
        "loops": C_LOOPS,
        "comments": C_COMMENTS,
    },
    "C++": {
        "assignments": CPP_ASSIGNMENTS,
        "branches": CPP_BRANCHES,
        "conditionals": CPP_CONDITIONALS,
        "loops": CPP_LOOPS,
        "comments": CPP_COMMENTS,
    },
    "C#": {
        "assignments": CSHARP_ASSIGNMENTS,
        "branches": CSHARP_BRANCHES,
        "conditionals": CSHARP_CONDITIONALS,
        "loops": CSHARP_LOOPS,
        "comments": CSHARP_COMMENTS,
    },
    "Objective-C": {
        "assignments": OBJC_ASSIGNMENTS,
        "branches": OBJC_BRANCHES,
        "conditionals": OBJC_CONDITIONALS,
        "loops": OBJC_LOOPS,
        "comments": OBJC_COMMENTS,
    },
    "Java": {
        "assignments": JAVA_ASSIGNMENTS,
        "branches": JAVA_BRANCHES,
        "conditionals": JAVA_CONDITIONALS,
        "loops": JAVA_LOOPS,
        "comments": JAVA_COMMENTS,
    },
    "JavaScript": {
        "assignments": JAVASCRIPT_ASSIGNMENTS,
        "branches": JAVASCRIPT_BRANCHES,
        "conditionals": JAVASCRIPT_CONDITIONALS,
        "loops": JAVASCRIPT_LOOPS,
        "comments": JAVASCRIPT_COMMENTS,
    },
    "TypeScript": {
            "assignments": TYPESCRIPT_ASSIGNMENTS,
            "branches": TYPESCRIPT_BRANCHES,
            "conditionals": TYPESCRIPT_CONDITIONALS,
            "loops": TYPESCRIPT_LOOPS,
            "comments": TYPESCRIPT_COMMENTS,
    },
    "Haskell": {
            "assignments": HASKELL_ASSIGNMENTS,
            "branches": HASKELL_BRANCHES,
            "conditionals": HASKELL_CONDITIONALS,
            "loops": HASKELL_LOOPS,
            "comments": HASKELL_COMMENTS,
    },
    "Go": {
        "assignments": GO_ASSIGNMENTS,
        "branches": GO_BRANCHES,
        "conditionals": GO_CONDITIONALS,
        "loops": GO_LOOPS,
        "comments": GO_COMMENTS,
    },
    "FORTRAN": {
        "assignments": FORTRAN_ASSIGNMENTS,
        "branches": FORTRAN_BRANCHES,
        "conditionals": FORTRAN_CONDITIONALS,
        "loops": FORTRAN_LOOPS,
        "comments": FORTRAN_COMMENTS,
    },
    "COBOL": {
        "assignments": COBOL_ASSIGNMENTS,
        "branches": COBOL_BRANCHES,
        "conditionals": COBOL_CONDITIONALS,
        "loops": COBOL_LOOPS,
        "comments": COBOL_COMMENTS,
    },
    "R": {
        "assignments": R_ASSIGNMENTS,
        "branches": R_BRANCHES,
        "conditionals": R_CONDITIONALS,
        "loops": R_LOOPS,
        "comments": R_COMMENTS,
    },
    "Lisp": {
        "assignments": LISP_ASSIGNMENTS,
        "branches": LISP_BRANCHES,
        "conditionals": LISP_CONDITIONALS,
        "loops": LISP_LOOPS,
        "comments": LISP_COMMENTS,
    },
    "PHP": {
        "assignments": PHP_ASSIGNMENTS,
        "branches": PHP_BRANCHES,
        "conditionals": PHP_CONDITIONALS,
        "loops": PHP_LOOPS,
        "comments": PHP_COMMENTS,
    },
    "Clojure": {
        "assignments": CLOJURE_ASSIGNMENTS,
        "branches": CLOJURE_BRANCHES,
        "conditionals": CLOJURE_CONDITIONALS,
        "loops": CLOJURE_LOOPS,
        "comments": CLOJURE_COMMENTS,
    },
    "Scala": {
        "assignments": SCALA_ASSIGNMENTS,
        "branches": SCALA_BRANCHES,
        "conditionals": SCALA_CONDITIONALS,
        "loops": SCALA_LOOPS,
        "comments": SCALA_COMMENTS,
    },

}

# Write the HLL instructions to a JSON file
with open('hll_tokens.json', 'w') as hll_file:
    json.dump(hll_instructions, hll_file, indent=4)

print("HLL JSON file has been generated.")

