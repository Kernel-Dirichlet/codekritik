.data
    message: .asciiz "Hello, World!\n"

.text
    .globl main

main:
    # Print the message
    li $v0, 4               # System call code for print_string
    la $a0, message         # Load address of message into $a0
    syscall                 # Call operating system to perform print

    # Exit the program
    li $v0, 10              # System call code for exit
    syscall                 # Call operating system to exit
