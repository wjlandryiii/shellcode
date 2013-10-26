.section .text
.global _start

_start:
  jmp bottom
top:
  popl %esi

openfile:
  xor %eax, %eax
  movb $0x05, %al#sys_open(char *file, int flags, int mode)
  movl %esi, %ebx #file
  xor %ecx, %ecx #flags
  xor %edx, %edx #mode
  int $0x80

savefd:
  movl %eax, %edi

makebuff:
  push $0x0

read:
  xor %eax, %eax
  movb $0x03, %al #sys_read(int fd, void *buff, size_t count)
  movl %edi, %ebx #fd
  movl %esp, %ecx #buff
  xor %edx, %edx
  inc %edx  #count
  int $0x80
  cmp $0x0, %eax
  jle exit

write:
  xchg %edx, %eax
  movl %esp, %ecx #buff
  xor %ebx, %ebx
  inc %ebx
  xor %eax, %eax
  movb $0x04, %al
  int $0x80
  jmp read

#close:
# xor %eax, %eax
#  movb $0x6, %al #sys_close(int fd)
#  movl %edi, %ebx #fd
#  int $0x80

exit:
  xor %ebx, %ebx
  xor %eax, %eax
  inc %eax
  int $0x80 #sys_exit(0)

bottom:
	call top

.ascii "readfile.s\000"

