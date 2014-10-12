#
# Copyright 214 Joseph Landry
#

.set	SYS_SETUID,23
.set	SYS_GETEUID,49
.set	SYS_SETRESUID,164

.section .text
.global _start

_start:
	xor	%eax,%eax
	movb	$SYS_GETEUID,%al
	int	$0x80

	mov	%eax,%edx
	mov	%eax,%ecx
	mov	%eax,%ebx
	xor	%eax,%eax
	movb	$SYS_SETRESUID,%al
	int	$0x80
