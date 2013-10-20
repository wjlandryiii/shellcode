.section .text
.global _start

_start:
execve:
    add r0, pc, #(filename - . - 8)
    mov r1, #0
    mov r2, #0
    mov r7, #11
    svc 0

exit:
    mov r0, #0
    mov r7, #1
    svc 0


filename:
.ascii "/bin/sh\000"