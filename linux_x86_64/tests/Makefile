CFLAGS=-g -O0

all: test

test: main.o runsc.o mock.o tests.o
	gcc -o $@ $^

main.o: main.c runsc.h mock.h tests.h
	gcc $(CFLAGS) -c -o $@ $<

runsc.o: runsc.c
	gcc $(CFLAGS) -c -o $@ $<

mock.o: mock.c mock.h
	gcc $(CFLAGS) -c -o $@ $<

tests.o: tests.c tests.h
	gcc $(CFLAGS) -c -o $@ $<

.PHONY:	testtest

testtest: test
	./test -m -t exit0
	./test -m -t ok
	./test -m -t sh
	./test -m -t readfile

.PHONY: clean

clean:
	rm -f test
