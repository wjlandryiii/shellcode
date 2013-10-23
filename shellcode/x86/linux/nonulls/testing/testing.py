#!/usr/bin/python

import os
import sys
import subprocess
import socket
import time

def get_output(sc):
	sc_bin = "sc.bin"
	f = open(sc_bin, "wb")
	f.write(sc)
	f.close()
	output = subprocess.check_output(["testing/runsc", sc_bin])
	os.remove(sc_bin)
	return output

def get_output_using_input(sc, input):
	sc_bin = "sc.bin"
	f = open(sc_bin, "wb")
	f.write(sc)
	f.close()
	p = subprocess.Popen(["testing/runsc", sc_bin], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	outp = p.communicate(input)[0]
	os.remove(sc_bin)
	return outp

def get_exitcode(sc):
	sc_bin = "sc.bin"
	f = open(sc_bin, "wb")
	f.write(sc)
	f.close()
	exit_code = subprocess.call(["testing/runsc", sc_bin])
	os.remove(sc_bin)
	return exit_code

def get_tcp_serv_recv_data(sc, port):
	sc_bin = "sc.bin"
	f = open(sc_bin, "wb")
	f.write(sc)
	f.close()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('', port))
	s.listen(5)
	s.settimeout(5.0)
	subprocess.Popen(["testing/runsc", sc_bin])
	try:
		conn, addr = s.accept()
		recv_data = ""
		d = conn.recv(1024)
		while(len(d) > 0):
			recv_data += d
			d = conn.recv(1024)
		os.remove(sc_bin)
		return recv_data
	except socket.timeout:
		print "socket timed out!"
		sys.exit(1)

def get_tcp_serv_recv_data_using_send_data(sc, port, send_data):
	sc_bin = "sc.bin"
	f = open(sc_bin, "wb")
	f.write(sc)
	f.close()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('', port))
	s.listen(5)
	s.settimeout(5.0)
	subprocess.Popen(["testing/runsc", sc_bin])
	try:
		conn, addr = s.accept()
		conn.sendall(send_data)
		recv_data = ""
		d = conn.recv(1024)
		while(len(d) > 0):
			recv_data += d
			d = conn.recv(1024)
		os.remove(sc_bin)
		return recv_data
	except socket.timeout:
		print "socket timed out!"
		sys.exit(1)

def get_tcp_client_recv_data(sc, ip, port, sock_fd):
	sc_bin = "sc.bin"
	f = open(sc_bin, "wb")
	f.write(sc)
	f.close()
	subprocess.Popen(["testing/runsc", "-l", str(port), str(sock_fd), sc_bin])
	time.sleep(1.0) # give runsc time to listen
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	recv_data = ""
	d = s.recv(1024)
	while(len(d) > 0):
		recv_data += d
		d = s.recv(1024)
	os.remove(sc_bin)
	return recv_data

def get_tcp_client_recv_data_using_send_data(sc, ip, port, sock_fd, send_data):
	sc_bin = "sc.bin"
	f = open(sc_bin, "wb")
	f.write(sc)
	f.close()
	subprocess.Popen(["testing/runsc", "-l", str(port), str(sock_fd), sc_bin])
	time.sleep(1.0) # give runsc time to listen
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	s.sendall(send_data)
	recv_data = ""
	d = s.recv(1024)
	while(len(d) > 0):
		recv_data += d
		d = s.recv(1024)
	os.remove(sc_bin)
	return recv_data


def run_expecting_output(sc, expected_output):
	output = get_output(sc)
	if(expected_output != output):
		print "Expected output: %s" % (expected_output)
		print "Got output: %s" % (output)
		sys.exit(1)

def run_expecting_exit_code(sc, expected_exit_code):
	exit_code = get_exitcode(sc)
	if(expected_exit_code != exit_code):
		print "Expected exit code: ", expected_exit_code
		print "Got exit code: ", exit_code
		sys.exit(1)

def run_expecting_output_using_input(sc, expected_output, input):
	output = get_output_using_input(sc, input)
	if(expected_output != output):
		print "Expected output: ", expected_output
		print "Got output: ", output
		sys.exit(1)

def run_tcp_expect_recv_data(sc, expected_recv_data, port):
	recv_data = get_tcp_serv_recv_data(sc, port)
	if(recv_data != expected_recv_data):
		print "Expected recv: ", expected_recv_data
		print "Got recv: ", recv_data
		sys.exit(1)

def run_tcp_expect_recv_data_using_send_data(sc, expected_recv_data, port, send_data):
	recv_data = get_tcp_serv_recv_data_using_send_data(sc, port, send_data)
	if(recv_data != expected_recv_data):
		print "Expected recv: ", expected_recv_data
		print "Got recv: ", recv_data
		sys.exit(1)

def run_tcp_client_expect_recv_data(sc, ip, port, sock_fd, expected_recv_data):
	recv_data = get_tcp_client_recv_data(sc, ip, port, sock_fd)
	if(recv_data != expected_recv_data):
		print "Expected recv: ", expected_recv_data
		print "Got recv: ", recv_data
		sys.exit(1)

def run_tcp_client_expect_recv_data_using_send_data(sc, ip, port, sock_fd, expected_recv_data, send_data):
	recv_data = get_tcp_client_recv_data_using_send_data(sc, ip, port, sock_fd, send_data)
	if(recv_data != expected_recv_data):
		print "Expected recv: ", expected_recv_data
		print "Got recv: ", recv_data
		sys.exit(1)

def verify_no_nulls(sc):
	if(sc.find("\x00") != -1):
		print "Shell code contains NULLS"
		sys.exit(1)

