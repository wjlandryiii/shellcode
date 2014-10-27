.section .text
.global _start

_start:
	mov $0x1, %eax # sys_exit()
	mov $0x0, %ebx # int status
	int $0x80
