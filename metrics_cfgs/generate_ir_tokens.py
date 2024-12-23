import json

# LLVM IR
LLVM_ASSIGNMENTS = ["add",
                    "sub",
                    "mul",
                    "div",
                    "and",
                    "or",
                    "xor",
                    "shl",
                    "lshr",
                    "ashr",
                    "alloca",
                    "store",
                    "load",
                    "gep",
                    "phi",
                    "call"]

LLVM_BRANCHES = ["br","ret","switch","indirectbr"]
LLVM_CONDITIONALS = ["icmp","fcmp","select","br","switch"]
LLVM_LOOPS = []
LLVM_COMMENTS = ["metadata","dbg","llvm.dbg.declare","llvm.dbg.value"]

# GIMPLE IR
GIMPLE_ASSIGNMENTS = ["=", "+=", "-=", "*=", "/=", "%=", "|=", "&=", "^=", "<<=", ">>="]
GIMPLE_BRANCHES = ["goto","return","label"]
GIMPLE_CONDITIONALS = ["<", "<=", ">", ">=", "==", "!=", "&&", "||", "!"]
GIMPLE_LOOPS = ["goto","label","if"]
GIMPLE_COMMENTS = []

ir_dict = {"LLVM": {"assignments": LLVM_ASSIGNMENTS,
                      "branches": LLVM_BRANCHES,
                      "conditionals": LLVM_CONDITIONALS,
                      "loops": LLVM_LOOPS,
                      "comments": LLVM_COMMENTS},
           "GIMPLE": {"asignments": GIMPLE_ASSIGNMENTS,
                      "branches": GIMPLE_BRANCHES,
                      "conditionals": GIMPLE_CONDITIONALS,
                      "loops": GIMPLE_LOOPS,
                      "comments": GIMPLE_COMMENTS}
             }
with open("ir_tokens.json","w") as ir_file:
    json.dump(ir_dict, ir_file, indent = 4)
print('IR token JSON file has been generated.')
