LD=gcc
CC=gcc
LDFLAGS=-lc
CFLAGS=-g -O0

all: test_execve_sh test_ok test_helloworld

all: test_stage

test_stage: test_stage.o runner.o
	$(LD) -o $@ $^ $(LDFLAGS)

test_stage.o: test_stage.c runner.h
	$(CC) -c -o $@ $< $(CFLAGS)

all: test_readfile

test_readfile: test_readfile.o runner.o
	$(LD) -o $@ $^ $(LDFLAGS)

test_readfile.o: test_readfile.c runner.h
	$(CC) -c -o $@ $< $(CFLAGS)

all: test_exit

test_exit: test_exit.o runner.o
	$(LD) -o $@ $^ $(LDFLAGS)

test_exit.o: test_exit.c runner.h
	$(CC) -c -o $@ $< $(CFLAGS)

test_helloworld: test_helloworld.o runner.o
	$(LD) -o $@ $^ $(LDFLAGS)

test_helloworld.o: test_helloworld.c runner.h
	$(CC) -c -o $@ $< $(CCFLAGS)

test_ok: test_ok.o runner.o
	$(LD) -o $@ $^ $(LDFLAGS)

test_ok.o: test_ok.c runner.h
	$(CC) -c -o $@ $< $(CFLAGS)

runner.o: runner.c runner.h
	$(CC) -c -o $@ $< $(CFLAGS)


test_execve_sh: test_execve_sh.o runner.o
	$(LD) -o $@ $^ $(LDFLAGS)

test_execve_sh.o: test_execve_sh.c
	$(CC) -c -o $@ $< $(CFLAGS)


.PHONY: clean

clean:
	rm -f *.o
	rm -f test_execve_sh
	rm -f test_ok
	rm -f test_helloworld
	rm -f test_exit
	rm -f test_readfile
