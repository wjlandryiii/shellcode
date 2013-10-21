SOURCES = connect.s execve.s execve_sh.s exit.s helloworld.s readfile.s

SRCS=$(addprefix src/,$(SOURCES))
OBJS=$(addprefix obj/,$(SOURCES:.s=.o))
ELFS=$(addprefix elf/,$(SOURCES:.s=.elf))
BINS=$(addprefix bin/,$(SOURCES:.s=.bin))
PYS=$(addprefix py/,$(SOURCES:.s=.py))

all: $(OBJS) $(ELFS) $(BINS) $(PYS)

obj/%.o: src/%.s
	as -o $@ $<

elf/%.elf: obj/%.o
	ld -o $@ $<

bin/%.bin: elf/%.elf
	objcopy -O binary --only-section=.text $< $@

py/%.py: bin/%.bin
	../../../bin2py.py $(notdir $(basename $@))_shellcode $< $@



.PHONY : clean
clean:
	rm -f obj/*
	rm -f elf/*
	rm -f bin/*
	rm -f py/*