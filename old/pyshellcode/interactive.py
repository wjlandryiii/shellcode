import telnetlib

def interactive_mode(s):
	t = telnetlib.Telnet()
	t.sock = s
	print "Starting interactive mode"
	t.interact()