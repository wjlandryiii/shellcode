.section .text
.global _start

_start:
  jmp end
begin:
  popl %esi

  pushl $0x0 # argv[n] = NULL

  movl %esi, %eax
  jmp outer_loop_entry

#maybe this loop can be replaced with some repnz instruction?

outer_loop:
  inc %eax

outer_loop_entry:
  cmpb $0x0, (%eax)
  jz execve
  pushl %eax # argv[n]

inner_loop:
  cmpb $0x0, (%eax)
  jz outer_loop
  inc %eax
  jmp inner_loop

execve:
  xor %eax, %eax
  push %eax #envp[0] = NULL
  movl %esp, %edx # char *envp[]
  lea 0x4(%esp), %ecx # char *argv[]
  movl (%ecx), %ebx # char *filename
  movb $0xb, %al # sys_execve(char *filename, char *argv[], char *envp[])
  int $0x80

exit:
  xor %ebx, %ebx
  xor %eax, %eax
  inc %eax
  int $0x80 #sys_exit(0)

end:
  call begin

params:
.ascii "-a\000/bin/uname\000\000"
