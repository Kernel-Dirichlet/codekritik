data
    message:    .asciz "Hello, World!\n"

.text
    .global _start

_start:
    /* Write the message to stdout */
    mov r0, #1              @ File descriptor 1 is stdout
    ldr r1, =message        @ Address of the message string
    mov r2, #14             @ Length of the message (13 characters + newline)
    mov r7, #4              @ System call number for sys_write
    swi 0                   @ Call kernel

    /* Exit the program */
    mov r0, #0              @ Return 0 status
    mov r7, #1              @ System call number for sys_exit
    swi 0                   @ Call kernel
