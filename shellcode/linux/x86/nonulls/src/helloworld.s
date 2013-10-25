.section .text
.global _start

_start:
  jmp end
begin:
  popl %esi

write:
  xor %edx, %edx
  movb $0x0D, %dl
  movl %esi, %ecx #buff
  xor %ebx, %ebx
  inc %ebx
  xor %eax, %eax
  movb $0x04, %al
  int $0x80

exit:
  xor %ebx, %ebx
  mov %ebx, %eax
  inc %eax
  int $0x80 #sys_exit(0)

end:
  call begin

hello_string:
.ascii "Hello World!\n"
