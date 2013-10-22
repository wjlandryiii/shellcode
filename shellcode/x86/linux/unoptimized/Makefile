BUILDSCRIPTSDIR=../../../../build_scripts/
SRCDIR=src
OBJDIR=obj
ELFDIR=elf
BINDIR=bin
PYDIR=py

SOURCES = $(notdir $(wildcard src/*.s))
PYSOURCES = $(wildcard src/*.py)

SRCS=$(addprefix $(SRCDIR)/,$(SOURCES))
OBJS=$(addprefix $(OBJDIR)/,$(SOURCES:.s=.o))
ELFS=$(addprefix $(ELFDIR)/,$(SOURCES:.s=.elf))
BINS=$(addprefix $(BINDIR)/,$(SOURCES:.s=.bin))
PYS=$(addprefix $(PYDIR)/,$(SOURCES:.s=.py))

TESTS=$(notdir $(basename $(wildcard test/*.py)))

all: $(OBJS) $(ELFS) $(BINS) $(PYS) shellcode.py

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
	$(BUILDSCRIPTSDIR)/bin2py.py $(notdir $(basename $@))_shellcode $< $@

shellcode.py:
	echo \#!/usr/bin/python > shellcode.py
	echo >> shellcode.py
	echo \# uname -a: >>shellcode.py
	uname -a | sed  "s/^\([^\#]\)/# \1/g" >> shellcode.py
	echo >> shellcode.py
	echo \# assembler: >> shellcode.py
	as --version | sed  "s/^\([^\#]\)/# \1/g" >> shellcode.py
	echo >> shellcode.py
	cat $(PYS) >> shellcode.py
	cat $(PYSOURCES) >> shellcode.py

test: test/runsc $(TESTS)

$(TESTS):
	python -m test.$@

test/runsc:
	make -C test all

.PHONY: clean
clean:
	rm -f $(OBJDIR)/*
	rm -f $(ELFDIR)/*
	rm -f $(BINDIR)/*
	rm -f $(PYDIR)/*
	rm -f shellcode.py
	make -C test clean

