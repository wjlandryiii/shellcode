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

char *filename = "flag.txt";
char *flagfile = "The key is:\nwuba luba dub dub!\n";

void test_readfile(FILE *fin, FILE *fout, FILE *ferr, pid_t pid){
	char buff[1024] = { 0 };
	int status;

	assert(waitpid(pid, &status, 0) == pid);
	assert(fread(buff, strlen(flagfile), 1, fout) == 1);
	assert(fgetc(fout) == EOF);
	assert(fgetc(ferr) == EOF);
}

int main(int argc, char *argv[]){
	FILE *f;

	if(argc < 2){
		goto usage;
	} else {
		if((f = fopen(filename, "w")) == NULL){
			fprintf(stderr, "%s:%d fopen()\n", __FILE__, __LINE__);
			exit(1);
		} else if(fwrite(flagfile, strlen(flagfile), 1, f) != 1){
			fprintf(stderr,"%s:%d fwrite()\n", __FILE__, __LINE__);
		} else {
			fclose(f);
			test_shellcode(argv[1], test_readfile);
			remove(filename);
		}
		return 0;
	}
usage:
	fprintf(stderr, "%s: [filename]\n", argv[0]);
	return 1;
}
