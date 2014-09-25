CC=cc
CFLAGS=
AS=as
ASFLAGS=
LD=ld
LDFLAGS=
GENPY=../../binpygen/bingen.py

all: 	connect.bin \
	connect_execve.bin \
	connect_sh.bin \
	execve.bin \
	execve_small.bin \
	execve_sh.bin \
	execve_sh_nz.bin \
	exit.bin \
	getsetuid_frag.bin \
	getsetuid_nz_frag.bin \
	helloworld.bin \
	jmpesp.bin \
	ok.bin \
	readfile.bin \
	readfile_nz.bin \
	reusefd.bin \
	reusefd_findip.bin \
	stage.bin \
	tests

connect.bin: connect.exe
	objcopy -O binary --only-section=.text $< $@
connect.exe: connect.o
	$(LD) -o $@ $^ $(LDFLAGS)
connect.o: connect.s
	$(AS) -o $@ $< $(ASFLAGS)
connect_execve.bin: connect_execve.exe
	objcopy -O binary --only-section=.text $< $@
connect_execve.exe: connect_execve.o
	$(LD) -o $@ $^ $(LDFLAGS)
connect_execve.o: connect_execve.s
	$(AS) -o $@ $< $(ASFLAGS)
connect_sh.bin: connect_sh.exe
	objcopy -O binary --only-section=.text $< $@
connect_sh.exe: connect_sh.o
	$(LD) -o $@ $^ $(LDFLAGS)
connect_sh.o: connect_sh.s
	$(AS) -o $@ $< $(ASFLAGS)
execve.bin: execve.exe
	objcopy -O binary --only-section=.text $< $@
execve.exe: execve.o
	$(LD) -o $@ $^ $(LDFLAGS)
execve.o: execve.s
	$(AS) -o $@ $< $(ASFLAGS)
execve_small.bin: execve_small.exe
	objcopy -O binary --only-section=.text $< $@
execve_small.exe: execve_small.o
	$(LD) -o $@ $^ $(LDFLAGS)
execve_small.o: execve_small.s
	$(AS) -o $@ $< $(ASFLAGS)
execve_sh.bin: execve_sh.exe
	objcopy -O binary --only-section=.text $< $@
execve_sh.exe: execve_sh.o
	$(LD) -o $@ $^ $(LDFLAGS)
execve_sh.o: execve_sh.s
	$(AS) -o $@ $< $(ASFLAGS)
execve_sh_nz.bin: execve_sh_nz.exe
	objcopy -O binary --only-section=.text $< $@
execve_sh_nz.exe: execve_sh_nz.o
	$(LD) -o $@ $^ $(LDFLAGS)
execve_sh_nz.o: execve_sh_nz.s
	$(AS) -o $@ $< $(ASFLAGS)
exit.bin: exit.exe
	objcopy -O binary --only-section=.text $< $@
exit.exe: exit.o
	$(LD) -o $@ $^ $(LDFLAGS)
exit.o: exit.s
	$(AS) -o $@ $< $(ASFLAGS)
getsetuid_frag.bin: getsetuid_frag.exe
	objcopy -O binary --only-section=.text $< $@
getsetuid_frag.exe: getsetuid_frag.o
	$(LD) -o $@ $^ $(LDFLAGS)
getsetuid_frag.o: getsetuid_frag.s
	$(AS) -o $@ $< $(ASFLAGS)
getsetuid_nz_frag.bin: getsetuid_nz_frag.exe
	objcopy -O binary --only-section=.text $< $@
getsetuid_nz_frag.exe: getsetuid_nz_frag.o
	$(LD) -o $@ $^ $(LDFLAGS)
getsetuid_nz_frag.o: getsetuid_nz_frag.s
	$(AS) -o $@ $< $(ASFLAGS)
helloworld.bin: helloworld.exe
	objcopy -O binary --only-section=.text $< $@
helloworld.exe: helloworld.o
	$(LD) -o $@ $^ $(LDFLAGS)
helloworld.o: helloworld.s
	$(AS) -o $@ $< $(ASFLAGS)
jmpesp.bin: jmpesp.exe
	objcopy -O binary --only-section=.text $< $@
jmpesp.exe: jmpesp.o
	$(LD) -o $@ $^ $(LDFLAGS)
jmpesp.o: jmpesp.s
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
readfile_nz.bin: readfile_nz.exe
	objcopy -O binary --only-section=.text $< $@
readfile_nz.exe: readfile_nz.o
	$(LD) -o $@ $^ $(LDFLAGS)
readfile_nz.o: readfile_nz.s
	$(AS) -o $@ $< $(ASFLAGS)
reusefd.bin: reusefd.exe
	objcopy -O binary --only-section=.text $< $@
reusefd.exe: reusefd.o
	$(LD) -o $@ $^ $(LDFLAGS)
