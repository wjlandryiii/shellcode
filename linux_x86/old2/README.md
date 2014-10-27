
<http://www.win.tue.nl/~aeb/linux/lk/lk-4.html>

"The system call number goes into %eax, the first parameter in %ebx, the second in %ecx, the third in %edx, the fourth in %esi, the fifth in %edi, the sixth in %ebp"

Various socketcall numbers <http://www.scs.stanford.edu/histar/src/pkg/uclibc/libc/inet/socketcalls.c>

```
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
```


