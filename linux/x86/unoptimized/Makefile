all: elfs bins

elfs: exit execve_sh helloworld execve readfile connect

bins: exit.bin execve_sh.bin helloworld.bin execve.bin readfile.bin connect.bin

exit.bin: exit.o
	ld --oformat binary -o exit.bin exit.o

exit: exit.o
	ld -o exit exit.o

exit.o: exit.s
	as -o exit.o exit.s

execve_sh.bin: execve_sh.o
	ld --oformat binary -o execve_sh.bin execve_sh.o

execve_sh: execve_sh.o
	ld -o execve_sh execve_sh.o

execve_sh.o: execve_sh.s
	as -o execve_sh.o execve_sh.s

helloworld.bin: helloworld.o
	ld --oformat binary -o helloworld.bin helloworld.o

helloworld: helloworld.o
	ld -o helloworld helloworld.o

helloworld.o: helloworld.s
	as -o helloworld.o helloworld.s

execve.bin: execve.o
	ld --oformat binary -o execve.bin execve.o

execve: execve.o
	ld -o execve execve.o

execve.o: execve.s
	as -o execve.o execve.s

readfile.bin: readfile.o
	ld --oformat binary -o readfile.bin readfile.o

readfile: readfile.o
	ld -o readfile readfile.o

readfile.o: readfile.s
	as -o readfile.o readfile.s

connect.bin: connect.o
	ld --oformat binary -o connect.bin connect.o

connect: connect.o
	ld -o connect connect.o

connect.o: connect.s
	as -o connect.o connect.s

