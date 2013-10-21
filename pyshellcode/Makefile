
BUILD_SCRIPTS_DIR=../build_scripts

all: pyshellcode.py

pyshellcode.py: shellcode_db.py pyshellcode_stub.py
	cat py/shellcode_db.py src/pyshellcode_stub.py > py/pyshellcode.py

shellcode_db.py:
	make_shellcode_db.py > py/shellcode_db.py
