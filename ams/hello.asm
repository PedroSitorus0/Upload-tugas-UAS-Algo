section .data
    msg db "Halo dari Assembly di Fedora!", 0xA
    len equ $ - msg

section .text
    global _start

_start:
    mov eax, 1          ; syscall: sys_write
    mov edi, 1          ; file descriptor: stdout
    mov rsi, msg        ; pointer ke pesan
    mov edx, len        ; panjang pesan
    syscall             ; panggil kernel

    mov eax, 60         ; syscall: sys_exit
    xor edi, edi        ; return code 0
    syscall

    