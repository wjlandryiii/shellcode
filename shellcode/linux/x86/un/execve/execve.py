from asm.execve import execve_shellcode

def execve(parameter_list):
	params = ""
	for x in reversed(parameter_list):
		params += x + "\x00"
	params += "\x00"
	return execve_shellcode[:-(len("-a\x00/bin/uname\x00\x00"))] + params
