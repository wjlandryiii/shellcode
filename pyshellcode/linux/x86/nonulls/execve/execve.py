from execve_shellcode import execve_shellcode

def execve(parameter_list):
	params = ""
	for x in reversed(parameter_list):
		params += x + "\xFF"
	params += "\xFF"
	return execve_shellcode[:-(len("-a\x00/bin/uname\x00\x00"))] + params
