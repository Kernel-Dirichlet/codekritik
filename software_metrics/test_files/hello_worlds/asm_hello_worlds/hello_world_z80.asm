; Hello World program for Z80 assembly

org 100h        ; Program starts at address 100h (CP/M convention)

start:
    ld de, msg  ; Load address of message into DE
    ld c, 9     ; BDOS function 9: Print string
    call 5      ; Call BDOS (CP/M system call)

    ld c, 0     ; BDOS function 0: System reset
    call 5      ; Call BDOS to exit program

msg:
    db 'Hello, World!$'  ; Message to print, terminated with '$'

end start
