.section .text
.global _start

_start:
  jmp end
begin:
  popl %esi

  mov %esi, %eax # string for strlen

strlen:
  push %ecx
  mov %eax, %ecx

strlen_loop:
  cmpb $0x0, (%ecx)
  jz strlen_done
  add $0x1, %ecx
  jmp strlen_loop

strlen_done:
  sub %eax, %ecx
  mov %ecx, %eax
  pop %ecx

strlen_end:

write:
  movl %eax, %edx #count
  movl %esi, %ecx #buff
  movl $0x1, %ebx #fd
  movl $0x4, %eax #sys_write(fd, buff, count)
  int $0x80

exit:
  mov $0x0, %ebx # int status
  mov $0x1, %eax # sys_exit(status)
  int $0x80

end:
  call begin

hello_string:
.ascii "Hello World!\n\000"
