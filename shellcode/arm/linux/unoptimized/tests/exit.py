#!/usr/bin/python

import shellcode
from testing import testing
import subprocess
import os
import sys

def test():
	sc = shellcode.exit()
	testing.run_expecting_exit_code(sc, 0)


if __name__ == "__main__":
	test()


