/*
 * Copyright 2014 Joseph Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>

#include "runner.h"


void test_connect_sh(FILE *fin, FILE *fout, FILE *ferr, pid_t pid){
	char buff[64] = { 0 };
	int status;
	int fd;
	int fd_conn;
	struct sockaddr_in addr;
	int addrlen;
	FILE *f_sock;
	int y = 1;
	int fd_bind;

	fd_bind = bind_tcp(htonl(INADDR_ANY), htons(1234));

	assert(waitpid(pid, NULL, WSTOPPED) == pid);
	assert(kill(pid, SIGCONT) == 0);

	fd_conn = accept_tcp(fd_bind);

	assert((f_sock = fdopen(fd_conn, "r+")) != NULL);
	setlinebuf(f_sock);
	assert(fputs("uname\n", f_sock) != EOF);
	assert(fgets(buff, sizeof(buff), f_sock) != NULL);
	assert(strcmp(buff, "Linux\n") == 0);
	assert(fputs("exit\n", f_sock) != EOF);
	assert(fgetc(f_sock) == EOF);
	fclose(f_sock);
	close(fd);
	assert(fgetc(fout) == EOF);
	fclose(fout);
	assert(fgetc(ferr) == EOF);
	fclose(ferr);
}

int main(int argc, char *argv[]){
	if(argc < 2){
		goto usage;
	} else {
		stop_before_running_shellcode();
		test_shellcode(argv[1], test_connect_sh);
		return 0;
	}

usage:
	fprintf(stderr, "%s: [filename]\n", argv[0]);
	return 1;
}
