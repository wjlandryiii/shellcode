LD=gcc
CC=gcc
LDFLAGS=-lc
CFLAGS=-g -O0

all: test_execve_sh runsc test_ok

test_ok: test_ok.o runner.o
	$(LD) -o $@ $^ $(LDFLAGS)

test_ok.o: test_ok.c runner.h
	$(CC) -c -o $@ $< $(CFLAGS)

runner.o: runner.c runner.h
	$(CC) -c -o $@ $< $(CFLAGS)


test_execve_sh: test_execve_sh.o
	$(LD) -o $@ $< $(LDFLAGS)

test_execve_sh.o: test_execve_sh.c
	$(CC) -c -o $@ $< $(CFLAGS)

runsc: runsc.o
	$(LD) -o $@ $< $(LDFLAGS)

runsc.o: runsc.c
	$(CC) -c -o $@ $< $(CFLAGS)

.PHONY: clean

clean:
	rm -f *.o
	rm -f test_execve_sh
