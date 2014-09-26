/*
 * Copyright 2014 Jospeh Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>

static void(*shellcode)(void) = NULL;

int load_shellcode(char *filename){
	FILE *f;
	long size;
	void *buff;

	int flags = MAP_PRIVATE | MAP_ANONYMOUS;
	int prot = PROT_READ | PROT_WRITE | PROT_EXEC;
	
	if((f = fopen(filename, "r")) == NULL){
		fprintf(stderr, "%s:%d fopen()\n", __FILE__, __LINE__);
		exit(1);
	} else if(fseek(f, 0, SEEK_END)){
		fprintf(stderr, "%s:%d fseek()\n", __FILE__, __LINE__);
		exit(1);
	} else if((size = ftell(f)) < 0){
		fprintf(stderr, "%s:%d ftell()\n", __FILE__, __LINE__);
		exit(1);
	} else if(fseek(f, 0, SEEK_SET)){
		fprintf(stderr, "%s:%d fseek()\n", __FILE__, __LINE__);
		exit(1);
	} else if((buff = mmap(NULL, size, prot, flags, -1, 0)) == MAP_FAILED){
		fprintf(stderr, "%s:%d mmap()\n", __FILE__, __LINE__);
		exit(1);
	} else if(fread(buff, 1, size, f) != size){
		fprintf(stderr, "%s:%d fread()\n", __FILE__, __LINE__);
		exit(1);
	} else {
		fclose(f);
		shellcode = buff;
		return 0;
	}
}

void run_shellcode(void){
	fprintf(stderr, "Launching shellcode...\n");
	if(shellcode == NULL){
		fprintf(stderr, "SHELLCODE POINTER IS NULL!\n");
		exit(1);
	}
	shellcode();
	exit(1);
}
