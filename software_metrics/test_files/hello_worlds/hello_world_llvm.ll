; Hello World program in LLVM IR

@.str = private unnamed_addr constant [14 x i8] c"Hello, World!\0A\00", align 1

define i32 @main() {
    ; Call printf function to print the string
    %1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str, i64 0, i64 0))
    
    ; Return 0 to indicate successful execution
    ret i32 0
}

; Declare the printf function from the C standard library
declare i32 @printf(i8*, ...)
