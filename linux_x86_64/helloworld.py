shellcode = ""
shellcode += "\x48\x8D\x35\x26\x00\x00\x00\x48\x31\xD2\x80\x3C\x16\x00\x74\x05"
shellcode += "\x48\xFF\xC2\xEB\xF5\x48\x31\xFF\x48\xFF\xC7\x48\x31\xC0\xB0\x01"
shellcode += "\x0F\x05\x48\x31\xFF\x48\x31\xC0\xB0\x3C\x0F\x05\xF4"
shellcode += "Hello World!\n\x00"
