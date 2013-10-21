
BUILDSCRIPTSDIR=../build_scripts
SHELLCODEDIR=../shellcode

all: pyshellcode.py

pyshellcode.py: py/shellcode_db.py src/pyshellcode_stub.py
	cat py/shellcode_db.py src/pyshellcode_stub.py > pyshellcode.py

py/shellcode_db.py:
	$(BUILDSCRIPTSDIR)/make_shellcode_db.py $(SHELLCODEDIR) > py/shellcode_db.py

.PHONY : clean py/shellcode_db.py
clean:
	rm -f py/*