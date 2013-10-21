SRCDIR=src
OBJDIR=obj
ELFDIR=elf
BINDIR=bin
PYDIR=py

SOURCES = $(notdir $(wildcard src/*.s))

SRCS=$(addprefix $(SRCDIR)/,$(SOURCES))
OBJS=$(addprefix $(OBJDIR)/,$(SOURCES:.s=.o))
ELFS=$(addprefix $(ELFDIR)/,$(SOURCES:.s=.elf))
BINS=$(addprefix $(BINDIR)/,$(SOURCES:.s=.bin))
PYS=$(addprefix $(PYDIR)/,$(SOURCES:.s=.py))

all: $(OBJS) $(ELFS) $(BINS) $(PYS)

$(OBJS): | $(OBJDIR)
$(ELFS): | $(ELFDIR)
$(BINS): | $(BINDIR)
$(PYS): | $(PYDIR)

$(OBJDIR):
	mkdir -p obj
$(ELFDIR):
	mkdir -p elf
$(BINDIR):
	mkdir -p bin
$(PYDIR):
	mkdir -p py

$(OBJDIR)/%.o: $(SRCDIR)/%.s
	as -o $@ $<

$(ELFDIR)/%.elf: $(OBJDIR)/%.o
	ld -o $@ $<

$(BINDIR)/%.bin: $(ELFDIR)/%.elf
	objcopy -O binary --only-section=.text $< $@

$(PYDIR)/%.py: $(BINDIR)/%.bin
	../../../bin2py.py $(notdir $(basename $@))_shellcode $< $@

.PHONY : clean
clean:
	rm -f $(OBJDIR)/*
	rm -f $(ELFDIR)/*
	rm -f $(BINDIR)/*
	rm -f $(PYDIR)/*