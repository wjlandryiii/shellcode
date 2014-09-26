/*
 * Copyright 2014 Joseph Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int test_exit0(FILE *in, FILE *out, pid_t pid){
	int status;
	pid_t wpid;

	wpid = waitpid(pid, &status, 0);
	if(wpid != pid){
		fprintf(stderr, "%s:%d waitpid()\n", __FILE__, __LINE__);
		fprintf(stderr, "Expected pid: %d but got: %d\n", pid, wpid);
		exit(1);
	}
	if(status != 0){
		fprintf(stderr, "%s:%d waitpid()\n", __FILE__, __LINE__);
		fprintf(stderr, "Expected status 0 but got %d\n", status);
		exit(1);
	}
	printf("exit0: ok\n");
	return 0;
}

int test_ok(FILE *in, FILE *out, pid_t pid){
	char buff[1024];
	int status;
	pid_t wpid;
	int c;

	if(fgets(buff, sizeof(buff), in) == NULL){
		fprintf(stderr, "%s:%d fgets()\n", __FILE__, __LINE__);
		fprintf(stderr, "fgets returned NULL\n");
		exit(1);
	}

	if(strcmp(buff, "OK\n") != 0){
		fprintf(stderr, "%s:%d strcmp()\n", __FILE__, __LINE__);
		fprintf(stderr, "Expected \"OK\\n\" but got: %s\n", buff);
		exit(1);
	}

	if((c = fgetc(in)) != EOF){
		fprintf(stderr, "%s:%d fgetc()\n", __FILE__, __LINE__);
		fprintf(stderr, "Expected EOF but got %d\n", c);
		exit(1);
	}

	wpid = waitpid(pid, &status, 0);
	if(wpid != pid){
		fprintf(stderr, "%s:%d waitpid()\n", __FILE__, __LINE__);
		fprintf(stderr, "Expected pid: %d but got: %d\n", pid, wpid);
		exit(1);
	}
	if(status != 0){
		fprintf(stderr, "%s:%d waitpid()\n", __FILE__, __LINE__);
		fprintf(stderr, "Expected status 0 but got %d\n", status);
		exit(1);
	}

	assert(fgetc(in) == EOF);
	printf("ok: ok\n");
	return 0;
}


int test_sh(FILE *in, FILE *out, pid_t pid){
	char buff[1024];

	setlinebuf(out);
	assert(fputs("echo sh test\n", out) != EOF);
	assert(fgets(buff, sizeof(buff), in) != NULL);
	assert(strcmp(buff, "sh test\n") == 0);
	assert(fputs("exit\n", out) != EOF);
	assert(fgetc(in) == EOF);
	printf("sh: ok\n");
	return 0;
}



char *readfile_filename = "/etc/passwd";

int test_readfile(FILE *in, FILE *out, pid_t pid){
	FILE *f;
	int c_f = 0;
	int c_sc = 0;

	f = fopen(readfile_filename, "r");

	while(c_f != EOF && c_sc != EOF){
		c_f = fgetc(f);
		c_sc = fgetc(in);
		assert(c_f == c_sc);
	}
	printf("readfile: ok\n");
	return 0;
}
