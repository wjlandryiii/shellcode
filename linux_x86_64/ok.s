#
# Copyright 2014 Joseph Landry
#

.section .text
.global _start

.set SYS_WRITE,1
.set SYS_EXIT,60

_start:
	xor	%rax,%rax
	movl	$0x410A4B4F,%eax
	pushq	%rax

write:
	mov	$3,%edx

	mov	%rsp,%rsi

	xor	%rdi,%rdi
	inc	%rdi

	xor	%rax,%rax
	movb	$SYS_WRITE,%al

	syscall
	add	$4,%rsp

exit:
	xor	%rdi,%rdi

	xor	%rax,%rax
	movb	$SYS_EXIT,%al
	syscall
	hlt
