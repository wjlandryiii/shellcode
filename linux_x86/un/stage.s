/*
 * Copyright 2014 Joseph Landry
 */

.struct 0
mm_addr:
.struct mm_addr + 4
mm_len:
.struct mm_len + 4
mm_prot:
.struct mm_prot + 4
mm_flags:
.struct mm_flags + 4
mm_fd:
.struct mm_fd + 4
mm_offset:


.section .text
.global _start

.set WRITE_FD,0x0



_start:
	pushl	$mmapsz
	call	puts
	add	$4,%esp

	pushl	$0
	pushl	$-1
	pushl	$0x22
	pushl	$0x7
	pushl	$0x1000
	pushl	$0
	call	mmap2
	add	$0x18,%esp

	test	%eax,%eax
	jnz	1f
	pushl	$failsz
	call	puts
	add	$4,%esp
	call	exit

1:
	mov	%eax,%edx
	pushl	$oksz
	call	puts
	add	$4,%esp

	pushl	$0x1000
	pushl	%edx
	pushl	$0
	call	read
	add	$0xC,%esp

	cmp	$0x0,%eax
	jg	1f
	pushl	$failsz
	call	puts
	add	$4,%esp
	call	exit

1:
	pushl	%eax
	pushl	%edx
	pushl	$1
	call	write
	
	jmp	exit




mmap2:
.set addr,0x8
.set len,0xC
.set prot,0x10
.set flags,0x14
.set fd,0x1C
.set offs,0x20

	pushl	%ebp
	movl	%esp,%ebp
	pushl	%ebx
	pushl	%ecx
	pushl	%edx
	pushl	%esi
	pushl	%edi
	pushl	%ebp

	movl	addr(%ebp),%ebx
	movl	len(%ebp),%ecx
	movl	prot(%ebp),%edx
	movl	flags(%ebp),%esi
	movl	fd(%ebp),%edi
	movl	offs(%ebp),%ebp
	movl	$192,%eax
	int	$0x80

	popl	%ebp
	popl	%edi
	popl	%esi
	popl	%esi
	popl	%edx
	popl	%ecx
	popl	%ebx

	cmp	$0xFFFFF000,%eax
	jbe	1f
	xor	%eax,%eax

1:
	movl	%ebp,%esp
	popl	%ebp
	ret
	


puts:
.set buf,0x8

	pushl	%ebp
	movl	%esp,%ebp
	pushl	%ebx
	pushl	%ecx
	pushl	%edx

	movl	$-1,%ecx
	movl	buf(%ebp),%edi
	xor	%eax,%eax
	cld
repne	scasb
	not	%ecx
	lea	-1(%ecx),%eax

	pushl	%eax
	pushl	buf(%ebp)
	pushl	$0x1
	call	write
	add	$0xC,%esp

	popl	%edx
	popl	%ecx
	popl	%ebx
	movl	%ebp,%esp
	popl	%ebp
	ret
	


write:
.set fd,0x8
.set buf,0xC
.set count,0x10

	pushl	%ebp
	movl	%esp,%ebp
	pushl	%ebx
	pushl	%ecx
	pushl	%edx

	movl	fd(%ebp),%ebx
	movl	buf(%ebp),%ecx
	movl	count(%ebp),%edx	
	movl	$0x4,%eax
	int	$0x80
	cmp	$0x0,%eax
	jge	1f
	movl	$-1,%eax

1:
	popl	%edx
	popl	%ecx
	popl	%ebx
	movl	%ebp,%esp
	popl	%ebp
	ret

read:
.set fd,0x8
.set buf,0xC
.set count,0x10

	pushl	%ebp
	movl	%esp,%ebp
	pushl	%ebx
	pushl	%ecx
	pushl	%edx

	movl	fd(%ebp),%ebx
	movl	buf(%ebp),%ecx
	movl	count(%ebp),%edx
	movl	$0x3,%eax
	int	$0x80
	cmp	$0x0,%eax
	jge	1f
	movl	$-1,%eax

1:
	popl	%edx
	popl	%ecx
	popl	%ebx
	movl	%ebp,%esp
	popl	%ebp
	ret

exit:
	mov	$0x1,%eax
	mov	$0x0,%ebx
	int	$0x80
	hlt

oksz: 	.asciz	"OK\n"
failsz:	.asciz 	"FAIL\n"
mmapsz:	.asciz	"mmap...."
readsz: .asciz	"read...."
