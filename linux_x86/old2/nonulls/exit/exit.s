.section .text
.global _start

_start:
	xor %ebx, %ebx
	xor %eax, %eax
	inc %eax
	int $0x80 #sys_exit(0)