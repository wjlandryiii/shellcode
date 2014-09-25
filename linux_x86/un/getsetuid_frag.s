#
# Copyright 2014 Joseph Landry
#

.set	SYS_SETUID,23
.set	SYS_GETEUID,49

.section .text
.global _start

_start:

	mov	$SYS_GETEUID,%eax
	int	$0x80

	mov	%eax,%ebx
	mov	$SYS_SETUID,%eax
	int	$0x80
