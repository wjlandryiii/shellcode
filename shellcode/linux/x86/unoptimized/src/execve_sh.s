.section .text
.global _start

_start:
  jmp end
begin:
  popl %esi

  movl $0xb, %eax # sys_execve()
  movl %esi, %ebx # char *filename
  pushl $0x0
  pushl %esi
  movl %esp, %ecx # char *argv[]
  pushl $0x0
  movl %esp, %edx # char *envp[]
  int $0x80

end:
  call begin

path:
.ascii "/bin/sh\000"
