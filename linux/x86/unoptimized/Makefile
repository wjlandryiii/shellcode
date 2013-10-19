all: elfs bins

elfs: exit

bins: exit.bin

exit.bin: exit.o
	ld --oformat binary -o exit.bin exit.o

exit: exit.o
	ld -o exit exit.o

exit.o: exit.s
	as -o exit.o exit.s
