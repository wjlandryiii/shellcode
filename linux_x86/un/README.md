Linux x86 Shellcode
===================


files
-----

###connect (fragment)
Established a connection to a TCP server, then falls through.

###connect_sh
Established a connection to a TCP server, redirects stdio to the socket,
then executes /bin/sh.

###connect_execve
Established a connection to a TCP server, redirects stdio to the socket, then
runs a program with command line arguments.

###connect_readfile
Established a connection to a TCP server, writes the contents of a file to
the socket, then exits.

###execve
Runs a program with command line arguments.

###execve_sh
A smaller version of execve that only executes /bin/sh.

###exit
Exits

###helloworld
Prints the string "Hello World!\n" to stdout then exits.

###ok
Prints the string "OK\n" to stdout then exits. Used for testing.

###readfile
Reads the contents of a file to stdout then exits.

###reusefd (fragment)
dup2() file descriptor 4 to 0,1,2 then falls through

###stage
reads 4k from stdin, then executes it.


Notes
-----

```
sycall table: arch/x86/syscalls/syscall_32.tbl
grep -r CONSTANT /usr/include
```
