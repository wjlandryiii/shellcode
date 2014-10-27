#
# Copyright 2014 Joseph Landry
#

.set	SYS_EXIT,1
.set	SYS_WRITE,4

.section .text
.global _start

_start:
	pushl	%esp

1:
	# cmpl	$0xC0000000,(%esp)
	cmpl	$0xFFFFC000,(%esp)
	je	1f
	call	dump_hex_line
	add	$16,(%esp)
	jmp	1b
1:
	movl	$0,(%esp)
	call	exit


dump_hex_line:
.set	arg_p,8
.set	r,4
.set	s,0
	push	%ebp
	mov	%esp,%ebp
	sub	$4,%esp

	mov	arg_p(%ebp),%eax
	mov	%eax,(%esp)
	call	print_dword_hex

	movl	$0x3A,(%esp)
	call	putchar

	movl	$0x20,(%esp)
	call	putchar


	xor	%ecx,%ecx

1:
	movl	arg_p(%ebp),%eax
	movb	(%eax,%ecx),%al
	mov	%eax,(%esp)
	call	print_byte_hex
	movl	$0x20,(%esp)
	call	putchar

	inc	%ecx
	cmp	$0x10,%ecx
	jl	1b

	movl	$0x20,(%esp)
	call	putchar

	xor	%ecx,%ecx

1:
	movl	arg_p(%ebp),%eax
	movb	(%eax,%ecx),%al
	mov	%eax,(%esp)
	call	isprint
	test	%eax,%eax
	jz	2f
	movl	arg_p(%ebp),%eax
	movb	(%eax,%ecx),%al
	mov	%eax,(%esp)
	jmp	3f
2:
	movl	$0x2E,(%esp)

3:
	call	putchar
	inc	%ecx
	cmp	$0x10,%ecx
	jl	1b
	

	movl	$0xA,(%esp)
	call	putchar

	mov	%ebp,%esp
	pop	%ebp
	ret

isprint:
	push	%ebp
	mov	%esp,%ebp

	xor	%eax,%eax
	movb	8(%ebp),%al

	cmp	$0x20,%eax
	jl	1f
	cmp	$0x7E,%eax
	jg	1f
	mov	$1,%eax
	jmp	2f	
1:
	mov	$0,%eax
2:
	mov	%ebp,%esp
	pop	%ebp
	ret


print_all_bytes:
	push	%ebp
	mov	%esp,%ebp
	sub	$4,%esp

	xor	%ecx,%ecx
1:
	movl	%ecx,(%esp)
	call	print_byte_hex

	movl	$10,(%esp)
	call	putchar
	inc	%ecx
	cmp	$0x100,%ecx
	je	1f
	jmp	1b
1:
	leave
	ret

print_dword_hex:
.set	arg_word,0xC
	push	%ebp
	mov	%esp,%ebp
	sub	$4,%esp

	mov	arg_word(%esp),%eax
	shr	$24,%eax
	mov	%eax,(%esp)
	call	print_byte_hex
	mov	arg_word(%esp),%eax
	shr	$16,%eax
	mov	%eax,(%esp)
	call	print_byte_hex
	mov	arg_word(%esp),%eax
	shr	$8,%eax
	mov	%eax,(%esp)
	call	print_byte_hex
	mov	arg_word(%esp),%eax
	mov	%eax,(%esp)
	call	print_byte_hex

	mov	%ebp,%esp
	pop	%ebp
	ret

print_word_hex:
.set	arg_word,0xC
	push	%ebp
	mov	%esp,%ebp
	sub	$4,%esp

	mov	arg_word(%esp),%eax
	shr	$8,%eax
	mov	%eax,(%esp)
	call	print_byte_hex
	mov	arg_word(%esp),%eax
	mov	%eax,(%esp)
	call	print_byte_hex

	mov	%ebp,%esp
	pop	%ebp
	ret

print_byte_hex:
.set	arg_byte,8
.set	buf,-0x10

	push	%ebp
	mov	%esp,%ebp
	push	%ebx
	push	%ecx
	push	%edx
	sub	$4,%esp


	movl	$0,buf(%ebp)

	xor	%eax,%eax
	movb	arg_byte(%ebp),%al
	shrb	$4,%al
	add	$0x30,%al
	cmpb	$0x3A,%al
	jb	1f
	add	$0x7,%al
1:
	movb	%al,buf(%ebp)

	movb	arg_byte(%ebp),%al
	andb	$0xF,%al
	addb	$0x30,%al
	cmpb	$0x3A,%al
	jb	1f
	add	$0x7,%al
1:
	movb	%al,buf+1(%ebp)
	

	movl	$2,%edx
	lea	buf(%ebp),%ecx
	movl	$1,%ebx
	movl	$SYS_WRITE,%eax
	int	$0x80

	add	$4,%esp
	pop	%edx
	pop	%ecx
	pop	%ebx
	leave
	ret


puts:
	push	%ebp
	mov	%esp,%ebp
	push	%ebx
	push	%ecx
	push	%edx

	movl	8(%ebp),%eax
	push	%eax
	call	strlen
	addl	$4,%esp

	movl	%eax,%edx
	movl	8(%ebp),%ecx
	movl	$1,%ebx
	movl	$SYS_WRITE,%eax
	int	$0x80

	pop	%edx
	pop	%ecx
	pop	%edx
	leave
	ret


putchar:
	push	%ebp
	mov	%esp,%ebp
	push	%ebx
	push	%ecx
	push	%edx
	sub	$4,%esp

	movl	$1,%edx
	lea	8(%ebp),%ecx
	movl	$1,%ebx
	movl	$SYS_WRITE,%eax
	int	$0x80

	add	$4,%esp	
	pop	%edx
	pop	%ecx
	pop	%edx
	movl	%ebp,%esp
	pop	%ebp	
	ret

strlen:
	push	%ebp
	mov	%esp,%ebp
	push	%ebx
	push	%ecx

	mov	8(%ebp),%ebx
	xor	%ecx,%ecx

1:
	cmpb	$0,(%ebx,%ecx)
	je	2f
	inc	%ecx
	jmp	1b

2:
	mov	%ecx,%eax
	pop	%ecx
	pop	%ebx
	leave
	ret

exit:
	mov	4(%esp),%ebx
	mov	$SYS_EXIT,%eax
	int	$0x80
	hlt


hello_string:
.ascii	"hello world\n\x00"
