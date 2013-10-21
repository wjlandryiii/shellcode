SOURCES = connect.s execve.s execve_sh.s exit.s helloworld.s readfile.s

SRCS=$(addprefix src/,$(SOURCES))
OBJS=$(addprefix obj/,$(SOURCES:.s=.o))
ELFS=$(addprefix elf/,$(SOURCES:.s=.elf))
BINS=$(addprefix bin/,$(SOURCES:.s=.bin))

all: $(OBJS) $(ELFS) $(BINS)

obj/%.o: src/%.s
	as -o $@ $<

elf/%.elf: obj/%.o
	ld -o $@ $<

bin/%.bin: elf/%.elf
	objcopy -O binary --only-section=.text $< $@

.PHONY : clean
clean:
	rm obj/*
	rm elf/*
	rm bin/*
