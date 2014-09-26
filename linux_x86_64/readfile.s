#
# Copyright 2014 Jospeh Landry
#

.set	SYS_READ,0
.set	SYS_WRITE,1
.set	SYS_OPEN,2
.set	SYS_CLOSE,3
.set	SYS_EXIT,60

.section .text
.global _start

_start:
	jmp	bottom

begin:
	pop	%r12

open:
	movq	$0,%rdx
	movq	$0,%rsi
	movq	%r12,%rdi
	movq	$SYS_OPEN,%rax	
	syscall

	cmpq	$0,%rax
	jl	exit1

	movq	%rax,%r13
	sub	$1024,%rsp
	
read:
	movq	$1024,%rdx
	movq	%rsp,%rsi
	movq	%r13,%rdi
	movq	$SYS_READ,%rax
	syscall

	cmpq	$0,%rax
	jl	exit1
	je	close

write:
	movq	%rax,%rdx
	movq	%rsp,%rsi
	movq	$1,%rdi
	movq	$SYS_WRITE,%rax
	syscall
	jmp read


close:
	movq	%r13,%rdi
	movq	$SYS_CLOSE,%rax
	syscall

	jmp	exit0
	

exit1:
	mov	$1,%rdi
	jmp	exit

exit0:
	movq	$0,%rdi

exit:
	movq	$SYS_EXIT,%rax
	syscall

bottom:
	call	begin

.ascii "/etc/passwd\000"
