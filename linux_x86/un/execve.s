/*
 * Copyright 2013 Joseph Landry
 */

.section .text
.global _start

.set SYS_exit,1
.set SYS_execve,11

_start:
	jmp	end
begin:
	popl	%esi

build_argv:	
	pushl	$0		# argv[n] = NULL
	movl	%esi, %eax
	jmp	2f

1:
	add	$1, %eax
2:
	cmpb	$0, (%eax)
	jz	continue
	pushl	%eax			# argv[n]
3:
	cmpb	$0, (%eax)
	jz	1b
	add	$1, %eax
	jmp	3b

continue:
	pushl	$0x0			#envp[0] = NULL
	
	movl	%esp, %edx		# char *envp[]
	lea	0x4(%esp), %ecx		# char *argv[]
	movl	(%ecx), %ebx		# char *filename
	movl	$SYS_execve,%eax	# sys_execve()
	int	$0x80

exit:
	mov	$1,%ebx			# int status
	mov	$SYS_exit,%eax
	int	$0x80

end:
	call begin

params:
.ascii "sh\000"
.ascii "-c\000"
.ascii "/bin/sh\000\000"
