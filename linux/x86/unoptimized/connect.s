.section .text
.global _start


# Various socketcall numbers http://www.scs.stanford.edu/histar/src/pkg/uclibc/libc/inet/socketcalls.c
#define SYS_SOCKET      1
#define SYS_BIND        2
#define SYS_CONNECT     3
#define SYS_LISTEN      4
#define SYS_ACCEPT      5
#define SYS_GETSOCKNAME 6
#define SYS_GETPEERNAME 7
#define SYS_SOCKETPAIR  8
#define SYS_SEND        9
#define SYS_RECV        10
#define SYS_SENDTO      11
#define SYS_RECVFROM    12
#define SYS_SHUTDOWN    13
#define SYS_SETSOCKOPT  14
#define SYS_GETSOCKOPT  15
#define SYS_SENDMSG     16
#define SYS_RECVMSG     17
#endif

_start:
  jmp end
begin:
  popl %edi

socket:
  mov $0x66, %eax #sys_socketcall(int call, args)
  mov $0x01, %ebx #socket(int domain, int type, int protocol)
  mov $0x02, %ecx # int domain = AF_INET (0x2)
  mov $0x01, %edx # int type = SOCK_STREAM (0x1)
  mov $0x00, %esi # int protocol = 0
  int $0x80

socket_test:
  cmpl $-0x1, %eax
  jz exit
  push %eax

connect:
  mov $0x66, %eax # sys_socketcall(int call, args)
  mov $0x03, %ebx # connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
  mov (%esp), %ecx #int sockfd
  mov %edi, %edx # sockaddr *addr
  mov $0x08, %esi
  int $0x80

connect_test:
  cmp $0x0, %eax
  jnz exit

send:
  mov $0x66, %eax # sys_socketcall(int call, args)
  mov $0x09, %ebx # send(int sockfd, void *buf, size_t len, int flags)
  mov (%esp), %ecx #int sockfd
  lea 0x8(%edi), %edx # void *buf
  mov 0x0D, %esi # size_t len
  mov 0x00, %edi # int flags
  int $0x80

close:
  movl $0x6, %eax #sys_close(int fd)
  mov (%esp), %ebx #int sockfd
  int $0x80

exit:
  mov $0x1, %eax # sys_exit()
  mov $0x0, %ebx # int status
  int $0x80


end:
  call begin

addr:
.short 2
.short 0x1111
.byte 127,0,0,1
.ascii "Hello World!\n"
