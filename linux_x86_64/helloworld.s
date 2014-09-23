#
# Copyright 2014 Joseph Landry
#

.section .text
.global _start

.set 	SYS_WRITE,1
.set 	SYS_EXIT,60

_start:
	jmp	end

begin:
	pop	%rsi
	xor	%rdx,%rdx
1:
	cmpb	$0, (%rsi,%rdx)
	jz	2f
	inc	%rdx
	jmp	1b

2:
	xor	%rdi,%rdi
	inc	%rdi

	xor	%rax,%rax
	movb	$SYS_WRITE,%al
write:
	syscall

exit:
	xor	%rdi,%rdi
	xor	%rax,%rax
	movb	$SYS_EXIT,%al
	syscall
	hlt

end:
	call	begin

hello_string:
.ascii "Hello World!\n\x00"
