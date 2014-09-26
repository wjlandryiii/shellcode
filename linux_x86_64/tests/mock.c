/*
 * Copyright 2014 Joseph Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void mock_exit0(void){
	exit(0);
}

void mock_ok(void){
	write(1, "OK\n", 3);
	exit(0);
}

void mock_sh(void){
	execl("/bin/sh", "sh", NULL);
	exit(1);
}

void mock_readfile(void){
	int fd;
	int bytes_read;
	int bytes_sent;
	char buff[1024];

	fd = open("/etc/passwd", 0);

	for(;;){
		bytes_read = read(fd, buff, sizeof(buff));
		if(bytes_read <= 0)
			break;
		write(1, buff, bytes_read);
	}
	close(fd);
	exit(0);
}
