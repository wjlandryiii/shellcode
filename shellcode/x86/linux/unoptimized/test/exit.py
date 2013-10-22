#!/usr/bin/python

import shellcode
import subprocess
import os
import sys

def exit():
	shellcode_file = "shellcode.bin"
	f = open(shellcode_file, "wb")
	f.write(shellcode.exit())
	f.close()
	output = subprocess.call(["test/runsc", "shellcode.bin"])
	os.remove(shellcode_file)
	return output


if __name__ == "__main__":
	if(exit() != 0):
		import sys
		sys.exit(-1)


