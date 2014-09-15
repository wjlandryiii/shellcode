from reusefd_shellcode import reusefd_shellcode

def reusefd(fd):
	import struct
	params = struct.pack("<I", int(fd))
	return reusefd_shellcode.replace("\x05\x00\x00\x00", params)

