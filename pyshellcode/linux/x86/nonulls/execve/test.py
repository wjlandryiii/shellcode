#!/usr/bin/python

import shellcode
from testing import testing
import subprocess
import os
import sys

def test():
	command = ["/bin/uname", "-s", "-n", "-r", "-v", "-m", "-p", "-i", "-o"]
	sc = shellcode.execve(command)
	expect = subprocess.check_output(command)
	testing.verify_no_nulls(sc)
	testing.run_expecting_output(sc, expect)


if __name__ == "__main__":
	test()
