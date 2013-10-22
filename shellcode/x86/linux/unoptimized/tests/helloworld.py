#!/usr/bin/python

import shellcode
from testing import testing


def test():
	sc = shellcode.helloworld()
	testing.run_expecting_output(sc, "Hello World!\n")	

if __name__ == "__main__":
	test()

