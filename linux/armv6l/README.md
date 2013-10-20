armsuffs

http://man7.org/linux/man-pages/man2/syscall.2.html

       arch/ABI   instruction          syscall #   retval Notes
       -----------------------------------------------------------------------------------
       arm/EABI   swi 0x0              r7          r0

       arch/ABI   arg1   arg2   arg3   arg4   arg5   arg6   arg7
       ----------------------------------------------------------
       arm/EABI   r0     r1     r2     r3     r4     r5     r6


Syscall numbers from linux/arch/arm/kernel/calls.S

0x0001 sys_exit		void exit(int status)
0x0002 sys_fork		pid_t fork(void)
0x0003 sys_read		ssize_t read(int fd, void *buf, size_t count)
0x0004 sys_write	ssize_t write(int fd, const void *buf, size_t count)
0x0005 sys_open 	int open(const char *pathname, int flags, mode_t mode);
0x0006 sys_close	int close(int fd)
...
0x000B sys_execve	int execve(const char *filename, char *const argv[], char *const envp[])
...
0x003f sys_dup2		int dup2(int oldfd, int newfd)
0x0119 sys_socket 	int socket(int domain, int type, int protocol);
0x011A sys_bind		int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
0x011B sys_connect	int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
0x011C sys_listen
0x011D sys_accept
...
0x0121 sys_send
0x0122 sys_sendto
0x0123 sys_recv
0x0124 sys_recvfrom
0x0125 sys_shutdown