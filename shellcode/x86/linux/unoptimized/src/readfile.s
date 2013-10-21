.section .text
.global _start

_start:
  jmp bottom
top:
  popl %esi

openfile:
  movl $0x5, %eax #sys_open(char *file, int flags, int mode)
  movl %esi, %ebx #file
  movl $0x0, %ecx #flags
  movl $0x0, %edx #mode
  int $0x80

savefd:
  movl %eax, %edi

makebuff:
  push $0x0

read:
  movl $0x3, %eax #sys_read(int fd, void *buff, size_t count)
  movl %edi, %ebx #fd
  movl %esp, %ecx #buff
  movl $0x1, %edx #count
  int $0x80
  cmp $0x0, %eax
  jle exit

write:
  movl $0x4, %eax #sys_write(int fd, void *buff, size_t count)
  movl $0x1, %ebx #fd
  movl %esp, %ecx #buff
  movl $0x1, %edx #count
  int $0x80
  jmp read

close:
  movl $0x6, %eax #sys_close(int fd)
  movl %edi, %ebx #fd
  int $0x80

exit:
  movl $0x1, %eax #sys_exit(int status)
	movl $0x0, %ebx #int status
  int $0x80

bottom:
	call top

.ascii "readfile.s\000"

