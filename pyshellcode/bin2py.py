#!/usr/bin/python

def bin2py(sc, varname = "shellcode"):
	code = ""
	code += "%s = \"\"\n" % (varname)
	for i in range(0, len(sc), 16):
		line = sc[i:i+16]
		s = ""
		for x in line:
			s += "\\x%02x" % (ord(x))
		code += "%s += \"%s\"\n" % (varname, s)
	return code + "\n"

if __name__ == "__main__":
	import sys
	if(len(sys.argv) < 3):
		print "%s: [variable name] [binary file] [output file]" % (sys.argv[0])
		print "\tWill output to stdout if ouput file is not specified"
	else:
		f = open(sys.argv[2], "rb")
		code = bin2py(f.read(), sys.argv[1])
		f.close()
		if(len(sys.argv) == 3):
			print code
		else:
			f = open(sys.argv[3], "w")
			f.write(code)
			f.close
