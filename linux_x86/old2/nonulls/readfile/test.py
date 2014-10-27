#!/usr/bin/python

import shellcode
from testing import testing
import os


def test():
	key_file = "key.tmp"
	key = "The key is {150a09840a39aec42662e3b7dd006f830fec39fa0020f65ea884216903fc9e4b}\n"
	f = open(key_file, "w")
	f.write(key)
	f.close()
	sc = shellcode.readfile(key_file)
	testing.verify_no_nulls(sc)
	testing.run_expecting_output(sc, key)
	os.remove(key_file)

if __name__ == "__main__":
	test()

