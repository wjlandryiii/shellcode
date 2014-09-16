/*
 * Copyright 2014 Joseph Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <assert.h>

#include "runner.h"


unsigned char *second_stage = NULL;

void test_stage(FILE *fin, FILE *fout, FILE *ferr, pid_t pid){
	int status;
	char buff[1024] = {0};

	assert(fwrite(second_stage, 1, 0x1000, fin) == 0x1000);
	assert(waitpid(pid, &status, 0) == pid);
	assert(status == 0);
	if(!feof(ferr)){
		fread(buff, 1, sizeof(buff), ferr);
		fprintf(stderr, "Got error message:\n");
		fprintf(stderr, "STARTMESSAGE\n");
		fprintf(stderr, "%s\n", buff);
		fprintf(stderr, "ENDMESSAGE\n");
		exit(1);
	}

	assert(fgets(buff, sizeof(buff), fout) != NULL);
	assert(strcpy(buff, "OK\n") == 0);
	assert(fgetc(fout) == EOF);
}

void load_second_stage(char *filename){
	FILE *f;

	if((second_stage = calloc(0x1000, 1)) == NULL){
		fprintf(stderr, "%s:%d calloc()\n", __FILE__, __LINE__);
		exit(1);
	} else if((f = fopen(filename, "r")) == NULL){
		fprintf(stderr, "%s:%d fopen()\n", __FILE__, __LINE__);
		exit(1);
	} else if(fread(second_stage, 1, 0x1000, f) < 1){
		fprintf(stderr, "%s:%d fread()\n", __FILE__, __LINE__);
		exit(1);
	} else {
		fclose(f);
	}
}

int main(int argc, char *argv[]){
	if(argc < 3){
		goto usage;
	} else {
		load_second_stage(argv[2]);
		test_shellcode(argv[1], test_stage);
		return 0;
	}
usage:
	fprintf(stderr, "%s: [filename] [ok filename]\n", argv[0]);
	return 1;
}
