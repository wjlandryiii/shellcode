
def readfile(filename):
	params = filename + "\x00"
	return readfile_shellcode[:-(len("readfile.s\x00"))] + params

