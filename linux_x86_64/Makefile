AS=as
ASFLAGS=
LD=ld
LDFLAGS=
PYGEN=../binpygen/bingen.py

all:	execve.bin \
	execve_sh.bin \
	exit.bin

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

pygen:	execve.py \
	execve_sh.py

execve.py: execve.bin execve.types
	$(PYGEN) -t execve.types -o $@ $<
execve_sh.py: execve_sh.bin execve_sh.types
	$(PYGEN) -t execve_sh.types -o $@ $<



.PHONY: clean

clean:
	rm -r *.o
	rm -r *.exe
	rm -r *.bin
