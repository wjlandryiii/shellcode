all: elfs 
#bins

elfs: exit helloworld readfile execve_sh execve connect

#bins: helloworld.bin

exit: exit.o
	ld -o exit exit.o

exit.o: exit.s
	as -o exit.o exit.s

helloworld: helloworld.o
	ld -o helloworld helloworld.o

helloworld.o: helloworld.s
	as -o helloworld.o helloworld.s


readfile: readfile.o
	ld -o readfile readfile.o

readfile.o: readfile.s
	as -o readfile.o readfile.s

execve_sh: execve_sh.o
	ld -o execve_sh execve_sh.o

execve_sh.o: execve_sh.s
	as -o execve_sh.o execve_sh.s


execve: execve.o
	ld -o execve execve.o

execve.o: execve.s
	as -o execve.o execve.s

connect: connect.o
	ld -o connect connect.o

connect.o: connect.s
	as -o connect.o connect.s
