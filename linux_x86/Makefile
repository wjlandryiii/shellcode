CC=cc
CFLAGS=-m32 -nostdlib
GENPY=../binpygen/bingen.py

all: 	exefiles \
	connect.bin \
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
	hexdump.bin \
	jmpesp.bin \
	ok.bin \
	readfile.bin \
	readfile_nz.bin \
	reusefd.bin \
	reusefd_findip.bin \
	stage.bin

exefiles: 	connect.exe \
	connect_execve.exe \
	connect_sh.exe \
	execve.exe \
	execve_small.exe \
	execve_sh.exe \
	execve_sh_nz.exe \
	exit.exe \
	getsetuid_frag.exe \
	getsetuid_nz_frag.exe \
	helloworld.exe \
	hexdump.exe \
	jmpesp.exe \
	ok.exe \
	readfile.exe \
	readfile_nz.exe \
	reusefd.exe \
	reusefd_findip.exe \
	stage.exe

%.exe: %.s
	$(CC) $(CFLAGS) -o $@ $<

%.bin: %.exe
	objcopy -O binary --only-section=.text $< $@

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

%.py: %.bin
	$(GENPY) -o $@ $<

.PHONY: clean

clean:
	rm -f *.exe
	rm -f *.bin
	rm -f *.o
