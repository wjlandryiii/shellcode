.section .text
.global _start

_start:

write:
  mov r0, #1
  add r1, pc, #(hello_string - . - 8)
  mov r2, #13
  mov r7, #4
  svc 0

exit:
  mov r0, #0
  mov r7, #1
  svc 0

hello_string:
.ascii "Hello World!\n\000"
