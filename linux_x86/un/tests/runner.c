/*
 * Copyright 2014 Joseph Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <err.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/mman.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>

#include "runner.h"

static int stop_flag = 0;
static void (*shellcode)(void) = NULL;

static void (*prerun_callback)(void) = NULL;
static void (*prerun_postcontinue_callback)(void) = NULL;

static int load_shellcode(char *file){
	FILE *f;
	long size;
	void *buff;
	int c;
	char *p;

	int flags = MAP_PRIVATE | MAP_ANONYMOUS;
	int prot = PROT_READ | PROT_WRITE | PROT_EXEC;


	if((f = fopen(file, "r")) == NULL){
		printf("open()\n");
		exit(1);
	} else if(fseek(f, 0, SEEK_END)){
		printf("fseek()\n");
		exit(1);
	} else if((size = ftell(f)) < 0){
		printf("ftell()\n");
		exit(1);
	} else if(fseek(f, 0, SEEK_SET)){
		printf("fseek()\n");
		exit(1);
	} else if((buff = mmap(NULL, size, prot, flags, -1, 0)) == MAP_FAILED){
		printf("mmap()\n");
		exit(1);
	} else if(fread(buff, 1, size, f) != size){
		printf("fread()\n");
		exit(1);
	} else {
		fclose(f);
		shellcode = (void *) buff;
		return 0;
	}
	return -1;
}

static void run_shellcode(void){
	if(prerun_callback != NULL){
		prerun_callback();
	}
	if(stop_flag){
		raise(SIGSTOP);
	}
	if(prerun_postcontinue_callback != NULL){
		prerun_postcontinue_callback();
	}
	shellcode();
}

void child(int in, int out, int err){
	fclose(stdin);
	fclose(stdout);
	fclose(stderr);
	dup2(in, 0);
	dup2(out, 1);
	dup2(err, 2);
	stdin = fdopen(0, "r");
	stdout = fdopen(1, "w");
	stderr = fdopen(2, "w");
	alarm(5);
	run_shellcode();
	exit(-1);
}

void parent(testfn_t *testfn, int in, int out, int err, pid_t child){
	FILE *fin;
	FILE *fout;
	FILE *ferr;

	alarm(5);

	fin = fdopen(in, "w");
	fout = fdopen(out, "r");
	ferr = fdopen(err, "r");
	testfn(fin, fout, ferr, child);
}

int test_shellcode(char *filename, testfn_t *testfn){
	pid_t pid;
	int in[2];
	int out[2];
	int err[2];
	
	load_shellcode(filename);

	if(pipe(in)){
		fprintf(stderr, "%s:%d pipe()\n", __FILE__, __LINE__);
		exit(-1);
	} else if(pipe(out)){
		fprintf(stderr, "%s:%d pipe()\n", __FILE__, __LINE__);
		exit(-1);
	} else if(pipe(err)){
		fprintf(stderr, "%s:%d pipe()\n", __FILE__, __LINE__);
		exit(-1);
	}

	pid = fork();

	if(pid < 0){
		fprintf(stderr, "Error on fork()\n");
		exit(1);
	} else if(pid == 0){
		/* child */
		close(in[1]);
		close(out[0]);
		close(err[0]);
		child(in[0], out[1], err[1]);
	} else { 
		/* parent */
		close(in[0]);
		close(out[1]);
		close(err[1]);
		parent(testfn, in[1], out[0], err[0], pid);
	}
	return 0;
}	

void stop_before_running_shellcode(void){
	stop_flag = 1;
}

void set_prerun_callback(void (*callback)(void)){
	prerun_callback = callback;
}

void set_prerun_postcontinue_callback(void (*callback)(void)){
	prerun_postcontinue_callback = callback;
}

int bind_tcp(unsigned long ip, unsigned short port){
	int fd;
	struct sockaddr_in addr;
	int addrlen;
	FILE *f_sock;
	int y = 1;
	
	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = port;
	addr.sin_addr.s_addr = ip;

	if((fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1){
		fprintf(stderr, "%s:%d: socket()\n", __FILE__, __LINE__);
		exit(1);
	} else if(setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &y, sizeof(y))){
		fprintf(stderr, "%s:%d: setsockopt()\n", __FILE__, __LINE__);
		exit(1);
	} else if(bind(fd, (void *)&addr, sizeof(addr))){
		fprintf(stderr, "%d:%s\n", errno, strerror(errno));
		fprintf(stderr, "%s:%d: bind()\n", __FILE__, __LINE__);
		exit(1);
	} else if(listen(fd, 5)){
		fprintf(stderr, "%s:%d: listen()\n", __FILE__, __LINE__);
		exit(1);
	} else {
		return fd;
	}
}

int accept_tcp(int fd){
	int conn_fd;
	struct sockaddr_in addr;
	int addrlen = sizeof(addr);

	while((conn_fd = accept(fd, (void *)&addr, &addrlen)) == -1){
		fprintf(stderr, "accept(): %d\n", errno);
	}
	return conn_fd;
}

int connect_tcp(unsigned long ip, unsigned short port){
	int fd;
	struct sockaddr_in addr;

	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = port;
	addr.sin_addr.s_addr = ip;
	
	if((fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1){
		fprintf(stderr, "%s:%d: socket()\n", __FILE__, __LINE__);
		exit(1);
	} else if(connect(fd, (void *)&addr, sizeof(addr))){
		fprintf(stderr, "%s:%d: connect()\n", __FILE__, __LINE__);
		exit(1);
	} else {
		return fd;
	}
}
