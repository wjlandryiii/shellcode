.section .text
.global _start

_start:

open:
  add r0, pc, #(filename - . - 8) @ char *pathname
  mov r1, #0 @flags
  mov r2, #0 @mode
  mov r7, #5 @int open(const char *pathname, int flags, mode_t mode);
  svc 0
open_test:
  cmp r0, #0
  blt exit
  mov r6, r0 @save sockfd

alloc_buff:
  mov r0, #0
  push {r0}

loop:

read:
  mov r0, r6
  mov r1, sp
  mov r2, #1
  mov r7, #3
  svc 0
read_test:
  cmp r0, #0
  ble loop_continue

write:
  mov r0, #1
  mov r1, sp
  mov r2, #1
  mov r7, #4
  svc 0

  b loop

loop_continue:

close:
  mov r0, r6
  mov r7, #6
  svc 0

exit:
  mov r0, #0
  mov r7, #1
  svc 0

filename:
.ascii "readfile.s\000"
