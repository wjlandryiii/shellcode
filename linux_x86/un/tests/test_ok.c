#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <sys/types.h>
#include <sys/wait.h>

#include "runner.h"

void test_ok(FILE *fin, FILE *fout, FILE *ferr, pid_t pid){
	char buff[64] = { 0 };
	int status;

	assert(fgets(buff, 64, fout) != NULL);
	assert(strcmp(buff, "OK\n") == 0);

	assert(waitpid(pid, &status, 0) == pid);
	assert(status == 0);
}

int main(int argc, char *argv[]){
	if(argc < 2){
		goto usage;
	} else {
		test_shellcode(argv[1], test_ok);
	}
	return 0;

usage:
	fprintf(stderr, "%s: [filename]\n", argv[0]);
	return -1;
}
