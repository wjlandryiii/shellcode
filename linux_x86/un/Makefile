AS=as
ASFLAGS=
LD=ld
LDFLAGS=

all: helloworld.bin exit.bin connect.bin execve.bin execve_sh.bin readfile.bin reusefd.bin stage.bin ok.bin

ok.bin: ok
	objcopy -O binary --only-section=.text $< $@

ok: ok.o
	$(LD) -o $@ $< $(LDFLAGS)

ok.o: ok.s
	$(AS) -o $@ $<


stage.bin: stage
	objcopy -O binary --only-section=.text $< $@

stage: stage.o
	$(LD) -o $@ $<

stage.o: stage.s
	$(AS) -o $@ $<

helloworld.bin: helloworld
	objcopy -O binary --only-section=.text $< $@

helloworld: helloworld.o
	$(LD) -o $@ $<

helloworld.o: helloworld.s
	$(AS) -o $@ $<

exit.bin: exit
	objcopy -O binary --only-section=.text $< $@

exit: exit.o
	$(LD) -o $@ $<

exit.o: exit.s
	$(AS) -o $@ $<

connect.bin: connect
	objcopy -O binary --only-section=.text $< $@

connect: connect.o
	$(LD) -o $@ $<

connect.o: connect.s
	$(AS) -o $@ $<

execve.bin: execve
	objcopy -O binary --only-section=.text $< $@

execve: execve.o
	$(LD) -o $@ $<

execve.o: execve.s
	$(AS) -o $@ $<

execve_sh.bin: execve_sh
	objcopy -O binary --only-section=.text $< $@

execve_sh: execve_sh.o
	$(LD) -o $@ $<

execve_sh.o: execve_sh.s
	$(AS) -o $@ $<

readfile.bin: readfile
	objcopy -O binary --only-section=.text $< $@

readfile: readfile.o
	$(LD) -o $@ $<

readfile.o: readfile.s
	$(AS) -o $@ $<

reusefd.bin: reusefd
	objcopy -O binary --only-section=.text $< $@

reusefd: reusefd.o
	$(LD) -o $@ $<

reusefd.o: reusefd.s
	$(AS) -o $@ $<

.PHONY: clean

clean:
	rm -f *.bin
	rm -f *.o
	rm -f helloworld
	rm -f exit
	rm -f connect
	rm -f execve
	rm -f execve_sh
	rm -f readfile
	rm -f reusefd
	rm -f stage
	rm -f ok