reusefd.o: reusefd.s
	$(AS) -o $@ $< $(ASFLAGS)
reusefd_findip.bin: reusefd_findip.exe
	objcopy -O binary --only-section=.text $< $@
reusefd_findip.exe: reusefd_findip.o
	$(LD) -o $@ $^ $(LDFLAGS)
reusefd_findip.o: reusefd_findip.s
	$(AS) -o $@ $< $(ASFLAGS)
stage.bin: stage.exe
	objcopy -O binary --only-section=.text $< $@
stage.exe: stage.o
	$(LD) -o $@ $^ $(LDFLAGS)
stage.o: stage.s
	$(AS) -o $@ $< $(ASFLAGS)


tests:	tests/test_connect_sh.exe \
	tests/test_execve_sh.exe \
	tests/test_exit.exe \
	tests/test_helloworld.exe \
	tests/test_ok.exe \
	tests/test_readfile.exe \
	tests/test_reusefd_findip.exe \
	tests/test_stage.exe

tests/runner.o: tests/runner.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)
tests/test_connect_sh.exe: tests/test_connect_sh.o tests/runner.o
	$(CC) -o $@ $^
tests/test_connect_sh.o: tests/test_connect_sh.c tests/runner.h
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

tests/test_reusefd_findip.exe: tests/test_reusefd_findip.o tests/runner.o
	$(CC) -o $@ $^
tests/test_reusefd_findip.o: tests/test_reusefd_findip.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)

tests/test_stage.exe: tests/test_stage.o tests/runner.o
	$(CC) -o $@ $^
tests/test_stage.o: tests/test_stage.c tests/runner.h
	$(CC) -c -o $@ $< $(CFLAGS)



.PHONY: test
test: all
	tests/test_connect_sh.exe connect_sh.bin
	tests/test_connect_sh.exe connect_execve.bin
	tests/test_execve_sh.exe execve.bin
	tests/test_execve_sh.exe execve_small.bin
	tests/test_execve_sh.exe execve_sh.bin
	tests/test_helloworld.exe helloworld.bin
	tests/test_ok.exe ok.bin
	tests/test_readfile.exe readfile.bin
	tests/test_readfile.exe readfile_nz.bin
	tests/test_reusefd_findip.exe reusefd_findip.bin
	tests/test_stage.exe stage.bin ok.bin


pygen: 	connect.py \
	connect_execve.py \
	connect_sh.py \
	execve.py \
	execve_small.py \
	execve_sh.py \
	execve_sh_nz.py \
	getsetuid_frag.py \
	getsetuid_nz_frag.py \
	helloworld.py \
	jmpesp.py \
	ok.py \
	readfile.py \
	readfile_nz.py \
	reusefd.py \
	reusefd_findip.py \
	stage.py

connect.py: connect.bin connect.types
	$(GENPY) -t connect.types -o $@ $<
connect_execve.py: connect_execve.bin connect_execve.types
	$(GENPY) -t connect_execve.types -o $@ $<
connect_sh.py: connect_sh.bin connect_sh.types
	$(GENPY) -t connect_sh.types -o $@ $<
execve.py: execve.bin execve.types
	$(GENPY) -t execve.types -o $@ $<
execve_small.py: execve_small.bin execve_small.types
	$(GENPY) -t execve_small.types -o $@ $<
execve_sh.py: execve_sh.bin execve_sh.types
	$(GENPY) -t execve_sh.types -o $@ $<
execve_sh_nz.py: execve_sh_nz.bin
	$(GENPY) -o $@ $<
getsetuid_frag.py: getsetuid_frag.bin
	$(GENPY) -o $@ $<
getsetuid_nz_frag.py: getsetuid_nz_frag.bin
	$(GENPY) -o $@ $<
helloworld.py: helloworld.bin helloworld.types
	$(GENPY) -t helloworld.types -o $@ $<
jmpesp.py: jmpesp.bin
	$(GENPY) -o $@ $<
ok.py: ok.bin
	$(GENPY) -o $@ $<
readfile.py: readfile.bin readfile.types
	$(GENPY) -t readfile.types -o $@ $<
readfile_nz.py: readfile_nz.bin readfile_nz.types
	$(GENPY) -t readfile_nz.types -o $@ $<
reusefd.py: reusefd.bin reusefd.types
	$(GENPY) -t reusefd.types -o $@ $<
reusefd_findip.py: reusefd_findip.bin reusefd_findip.types
	$(GENPY) -t reusefd_findip.types -o $@ $<
stage.py: stage.bin
	$(GENPY) -o $@ $<

.PHONY: clean
clean:
	rm -f *.o
	rm -f *.exe
	rm -f *.bin
	rm -f tests/*.o
	rm -f tests/*.exe
