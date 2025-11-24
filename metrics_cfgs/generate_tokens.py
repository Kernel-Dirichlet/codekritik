import json 

# ========================= HIGH LEVEL LANGUAGES ========================== #
# ================================================================================= #

PYTHON_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '//=', '**=', '&=', '|=', '^=', '>>=', '<<=']
PYTHON_BRANCHES = ['if', 'elif', 'else', 'try', 'except', 'finally', 'with', 'for', 'while']
PYTHON_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=', 'is', 'is not', 'in', 'not in']
PYTHON_LOOPS = ['for', 'while']
PYTHON_COMMENTS = ['#','"""',"'''"] 

# ================================================================================= #

CPP_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
CPP_BRANCHES = ['if', 'else', 'switch', 'case', 'try', 'catch', 'default']
CPP_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=','&&', '||', '!']
CPP_LOOPS = ['for', 'while', 'do']
CPP_COMMENTS = ['//', '/*', '*/']

# ================================================================================= #

C_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
C_BRANCHES = ['if', 'else', 'switch', 'case', 'default']
C_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=','&&', '||', '!']
C_LOOPS = ['for', 'while', 'do']
C_COMMENTS = ['//', '/*', '*/'] 

# ================================================================================= #

CSHARP_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
CSHARP_BRANCHES = ['if', 'else', 'switch', 'case', 'try', 'catch', 'finally', 'default']
CSHARP_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=','&&', '||', '!']
CSHARP_LOOPS = ['for', 'while', 'do', 'foreach']
CSHARP_COMMENTS = ['//', '/*', '*/', '///']

# ================================================================================= #

OBJC_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
OBJC_BRANCHES = ['if', 'else', 'switch', 'case', 'try', 'catch', 'finally', 'default']
OBJC_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=','&&', '||', '!']
OBJC_LOOPS = ['for', 'while', 'do', 'foreach']
OBJC_COMMENTS = ['//', '/*', '*/']

# ================================================================================= # 

BASH_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
BASH_BRANCHES = ['if', 'elif', 'else', 'case', 'esac']
BASH_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=', '-eq', '-ne', '-lt', '-le', '-gt', '-ge',
                     '||', '&&', '!']
BASH_LOOPS = ['for', 'while', 'until']
BASH_COMMENTS = ['#', '<<COMMENT', 'COMMENT','EOF']

# ================================================================================= #

JAVA_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
JAVA_BRANCHES = ['if', 'else', 'switch', 'case', 'try', 'catch', 'finally', 'default']
JAVA_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=','&&', '||', '!']
JAVA_LOOPS = ['for', 'while', 'do', 'foreach']
JAVA_COMMENTS = ['//', '/*', '*/', '/**', '**/']

# ================================================================================= #

JAVASCRIPT_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
JAVASCRIPT_BRANCHES = ['if', 'else', 'switch', 'case', 'try', 'catch', 'finally', 'default']
JAVASCRIPT_CONDITIONALS = ['==', '===', '!=', '!==', '<', '>', '<=', '>=','&&', '||', '!']
JAVASCRIPT_LOOPS = ['for', 'while', 'do', 'for...in', 'for...of']
JAVASCRIPT_COMMENTS = ['//', '/*', '*/', '/**', '**/']

# ================================================================================= #

GO_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
GO_BRANCHES = ['if', 'else', 'switch', 'case', 'default']
GO_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=','&&', '||', '!']
GO_LOOPS = ['for']
GO_COMMENTS = ['//', '/*', '*/']

# ================================================================================= #

TYPESCRIPT_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
TYPESCRIPT_BRANCHES = ['if', 'else', 'switch', 'case', 'try', 'catch', 'finally', 'default']
TYPESCRIPT_CONDITIONALS = ['==', '===', '!=', '!==', '<', '>', '<=', '>=','&&', '||', '!']
TYPESCRIPT_LOOPS = ['for', 'while', 'do', 'for...in', 'for...of']
TYPESCRIPT_COMMENTS = ['//', '/*', '*/', '/**', '**/']

# ================================================================================= #

FORTRAN_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '**=']
FORTRAN_BRANCHES = ['if', 'else', 'select', 'case', 'end select']
FORTRAN_CONDITIONALS = ['.eq.', '.ne.', '.lt.', '.le.', '.gt.', '.ge.','.and.', '.or.', '.not.']
FORTRAN_LOOPS = ['do', 'do while', 'do until']
FORTRAN_COMMENTS = ['!','c','C','*']

