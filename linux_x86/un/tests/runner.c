#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <err.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/mman.h>

#include "runner.h"

static void (*shellcode)(void) = NULL;

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
		shellcode = buff;
		return 0;
	}
	return -1;
}

static void run_shellcode(void){
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
	run_shellcode();
	exit(-1);
}

void parent(testfn_t *testfn, int in, int out, int err, pid_t child){
	FILE *fin;
	FILE *fout;
	FILE *ferr;

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

