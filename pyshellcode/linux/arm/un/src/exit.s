.section .text
.global _start

_start:

exit:
  mov r0, #0
  mov r7, #1
  svc 0
