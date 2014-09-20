#
# Copyright 2014 Joseph Landry
#
.section .text
.global _start

.set SYS_exit,60

_start:
	movq	$SYS_exit,%rax
	movq	$1,%rdi
	syscall
	hlt
