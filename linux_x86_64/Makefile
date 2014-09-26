AS=as
ASFLAGS=
LD=ld
LDFLAGS=
PYGEN=../binpygen/bingen.py

all:	connect.bin \
	connect_ok.bin \
	connect_sh.bin \
	execve.bin \
	execve_sh.bin \
	execve_sh_nz.bin \
	exit.bin \
	hcf.bin \
	helloworld.bin \
	ok.bin \
	readfile.bin \
	reusefd_sh.bin

connect.bin: connect.exe
	objcopy -O binary --only-section=.text $< $@
connect.exe: connect.o
	$(LD) -o $@ $^ $(LDFLAGS)
connect.o: connect.s
	$(AS) -o $@ $< $(ASFLAGS)
connect_ok.bin: connect_ok.exe
	objcopy -O binary --only-section=.text $< $@
connect_ok.exe: connect_ok.o
	$(LD) -o $@ $^ $(LDFLAGS)
connect_ok.o: connect_ok.s
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
hcf.bin: hcf.exe
	objcopy -O binary --only-section=.text $< $@
hcf.exe: hcf.o
	$(LD) -o $@ $^ $(LDFLAGS)
hcf.o: hcf.s
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
reusefd_sh.bin: reusefd_sh.exe
	objcopy -O binary --only-section=.text $< $@
reusefd_sh.exe: reusefd_sh.o
	$(LD) -o $@ $^ $(LDFLAGS)
reusefd_sh.o: reusefd_sh.s
	$(AS) -o $@ $< $(ASFLAGS)

pygen:	connect_ok.py \
	connect_sh.py \
	execve.py \
	execve_sh.py \
	execve_sh_nz.py \
	helloworld.py \
	ok.py \
	readfile.py \
	reusefd_sh.py

connect_ok.py: connect_ok.bin
	$(PYGEN) -o $@ $<
connect_sh.py: connect_sh.bin connect_sh.types
	$(PYGEN) -t connect_sh.types -o $@ $<
execve.py: execve.bin execve.types
	$(PYGEN) -t execve.types -o $@ $<
execve_sh.py: execve_sh.bin execve_sh.types
	$(PYGEN) -t execve_sh.types -o $@ $<
execve_sh_nz.py: execve_sh_nz.bin
	$(PYGEN) -o $@ $<
helloworld.py: helloworld.bin helloworld.types
	$(PYGEN) -t helloworld.types -o $@ $<
ok.py: ok.bin
	$(PYGEN) -o $@ $<
readfile.py: readfile.bin readfile.types
	$(PYGEN) -t readfile.types -o $@ $<
reusefd_sh.py: reusefd_sh.bin reusefd_sh.types
	$(PYGEN) -t reusefd_sh.types -o $@ $<

.PHONY: clean

clean:
	rm -r *.o
	rm -r *.exe
	rm -r *.bin
