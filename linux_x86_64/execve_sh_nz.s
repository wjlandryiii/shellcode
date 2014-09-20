#
# Copyright 2014 Joseph Landry
#

.set SYS_execve,59
.set SYS_exit,60

.section .text
.global _start

_start:
	xor	%rdx,%rdx
	xor	%rsi,%rsi
	movq	$0xFF68732F6E69622F,%rax
	shl	$8,%rax
	shr	$8,%rax
	push	%rax
	mov	%rsp,%rdi
	xor	%rax,%rax
	movb	$SYS_execve,%al
	syscall

exit:
	xor	%rdi,%rdi
	inc	%rdi	
	xor	%rax,%rax
	movb	$SYS_exit,%al
	syscall
	hlt
	

	
