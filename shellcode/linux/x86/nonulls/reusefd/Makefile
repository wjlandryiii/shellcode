OS=$(notdir $(shell readlink -f ../../../))
ARCH=$(notdir $(shell readlink -f ../../))
OPTIMIZATION=$(notdir $(shell readlink -f ../))
METHOD=$(notdir $(shell pwd))
BUILDDIR=build

all: $(BUILDDIR) $(METHOD)_shellcode.py

$(BUILDDIR):
	mkdir -p $(BUILDDIR)

$(METHOD)_shellcode.py: $(BUILDDIR)/$(METHOD).bin
	python -m shellcode.bin2py $(METHOD)_shellcode $< $@

$(BUILDDIR)/$(METHOD).bin: $(BUILDDIR)/$(METHOD).elf
	objcopy -O binary --only-section=.text $< $@

$(BUILDDIR)/$(METHOD).elf: $(BUILDDIR)/$(METHOD).o
	ld -o $@ $<

$(BUILDDIR)/$(METHOD).o: $(METHOD).s
	as -o $@ $<

.PHONY: test

test:
	python -m shellcode.$(OS).$(ARCH).$(OPTIMIZATION).$(METHOD).test


.PHONY: clean

clean:
	rm -f $(BUILDDIR)/$(METHOD).bin
	rm -f $(BUILDDIR)/$(METHOD).elf
	rm -f $(BUILDDIR)/$(METHOD).o
	rm -f $(METHOD)_shellcode.py