helloworld_shellcode = ""
helloworld_shellcode += "\xeb\x31\x5e\x89\xf0\x51\x89\xc1\x80\x39\x00\x74\x05\x83\xc1\x01"
helloworld_shellcode += "\xeb\xf6\x29\xc1\x89\xc8\x59\x89\xc2\x89\xf1\xbb\x01\x00\x00\x00"
helloworld_shellcode += "\xb8\x04\x00\x00\x00\xcd\x80\xbb\x00\x00\x00\x00\xb8\x01\x00\x00"
helloworld_shellcode += "\x00\xcd\x80\xe8\xca\xff\xff\xff\x48\x65\x6c\x6c\x6f\x20\x57\x6f"
helloworld_shellcode += "\x72\x6c\x64\x21\x0a\x00"
