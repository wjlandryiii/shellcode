#!/usr/bin/python

import shellcode
import subprocess
import os
import sys

def helloworld():
	shellcode_file = "shellcode.bin"
	f = open(shellcode_file, "wb")
	f.write(shellcode.helloworld())
	f.close()
	output = subprocess.check_output(["test/runsc", "shellcode.bin"])
	os.remove(shellcode_file)
	return output


if __name__ == "__main__":
	if(helloworld() != "Hello World!\n"):
		import sys
		sys.exit(-1)


