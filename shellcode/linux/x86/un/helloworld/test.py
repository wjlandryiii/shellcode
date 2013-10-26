#!/usr/bin/python

import helloworld
from shellcode import testing


def test():
	sc = helloworld.helloworld()
	testing.run_expecting_output(sc, "Hello World!\n")	

if __name__ == "__main__":
	test()

