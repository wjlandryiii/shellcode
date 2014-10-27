#!/usr/bin/python

import urllib
import socket

def my_ip_public():
	return urllib.urlopen("http://wtfismyip.com/text").read().strip()

def my_ip_local():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("www.google.com", 80))
	local_ip = s.getsockname()[0]
	s.close()
	return local_ip

def my_ip(public = True):
	if(public):
		return my_ip_public()
	return my_ip_local()

if __name__ == "__main__":
	import sys
	if(len(sys.argv) < 2):
		print my_ip()
	else:
		if(sys.argv[1].upper() == "PUBLIC"):
			print my_ip_public()
		elif(sys.argv[1].upper() == "LOCAL"):
			print my_ip_local()
		else:
			print "Usage: %s [public | private]" % (sys.argv[0])