# ================================================================================= #

COBOL_ASSIGNMENTS = ['MOVE', 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE']
COBOL_BRANCHES = ['IF', 'ELSE', 'EVALUATE', 'WHEN', 'END-EVALUATE']
COBOL_CONDITIONALS = ['=', '!=', '<', '>', '<=', '>=']
COBOL_LOOPS = ['PERFORM', 'UNTIL', 'VARYING']
COBOL_COMMENTS = ['*', '*>']

# ================================================================================= #

PHP_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
PHP_BRANCHES = ['if', 'else', 'elseif', 'switch', 'case', 'try', 'catch', 'finally', 'default']
PHP_CONDITIONALS = ['==', '===', '!=', '!==', '<', '>', '<=', '>=','&&', '||', '!']
PHP_LOOPS = ['for', 'while', 'do', 'foreach']
PHP_COMMENTS = ['//', '#', '/*', '*/', '/**', '**/']

# ================================================================================= #

SCALA_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
SCALA_BRANCHES = ['if', 'else', 'switch', 'case', 'try', 'catch', 'finally', 'default','yield']
SCALA_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=','&&', '||', '!']
SCALA_LOOPS = ['for', 'while', 'do', 'foreach']
SCALA_COMMENTS = ['//', '/*', '*/', '/**', '**/']

# ================================================================================= #

RUST_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
RUST_BRANCHES = ['if', 'else', 'match','else if']
RUST_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=','&&', '||', '!']
RUST_LOOPS = ['for', 'while', 'loop']
RUST_COMMENTS = ['//', '/*', '*/', '///']

# ================================================================================= #

JULIA_ASSIGNMENTS = ['=', '+=', '-=', '*=', '/=', '%=', '<<=', '>>=', '&=', '|=', '^=']
JULIA_BRANCHES = ['if', 'elseif', 'else', 'try', 'catch', 'finally']
JULIA_CONDITIONALS = ['==', '!=', '<', '>', '<=', '>=','&&', '||', '!']
JULIA_LOOPS = ['for', 'while']
JULIA_COMMENTS = ['#', '#--', '-#']

# ================================================================================= #

# ========================= LOW LEVEL LANGUAGES ========================== #
# ================================================================================= #

X86_ASM_ASSIGNMENTS = ['mov','lea','push','pop','add','sub','xchg','mul',
                       'imul','div','idiv','xor','and','or','shl','sal',
                       'shr','sar','movzx','movsx','inc','dec','neg','not']

X86_ASM_BRANCHES = ['jmp','call','ret','jo','jno','js','jns','je','jne','jz',
                    'jnz','jg','jge','jl','jle','ja','jae','jb','jbe','jc',
                    'jnc','jp','jnp']

X86_ASM_CONDITIONALS = ['cmp','test','cmove','cmovne','cmovg','cmovge','cmovl',
                       'cmovle','cmova','cmovae','cmovb','cmovbe','sete','setne',
                       'setg','setge','setl','setle','seta','setae','setb','setbe',
                       'seto','setno','sets','setns','setp','setnp']

X86_ASM_LOOPS = ['loop', 'jcxz', 'jcxnz','jecxz','jecxnz']
X86_ASM_COMMENTS = [';','#']

# ================================================================================= #

ARM_ASM_ASSIGNMENTS = ['MOV','MVN','ADD','ADC','SUB','SBC','MUL',
                       'MLA','SDIV','UDIV','AND','ORR','EOR','LSL',
                       'LSR','ASR','ROR','RRX']

ARM_ASM_BRANCHES = ['B','BL','BX','BEQ','BNE','BGT','BGE',
                    'BLT','BLE','BHI','BHS','BCS','BLO',
                     'BCC','BMI','BPL']

ARM_ASM_CONDITIONALS = ['CMP', 'TST','CMN', 'TEQ']
ARM_ASM_LOOPS = []
ARM_ASM_COMMENTS = [';','@']

# ================================================================================= #

RISCV_ASM_ASSIGNMENTS = ['ADD','SUB','MUL','MULH','MULHU','MULHSU','DIV','DIVU','REM',
                         'REMU','AND','OR','XOR','SLL','SRL','SRA','LUI','AUIPC','LW',
                          'SW']

RISCV_ASM_BRANCHES = ['JAL', 'JALR', 'BEQ', 'BNE', 'BLT', 'BGE', 'BLTU', 'BGEU']
RISCV_ASM_CONDITIONALS = ['SLT', 'SLTU','SLTI','SLTIU']
RISCV_ASM_LOOPS = []
RISCV_ASM_COMMENTS = ['#', '//', '/*', '*/']

# ================================================================================= #

POWERPC_ASM_ASSIGNMENTS = ['lwz','stw','addi','add','subf','mullw','mulhw','divw','divwu',
                           'and','andi','or','ori','xor','xori','nor','slw','srw','sraw']

POWERPC_ASM_BRANCHES = ['b', 'beq', 'bne', 'bgt', 'bge', 'blt', 'ble', 'bl', 'blr','bc']
POWERPC_ASM_CONDITIONALS = ['cmp','cmpl','cntlzw']
POWERPC_ASM_LOOPS = ['loop']
POWERPC_ASM_COMMENTS = [';','#']    

# ================================================================================== #

MIPS_ASM_ASSIGNMENTS = ['add','addu','sub','subu','mult','multu','div','divu','and','andi',
                        'or','ori','xor','xori','nor','sll','sllv','srl','srlv','sra','srav']

MIPS_ASM_BRANCHES = ['j','jal','jr','beq','bne','bgtz','bgez','bltz','blez']
MIPS_ASM_CONDITIONALS = ['slt', 'sltu','slti','sltiu']
MIPS_ASM_LOOPS = []
MIPS_ASM_COMMENTS = ['#']

# ================================================================================== #
# ========================= INTERMEDIATE REPRESENTATIONS =========================== #
# ================================================================================== #

LLVM_IR_ASSIGNMENTS = ['add','sub','mul','udiv','sdiv','urem','srem','fadd','fsub','fmul','fdiv',
                       'frem','and','or','xor','shl','lshr','ashr','alloca',
                       'load','store','getelementptr','bitcast','zext','sext',
                       'trunc','phi']

LLVM_IR_BRANCHES = ['br','switch','invoke','ret','call','indirectbr']

LLVM_IR_CONDITIONALS = ['icmp','fcmp','select']

LLVM_IR_LOOPS = []
LLVM_IR_COMMENTS = [';']    

INSTRUCTIONS_DICT = {
    'Python': {'assignments': PYTHON_ASSIGNMENTS,
               'branches': PYTHON_BRANCHES,
               'conditionals': PYTHON_CONDITIONALS,
               'loops': PYTHON_LOOPS,
               'comments': PYTHON_COMMENTS},

    'C++': {'assignments': CPP_ASSIGNMENTS,
            'branches': CPP_BRANCHES,
            'conditionals': CPP_CONDITIONALS,
            'loops': CPP_LOOPS,
            'comments': CPP_COMMENTS},

    'C': {'assignments': C_ASSIGNMENTS,
          'branches': C_BRANCHES,
          'conditionals': C_CONDITIONALS,
          'loops': C_LOOPS,
          'comments': C_COMMENTS},

    'C#': {'assignments': CSHARP_ASSIGNMENTS,
           'branches': CSHARP_BRANCHES,
           'conditionals': CSHARP_CONDITIONALS,
           'loops': CSHARP_LOOPS,
           'comments': CSHARP_COMMENTS},

    'Objective-C': {'assignments': OBJC_ASSIGNMENTS,
                    'branches': OBJC_BRANCHES,
                    'conditionals': OBJC_CONDITIONALS,
                    'loops': OBJC_LOOPS,
                    'comments': OBJC_COMMENTS},

    'Bash': {'assignments': BASH_ASSIGNMENTS,
             'branches': BASH_BRANCHES,
             'conditionals': BASH_CONDITIONALS,
             'loops': BASH_LOOPS,
             'comments': BASH_COMMENTS},

    'Java': {'assignments': JAVA_ASSIGNMENTS,
             'branches': JAVA_BRANCHES,
             'conditionals': JAVA_CONDITIONALS,
             'loops': JAVA_LOOPS,
             'comments': JAVA_COMMENTS},

    'JavaScript': {'assignments': JAVASCRIPT_ASSIGNMENTS,
                   'branches': JAVASCRIPT_BRANCHES,
                   'conditionals': JAVASCRIPT_CONDITIONALS,
                   'loops': JAVASCRIPT_LOOPS,
                   'comments': JAVASCRIPT_COMMENTS},

    'Go': {'assignments': GO_ASSIGNMENTS,
           'branches': GO_BRANCHES,
           'conditionals': GO_CONDITIONALS,
           'loops': GO_LOOPS,
           'comments': GO_COMMENTS},

    'TypeScript': {'assignments': TYPESCRIPT_ASSIGNMENTS,
                   'branches': TYPESCRIPT_BRANCHES,
                   'conditionals': TYPESCRIPT_CONDITIONALS,
                   'loops': TYPESCRIPT_LOOPS,
                   'comments': TYPESCRIPT_COMMENTS},

    'Fortran': {'assignments': FORTRAN_ASSIGNMENTS,
                'branches': FORTRAN_BRANCHES,
                'conditionals': FORTRAN_CONDITIONALS,
                'loops': FORTRAN_LOOPS,
                'comments': FORTRAN_COMMENTS},

    'COBOL': {'assignments': COBOL_ASSIGNMENTS,
              'branches': COBOL_BRANCHES,
              'conditionals': COBOL_CONDITIONALS,
              'loops': COBOL_LOOPS,
              'comments': COBOL_COMMENTS},

    'PHP': {'assignments': PHP_ASSIGNMENTS,
            'branches': PHP_BRANCHES,
            'conditionals': PHP_CONDITIONALS,
            'loops': PHP_LOOPS,
            'comments': PHP_COMMENTS},

    'Scala': {'assignments': SCALA_ASSIGNMENTS,
              'branches': SCALA_BRANCHES,
              'conditionals': SCALA_CONDITIONALS,
              'loops': SCALA_LOOPS,
              'comments': SCALA_COMMENTS},

    'Rust': {'assignments': RUST_ASSIGNMENTS,
             'branches': RUST_BRANCHES,
             'conditionals': RUST_CONDITIONALS,
             'loops': RUST_LOOPS,
             'comments': RUST_COMMENTS},

    'Julia': {'assignments': JULIA_ASSIGNMENTS,
              'branches': JULIA_BRANCHES,
              'conditionals': JULIA_CONDITIONALS,
              'loops': JULIA_LOOPS,
              'comments': JULIA_COMMENTS},

    'x86': {'assignments': X86_ASM_ASSIGNMENTS,
            'branches': X86_ASM_BRANCHES,
            'conditionals': X86_ASM_CONDITIONALS,
            'loops': X86_ASM_LOOPS,
            'comments': X86_ASM_COMMENTS},

    'ARM': {'assignments': ARM_ASM_ASSIGNMENTS,
            'branches': ARM_ASM_BRANCHES,
            'conditionals': ARM_ASM_CONDITIONALS,
            'loops': ARM_ASM_LOOPS,
            'comments': ARM_ASM_COMMENTS},

    'RISC-V': {'assignments': RISCV_ASM_ASSIGNMENTS,
               'branches': RISCV_ASM_BRANCHES,
               'conditionals': RISCV_ASM_CONDITIONALS,
               'loops': RISCV_ASM_LOOPS,
               'comments': RISCV_ASM_COMMENTS},

    'PowerPC': {'assignments': POWERPC_ASM_ASSIGNMENTS,
                'branches': POWERPC_ASM_BRANCHES,
                'conditionals': POWERPC_ASM_CONDITIONALS,
                'loops': POWERPC_ASM_LOOPS,
                'comments': POWERPC_ASM_COMMENTS},

    'MIPS': {'assignments': MIPS_ASM_ASSIGNMENTS,
             'branches': MIPS_ASM_BRANCHES,
             'conditionals': MIPS_ASM_CONDITIONALS,
             'loops': MIPS_ASM_LOOPS,
             'comments': MIPS_ASM_COMMENTS},

    'LLVM': {'assignments': LLVM_IR_ASSIGNMENTS,
             'branches': LLVM_IR_BRANCHES,
              'conditionals': LLVM_IR_CONDITIONALS,
              'loops': LLVM_IR_LOOPS,
              'comments': LLVM_IR_COMMENTS}
}

# Write instructions dictionary to a file
with open('tokens.json', 'w') as file:  
    json.dump(INSTRUCTIONS_DICT, file, indent=4)    


