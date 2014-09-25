#
# Copyright 214 Joseph Landry
#

.set	SYS_SETUID,23
.set	SYS_GETUID,24

.section .text
.global _start

_start:
	xor	%eax,%eax
	movb	$SYS_GETUID,%al
	int	$0x80

	mov	%eax,%ebx
	xor	%eax,%eax
	movb	$SYS_SETUID,%al
	int	$0x80
