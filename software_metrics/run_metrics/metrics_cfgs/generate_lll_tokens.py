import json

# LLVM IR
LLVM_ASSIGNMENTS = ["alloca", "store", "load", "phi"]
LLVM_BRANCHES = ["br", "switch", "indirectbr"]
LLVM_CONDITIONALS = ["icmp", "fcmp"]
LLVM_LOOPS = ["br", "indirectbr"]
LLVM_COMMENTS = [';']

# x86 Assembly
X86_ASSIGNMENTS = ["mov", "movzx", "movsx", "lea", "push", "pop"]
X86_BRANCHES = ["jmp", "je", "jne", "jg", "jge", "jl", "jle", "ja", "jae", "jb", "jbe", "call", "ret"]
X86_CONDITIONALS = ["cmp", "test"]
X86_LOOPS = ["loop", "loopz", "loope", "loopnz", "loopne"]
X86_COMMENTS = [';']

# ARM Assembly
ARM_ASSIGNMENTS = ["mov", "ldr", "str", "push", "pop"]
ARM_BRANCHES = ["b", "bl", "bx", "beq", "bne", "bgt", "bge", "blt", "ble", "bhi", "bls"]
ARM_CONDITIONALS = ["cmp", "tst"]
ARM_LOOPS = ["b", "bl", "bx"]  # ARM uses branch instructions for loops
ARM_COMMENTS = [';']

# RISC-V Assembly
RISCV_ASSIGNMENTS = ["li", "mv", "la", "lw", "sw"]
RISCV_BRANCHES = ["j", "jal", "jalr", "beq", "bne", "bge", "blt", "bltu", "bgeu"]
RISCV_CONDITIONALS = ["slti", "sltiu", "slt", "slu", "sltu"]
RISCV_LOOPS = ["j", "jal"]  # RISC-V uses jump instructions for loops
RISCV_COMMENTS = [';']

# MIPS Assembly
MIPS_ASSIGNMENTS = ["li", "move", "la", "lw", "sw"]
MIPS_BRANCHES = ["j", "jal", "jr", "beq", "bne", "bgtz", "blez", "bltz", "bgez"]
MIPS_CONDITIONALS = ["slt", "slti", "sltu", "sltiu"]
MIPS_LOOPS = ["j", "jal"]  # MIPS uses jump instructions for loops
MIPS_COMMENTS = ['#']

# PowerPC Assembly
POWERPC_ASSIGNMENTS = ["li", "mr", "la", "lwz", "stw", "stwu", "addi", "addis"]
POWERPC_BRANCHES = ["b", "bl", "blr", "bc", "bclr", "bne", "beq", "bge", "blt"]
POWERPC_CONDITIONALS = ["cmp", "cmpi", "cmpl", "cmpli"]
POWERPC_LOOPS = ["b", "bl"]  # PowerPC uses branch instructions for loops
POWERPC_COMMENTS = ['#']

# SPARC Assembly
SPARC_ASSIGNMENTS = ["mov", "set", "ld", "st", "add", "sub", "and", "or", "xor"]
SPARC_BRANCHES = ["ba", "b", "bl", "be", "bne", "bg", "ble", "bge", "blt"]
SPARC_CONDITIONALS = ["cmp", "tst"]
SPARC_LOOPS = ["ba", "b", "bl"]  # SPARC uses branch instructions for loops
SPARC_COMMENTS = ['!']

# Z80 Assembly
Z80_ASSIGNMENTS = ["ld", "ldd", "ldi", "ldir", "lddr", "push", "pop"]
Z80_BRANCHES = ["jp", "jr", "call", "ret", "retn", "reti"]
Z80_CONDITIONALS = ["cp", "and", "or", "xor", "sub", "dec", "inc"]
Z80_LOOPS = ["djnz", "jp", "jr", "call"]  # Z80 uses conditional jumps for loops
Z80_COMMENTS = [';']

# Create LLVM dictionary
llvm_dict = {
    "LLVM": {
        "assignments": LLVM_ASSIGNMENTS,
        "branches": LLVM_BRANCHES,
        "conditionals": LLVM_CONDITIONALS,
        "loops": LLVM_LOOPS,
        "comments": LLVM_COMMENTS
    }
}

# Create assembly languages dictionary
asm_dict = {
    "x86": {
        "assignments": X86_ASSIGNMENTS,
        "branches": X86_BRANCHES,
        "conditionals": X86_CONDITIONALS,
        "loops": X86_LOOPS,
        "comments": X86_COMMENTS
    },
    "ARM": {
        "assignments": ARM_ASSIGNMENTS,
        "branches": ARM_BRANCHES,
        "conditionals": ARM_CONDITIONALS,
        "loops": ARM_LOOPS,
        "comments": ARM_COMMENTS
    },
    "RISC-V": {
        "assignments": RISCV_ASSIGNMENTS,
        "branches": RISCV_BRANCHES,
        "conditionals": RISCV_CONDITIONALS,
        "loops": RISCV_LOOPS,
        "comments": RISCV_COMMENTS
    },
    "MIPS": {
        "assignments": MIPS_ASSIGNMENTS,
        "branches": MIPS_BRANCHES,
        "conditionals": MIPS_CONDITIONALS,
        "loops": MIPS_LOOPS,
        "comments": MIPS_COMMENTS
    },
    "PowerPC": {
        "assignments": POWERPC_ASSIGNMENTS,
        "branches": POWERPC_BRANCHES,
        "conditionals": POWERPC_CONDITIONALS,
        "loops": POWERPC_LOOPS,
        "comments": POWERPC_COMMENTS
    },
    "SPARC": {
        "assignments": SPARC_ASSIGNMENTS,
        "branches": SPARC_BRANCHES,
        "conditionals": SPARC_CONDITIONALS,
        "loops": SPARC_LOOPS,
        "comments": SPARC_COMMENTS,
    },
    "Z80": {
        "assignments": Z80_ASSIGNMENTS,
        "branches": Z80_BRANCHES,
        "conditionals": Z80_CONDITIONALS,
        "loops": Z80_LOOPS,
        "comments": Z80_COMMENTS,
    }
}

# Write LLVM dictionary to a file
with open('llvm_tokens.json', 'w') as llvm_file:
    json.dump(llvm_dict, llvm_file, indent=4)

# Write assembly languages dictionary to a file
with open('asm_tokens.json', 'w') as asm_file:
    json.dump(asm_dict, asm_file, indent=4)

print("LLVM and assembly instructions JSON files have been generated.")

