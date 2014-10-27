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

int bind_fd;
int conn_fd;

static void prerun_callback(void){

	bind_fd = bind_tcp(htonl(INADDR_LOOPBACK), htons(1234));
}

static void prerun_postcontinue_callback(void){
	conn_fd = accept_tcp(bind_fd);	
}

void test_reusefd(FILE *fin, FILE *fout, FILE *ferr, pid_t pid){
	char buff[1024];
	int sock_fd;
	FILE *f_sock;
	int status;

	assert(waitpid(pid, NULL, WSTOPPED) == pid);
	assert(kill(pid, SIGCONT) == 0);
	
	sock_fd = connect_tcp(htonl(INADDR_LOOPBACK), htons(1234));

	f_sock = fdopen(sock_fd, "r+");

	assert(fputs("uname\n", f_sock) != EOF);
	assert(fgets(buff, sizeof(buff), f_sock) != NULL);
	assert(strcmp(buff, "Linux\n") == 0);

	assert(fputs("exit\n", f_sock) != EOF);
	assert(fgetc(f_sock) == EOF);

	assert(waitpid(pid, &status, 0) == pid);
	assert(status == 0);


	fclose(f_sock);
	close(sock_fd);
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
		set_prerun_callback(prerun_callback);
		set_prerun_postcontinue_callback(prerun_postcontinue_callback);
		test_shellcode(argv[1], test_reusefd);
		return 0;
	}
usage:
	fprintf(stderr, "%s: [filename]\n", argv[0]);
	return 1;
}
