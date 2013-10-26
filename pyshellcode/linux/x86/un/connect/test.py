#!/usr/bin/python

import shellcode
from testing import testing
import subprocess

def test():
	port = 1111
	command = ["/bin/uname", "-i", "-o"]
	sc = shellcode.connect("127.0.0.1", port)
	sc += shellcode.helloworld()
	testing.run_tcp_expect_recv_data(sc, "Hello World!\n", port)
	sc = shellcode.connect("127.0.0.1", port)
	sc += shellcode.execve_sh()
	expect = subprocess.check_output(command)
	testing.run_tcp_expect_recv_data_using_send_data(sc, expect, port, "uname -i -o\nexit\n")


if __name__ == "__main__":
	test()

