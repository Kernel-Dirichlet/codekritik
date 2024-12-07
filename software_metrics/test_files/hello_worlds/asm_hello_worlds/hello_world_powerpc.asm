.data
    message: .asciz "Hello, World!\n"

.text
    .global _start

_start:
    # Load address of message into r3
    lis r3, message@ha
    addi r3, r3, message@l

    # Call the write system call
    li r0, 4        # System call number for write
    li r4, 13       # Length of the string
    li r5, 1        # File descriptor 1 is stdout
    sc              # Perform system call

    # Exit the program
    li r0, 1        # System call number for exit
    li r3, 0        # Exit status
    sc              # Perform system call
