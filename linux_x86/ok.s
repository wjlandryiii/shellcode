.section .text
.global _start

_start:
	pushl	$0x410A4B4F	# "OK\nA"

write:
	xor	%eax,%eax
	movb	$0x4,%al	# SYS_WRITE
	xor	%ebx,%ebx	
	inc	%ebx		# int fd = 1
	movl	%esp,%ecx	# char *buf
	movl	%eax,%edx
	dec	%edx		# size_t count
	int	$0x80		# size_t write(int fd, char *buf, size_t c)

exit:
	xor	%eax,%eax
	inc	%eax		# SYS_EXIT
	xor	%ebx,%ebx	# int status
	int	$0x80		# exit(int status)
	hlt
