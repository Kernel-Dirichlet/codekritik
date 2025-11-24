import json

# x86 Assembly
X86_ASSIGNMENTS = ['mov','lea','push','pop','add','sub','xchg','mul',
                    'imul','div','idiv','xor','and','or','shl','sal',
                    'shr','sar','movzx','movsx','inc','dec','neg','not']

X86_BRANCHES = ['jmp','call','ret','jo','jno','js','jns','je','jne','jz',
                    'jnz','jg','jge','jl','jle','ja','jae','jb','jbe','jc',
                    'jnc','jp','jnp']

X86_CONDITIONALS = ['cmp','test','cmove','cmovne','cmovg','cmovge','cmovl',
                       'cmovle','cmova','cmovae','cmovb','cmovbe','sete','setne',
                       'setg','setge','setl','setle','seta','setae','setb','setbe',
                       'seto','setno','sets','setns','setp','setnp']

X86_LOOPS = ['loop', 'jcxz', 'jcxnz','jecxz','jecxnz']
X86_COMMENTS = [';','#']


# ARM Assembly
ARM_ASSIGNMENTS = ['MOV','MVN','ADD','ADC','SUB','SBC','MUL',
                       'MLA','SDIV','UDIV','AND','ORR','EOR','LSL',
                       'LSR','ASR','ROR','RRX']

ARM_BRANCHES = ['B','BL','BX','BEQ','BNE','BGT','BGE',
                    'BLT','BLE','BHI','BHS','BCS','BLO',
                     'BCC','BMI','BPL']

ARM_CONDITIONALS = ['CMP', 'TST','CMN', 'TEQ']
ARM_LOOPS = []
ARM_COMMENTS = [';','@']


# RISC-V Assembly
RISCV_ASSIGNMENTS = ['ADD','SUB','MUL','MULH','MULHU','MULHSU','DIV','DIVU','REM',
                         'REMU','AND','OR','XOR','SLL','SRL','SRA','LUI','AUIPC','LW',
                          'SW']

RISCV_BRANCHES = ['JAL', 'JALR', 'BEQ', 'BNE', 'BLT', 'BGE', 'BLTU', 'BGEU']
RISCV_CONDITIONALS = ['SLT', 'SLTU','SLTI','SLTIU']
RISCV_LOOPS = []
RISCV_COMMENTS = ['#', '//', '/*', '*/']


# MIPS Assembly
MIPS_ASSIGNMENTS = ['add','addu','sub','subu','mult','multu','div','divu','and','andi',
                    'or','ori','xor','xori','nor','sll','sllv','srl','srlv','sra','srav']

MIPS_BRANCHES = ['j','jal','jr','beq','bne','bgtz','bgez','bltz','blez']
MIPS_CONDITIONALS = ['slt', 'sltu','slti','sltiu']
MIPS_LOOPS = []
MIPS_COMMENTS = ['#']

# PowerPC Assembly
POWERPC_ASSIGNMENTS = ['lwz','stw','addi','add','subf','mullw','mulhw','divw','divwu',
                           'and','andi','or','ori','xor','xori','nor','slw','srw','sraw']

POWERPC_BRANCHES = ['b', 'beq', 'bne', 'bgt', 'bge', 'blt', 'ble', 'bl', 'blr','bc']
POWERPC_CONDITIONALS = ['cmp','cmpl','cntlzw']
POWERPC_LOOPS = ['loop']
POWERPC_COMMENTS = [';','#']    


# SPARC Assembly
SPARC_ASSIGNMENTS = ['mov','set','ld','lduw','ldub','lduh','st','stw','stb',
                      'sth','add','addcc','sub','subcc','mulx','sdivx',
                    'udivx','and','andcc','or','orcc','xor','xorcc','sll',
                    'srl','sra']

SPARC_BRANCHES = ['ba','bn','be','bne','bg','bge','bl','ble',
                  'bgu','bgeu','blu','bleu','call','ret','retl','jmp']

SPARC_CONDITIONALS = ['cmp','tst','scc','movcc']
SPARC_LOOPS = []
SPARC_COMMENTS = ['!','/*','*/']

# Z80 Assembly
Z80_ASSIGNMENTS = ['LD','ADD','ADC','SUB','SBC','INC','DEC','AND','OR','XOR',
                  'CP','NEG','RLCA','RLA','RRCA','RRA','RLC','RL','RRC','RR',
                  'SLA','SRA','SRL','SLL']

Z80_BRANCHES = ['JP','JR','CALL','RET','RST']
Z80_CONDITIONALS = ['JP cc', 'JR cc', 'CALL cc','RET cc','CP','BIT','SET','RES'] 
Z80_LOOPS = ['DJNZ'] 
Z80_COMMENTS = [';']



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

# Write assembly languages dictionary to a file
with open('asm_tokens.json', 'w') as asm_file:
    json.dump(asm_dict, asm_file, indent=4)

print("Assembly instructions JSON file has been generated.")

