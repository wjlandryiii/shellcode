/*
 * Copyright 2014 Jospeh Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <sys/types.h>
#include <sys/wait.h>

#include "runner.h"

char *filename = "/etc/passwd";

void test_readfile(FILE *fin, FILE *fout, FILE *ferr, pid_t pid){
	FILE *f;
	int status;
	int c_f;
	int c_sc;

	f = fopen(filename, "r");

	do {
		c_f = fgetc(f);
		c_sc = fgetc(fout);
		assert(c_f == c_sc);
	} while(c_f != EOF && c_sc != EOF);

	assert(waitpid(pid, &status, 0) == pid);
	assert(fgetc(fout) == EOF);
	assert(fgetc(ferr) == EOF);
}

int main(int argc, char *argv[]){
	FILE *f;

	if(argc < 2){
		goto usage;
	} else {
		test_shellcode(argv[1], test_readfile);
		remove(filename);
		return 0;
	}
usage:
	fprintf(stderr, "%s: [filename]\n", argv[0]);
	return 1;
}
