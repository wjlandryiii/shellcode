/*
 * Copyright 2014 Jospeh Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>

#include "tests.h"
#include "runsc.h"
#include "mock.h"

enum {
	TEST_EXIT0 = 0,
	TEST_OK,
	TEST_SH,
	TEST_READFILE
};

int test_type = TEST_EXIT0;
int opt_mock = 0;



void run_shellcode_for_test(void){
	run_shellcode();
}

void child(int in, int out){
	FILE *fin;
	FILE *fout;

	fclose(stdin);
	fclose(stdout);
	stdin = NULL;
	stdout = NULL;

	dup2(in, 0);
	dup2(out, 1);

	close(in);
	close(out);

	if(!opt_mock){
		run_shellcode_for_test();
	} else {
		if(test_type == TEST_EXIT0){
			mock_exit0();
			exit(1);
		} else if (test_type == TEST_OK){
			mock_ok();
			exit(1);
		} else if(test_type == TEST_SH){
			mock_sh();
			exit(1);
		} else if(test_type == TEST_READFILE){
			mock_readfile();
			exit(1);
		} else {
			exit(1);
		}
	}
}

void parent(int in, int out, pid_t pid){
	FILE *fin;
	FILE *fout;

	if((fin = fdopen(in, "r")) == NULL){
		fprintf(stderr, "%s:%d fdopen()\n", __FILE__, __LINE__);
		exit(1);
	} else if((fout = fdopen(out, "w")) == NULL){
		fprintf(stderr, "%s:%d fdopen()\n", __FILE__, __LINE__);
		exit(1);
	}

	switch(test_type){
	case TEST_EXIT0:
		test_exit0(fin, fout, pid);
		break;
	case TEST_OK:
		test_ok(fin, fout, pid);
		break;
	case TEST_SH:
		test_sh(fin, fout, pid);
		break;
	case TEST_READFILE:
		test_readfile(fin, fout, pid);
		break;
	default:
		printf("didn't know what test to run!\n");
		exit(1);
	}
	printf("OK!\n");
	exit(0);
}

int run_test(){
	pid_t pid;
	int child_in[2];
	int child_out[2];

	if(pipe(child_in)){
		fprintf(stderr, "%s:%d pipe()\n", __FILE__, __LINE__);
		exit(-1);
	} else if(pipe(child_out)){
		fprintf(stderr, "%s:%d pipe()\n", __FILE__, __LINE__);
		exit(-1);
	}

	pid = fork();

	if(pid < 0){
		fprintf(stderr, "%s:%d fork()\n", __FILE__, __LINE__);
		exit(-1);
	} else if(pid == 0){
		/* child */
		close(child_in[1]);
		close(child_out[0]);
		child(child_in[0], child_out[1]);
	} else {
		/* parent */
		close(child_in[0]);
		close(child_out[1]);
		parent(child_out[0], child_in[1], pid);
	}
	return 0;
}

int main(int argc, char *argv[]){
	int c;
	char *test_str = "exit0";
	int test;

	while((c = getopt(argc, argv, "hmt:")) != -1){
		switch(c){
		case 'h':
			goto usage;
		case 'm':
			opt_mock = 1;
			break;
		case 't':
			test_str = optarg;
			break;
		}
	}

	if(strcmp(test_str, "exit0") == 0){
		test_type = TEST_EXIT0;
	} else if(strcmp(test_str, "ok") == 0){
		test_type = TEST_OK;
	} else if(strcmp(test_str, "sh") == 0){
		test_type = TEST_SH;
	} else if(strcmp(test_str, "readfile") == 0){
		test_type = TEST_READFILE;
	} else {
		fprintf(stderr, "Invalid test type: %s\n", test_str);
		exit(1);
	}

	if(!opt_mock){
		if(argc - optind < 1){
			goto usage;
		} else {
			printf("shellcode file: %s\n", argv[optind]);
			load_shellcode(argv[optind]);
		}
	}


	run_test();
	return 0;
usage:
	printf("%s: [options] [shellcode filename]\n", argv[0]);
	printf("\tOptions:\n");
	printf("\t-t [test type]\n");
	printf("\t\texit0 (default)\n");
	printf("\t\tok\n");
	printf("\t\tsh\n");
	printf("\t\treadfile\n");
	printf("\t-m run mock functions instead of shellcode\n");
	return 1;	
}
