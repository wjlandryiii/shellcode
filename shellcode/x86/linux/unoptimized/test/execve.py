#!/usr/bin/python

import shellcode
import subprocess
import os
import sys

def test():
	shellcode_file = "shellcode.bin"
	f = open(shellcode_file, "wb")
	f.write(shellcode.execve(("/bin/uname", "-s", "-n", "-r", "-v", "-m", "-p", "-i", "-o")))
	f.close()
	output = subprocess.check_output(["test/runsc", "shellcode.bin"])
	os.remove(shellcode_file)
	return output


if __name__ == "__main__":
	if(test() != subprocess.check_output(["/bin/uname", "-s", "-n", "-r", "-v", "-m", "-p", "-i", "-o"])):
		sys.exit(-1)
	if(test() == subprocess.check_output(["/bin/uname"])):
		sys.exit(-1)
