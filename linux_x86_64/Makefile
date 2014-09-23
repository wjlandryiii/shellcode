AS=as
ASFLAGS=
LD=ld
LDFLAGS=
PYGEN=../binpygen/bingen.py

all:	execve.bin \
	execve_sh.bin \
	execve_sh_nz.bin \
	exit.bin \
	helloworld.bin \
	ok.bin

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
ok.bin: ok.exe
	objcopy -O binary --only-section=.text $< $@
ok.exe: ok.o
	$(LD) -o $@ $^ $(LDFLAGS)
ok.o: ok.s
	$(AS) -o $@ $< $(ASFLAGS)
helloworld.bin: helloworld.exe
	objcopy -O binary --only-section=.text $< $@
helloworld.exe: helloworld.o
	$(LD) -o $@ $^ $(LDFLAGS)
helloworld.o: helloworld.s
	$(AS) -o $@ $< $(ASFLAGS)

pygen:	execve.py \
	execve_sh.py \
	execve_sh_nz.py \
	helloworld.py \
	ok.py

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

.PHONY: clean

clean:
	rm -r *.o
	rm -r *.exe
	rm -r *.bin
