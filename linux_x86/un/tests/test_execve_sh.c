/*
 * Copyright 2014 Joseph Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <unistd.h>
#include <err.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/mman.h>

#include "runner.h"

void test_execve_sh(FILE *fin, FILE *fout, FILE *ferr, pid_t pid){
	char buff[64];
	int status;

	setlinebuf(fin);

	assert(fputs("uname\n", fin) >= 0);
	assert(fgets(buff, sizeof(buff), fout) != NULL);
	assert(strcmp(buff, "Linux\n") == 0);

	assert(fputs("exit\n", fin) >= 0);
	assert(fgetc(fout) == EOF);
	assert(fgetc(ferr) == EOF);

	assert(waitpid(pid, &status, 0) == pid);
	assert(status == 0);
}

int main(int argc, char *argv[]){
	if(argc < 2){
		goto usage;
	} else {
		test_shellcode(argv[1], test_execve_sh);
		return 0;
	}

usage:
	fprintf(stderr, "%s: [filename]\n", argv[0]);
	return 1;
}
