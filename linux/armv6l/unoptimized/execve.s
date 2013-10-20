.section .text
.global _start

_start:
	mov r0, #0
	push {r0}

	add r0, pc, #(params - . - 8)

outer_loop:
	ldrb r1, [r0]
	cmp r1, #0
	beq loop_continue
	push {r0}
inner_loop:
	ldrb r1, [r0], #1  @increments r0
	cmp r1, #0
	bne inner_loop
	b outer_loop
loop_continue:

execve:
    ldr r0, [sp]
    mov r1, sp
    mov r2, #0
    push {r2}
    mov r2, sp
    mov r7, #11
    svc 0

exit:
    mov r0, #0
    mov r7, #1
    svc 0

params:
.ascii "-a\000/bin/uname\000\000"
