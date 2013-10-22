#!/usr/bin/python

import shellcode
from testing import testing
import subprocess

def test():
	command = ["/bin/uname", "-i", "-o"]
	sc = shellcode.execve_sh()
	expect = subprocess.check_output(command)
	testing.run_expecting_output_using_input(sc, expect, "uname -i -o\nexit\n")


if __name__ == "__main__":
	test()
