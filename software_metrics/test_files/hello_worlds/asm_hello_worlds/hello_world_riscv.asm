.data
    message: .string "Hello, World!\n"

.text
    .global _start

_start:
    # Write the message to stdout
    li a0, 1                # File descriptor 1 is stdout
    la a1, message          # Address of the message string
    li a2, 14               # Length of the message (13 characters + newline)
    li a7, 64               # System call number for sys_write
    ecall                   # Call kernel

    # Exit the program
    li a0, 0                # Return 0 status
    li a7, 93               # System call number for sys_exit
    ecall                   # Call kernel
