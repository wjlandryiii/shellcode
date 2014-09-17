CC=cc
CFLAGS=
AS=as
ASFLAGS=
LD=ld
LDFLAGS=

all: connect.bin \
	execve.bin \
	execve_sh.bin \
	exit.bin \
	helloworld.bin \
	ok.bin \
	readfile.bin \
	reusefd.bin \
	stage.bin \
	tests

connect.bin: connect.exe
	objcopy -O binary --only-section=.text $< $@
connect.exe: connect.o
	$(LD) -o $@ $^ $(LDFLAGS)
connect.o: connect.s
	$(AS) -o $@ $< $(ASFLAGS)
execve.bin: execve.exe
	objcopy -O binary --only-section=.text $< $@
execve.exe: execve.o
	$(LD) -o $@ $^ $(LDFLAGS)
execve.o: execve.s
	$(AS) -o $@ $< $(ASFLAGS)
execve_sh.bin: execve_sh.exe
	objcopy -O binary --only-section=.text $< $@
execve_sh.exe: execve_sh.o
	$(LD) -o $@ $^ $(LDFLAGS)
execve_sh.o: execve_sh.s
	$(AS) -o $@ $< $(ASFLAGS)
exit.bin: exit.exe
	objcopy -O binary --only-section=.text $< $@
exit.exe: exit.o
	$(LD) -o $@ $^ $(LDFLAGS)
exit.o: exit.s
	$(AS) -o $@ $< $(ASFLAGS)
helloworld.bin: helloworld.exe
	objcopy -O binary --only-section=.text $< $@
helloworld.exe: helloworld.o
	$(LD) -o $@ $^ $(LDFLAGS)
helloworld.o: helloworld.s
	$(AS) -o $@ $< $(ASFLAGS)
ok.bin: ok.exe
	objcopy -O binary --only-section=.text $< $@
ok.exe: ok.o
	$(LD) -o $@ $^ $(LDFLAGS)
ok.o: ok.s
	$(AS) -o $@ $< $(ASFLAGS)
readfile.bin: readfile.exe
	objcopy -O binary --only-section=.text $< $@
readfile.exe: readfile.o
	$(LD) -o $@ $^ $(LDFLAGS)
readfile.o: readfile.s
	$(AS) -o $@ $< $(ASFLAGS)
reusefd.bin: reusefd.exe
	objcopy -O binary --only-section=.text $< $@
reusefd.exe: reusefd.o
	$(LD) -o $@ $^ $(LDFLAGS)
reusefd.o: reusefd.s
	$(AS) -o $@ $< $(ASFLAGS)
stage.bin: stage.exe
	objcopy -O binary --only-section=.text $< $@
stage.exe: stage.o
	$(LD) -o $@ $^ $(LDFLAGS)
stage.o: stage.s
	$(AS) -o $@ $< $(ASFLAGS)


tests:	tests/test_execve_sh.exe \
	tests/test_exit.exe \
	tests/test_helloworld.exe \
	tests/test_ok.exe \
	tests/test_readfile.exe \
	tests/test_stage.exe

tests/runner.o: tests/runner.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)
tests/test_execve_sh.exe: tests/test_execve_sh.o tests/runner.o
	$(CC) -o $@ $^
tests/test_execve_sh.o: tests/test_execve_sh.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)
tests/test_exit.exe: tests/test_exit.o tests/runner.o
	$(CC) -o $@ $^
tests/test_exit.o: tests/test_exit.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)
tests/test_helloworld.exe: tests/test_helloworld.o tests/runner.o
	$(CC) -o $@ $^
tests/test_helloworld.o: tests/test_helloworld.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)
tests/test_ok.exe: tests/test_ok.o tests/runner.o
	$(CC) -o $@ $^
tests/test_ok.o: tests/test_ok.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)
tests/test_readfile.exe: tests/test_readfile.o tests/runner.o
	$(CC) -o $@ $^
tests/test_readfile.o: tests/test_readfile.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)
tests/test_stage.exe: tests/test_stage.o tests/runner.o
	$(CC) -o $@ $^
tests/test_stage.o: tests/test_stage.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)



.PHONY: test
test: all
	tests/test_execve_sh.exe execve_sh.bin
	tests/test_helloworld.exe helloworld.bin
	tests/test_ok.exe ok.bin
	tests/test_readfile.exe readfile.bin
	tests/test_stage.exe stage.bin ok.bin

.PHONY: clean
clean:
	rm -f *.o
	rm -f *.exe
	rm -f *.bin
	rm -f tests/*.o
	rm -f tests/*.exe
