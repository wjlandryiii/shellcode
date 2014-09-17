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

	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = htons(1234);
	addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
	addr.sin_addr.s_addr = INADDR_ANY;

	if((fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1){
		fprintf(stderr, "%s:%d: socket()\n", __FILE__, __LINE__);
		exit(1);
	} else if(setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &y, sizeof(y))){
		fprintf(stderr, "%s:%d: setsockopt()\n", __FILE__, __LINE__);
		exit(1);
	} else if(bind(fd, (void *)&addr, sizeof(addr))){
		fprintf(stderr, "%s:%d: bind()\n", __FILE__, __LINE__);
		exit(1);
	} else if(listen(fd, 5)){
		fprintf(stderr, "%s:%d: listen()\n", __FILE__, __LINE__);
		exit(1);
	} else {
		assert(waitpid(pid, NULL, WSTOPPED) == pid);
		assert(kill(pid, SIGCONT) == 0);
		addrlen = sizeof(addr);
		while((fd_conn = accept(fd, (void *)&addr, &addrlen)) == -1){
			fprintf(stderr, "accept(): %d\n", errno);
		}
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
