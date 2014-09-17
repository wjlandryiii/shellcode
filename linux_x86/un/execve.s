/*
 * Copyright 2013 Joseph Landry
 */

.section .text
.global _start

_start:
  jmp end
begin:
  popl %esi

  pushl $0x0 # argv[n] = NULL

  movl %esi, %eax
  jmp outer_loop_entry

outer_loop:
  add $0x1, %eax
outer_loop_entry:
  cmpb $0x0, (%eax)
  jz continue
  pushl %eax # argv[n]
inner_loop:
  cmpb $0x0, (%eax)
  jz outer_loop
  add $0x1, %eax
  jmp inner_loop
continue:

  pushl $0x0 #envp[0] = NULL

  movl %esp, %edx # char *envp[]
  lea 0x4(%esp), %ecx # char *argv[]
  movl (%ecx), %ebx # char *filename
  movl $0xb, %eax # sys_execve(char *filename, char *argv[], char *envp[])
  int $0x80

exit:
  mov $0x1, %eax # sys_exit()
  mov $0x0, %ebx # int status
  int $0x80

end:
  call begin

params:
.ascii "-a\000/bin/uname\000\000"
