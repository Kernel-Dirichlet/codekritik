section .data
    message db 'Hello, World!', 0Ah    ; Define the message string with a newline character

section .text
    global _start

_start:
    ; Write the message to stdout
    mov eax, 4          ; System call number for sys_write
    mov ebx, 1          ; File descriptor 1 is stdout
    mov ecx, message    ; Address of the message string
    mov edx, 14         ; Length of the message (13 characters + newline)
    int 80h             ; Call kernel

    ; Exit the program
    mov eax, 1          ; System call number for sys_exit
    xor ebx, ebx        ; Return 0 status
    int 80h             ; Call kernel
