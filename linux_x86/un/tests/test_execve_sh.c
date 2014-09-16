#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <err.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/mman.h>

unsigned char *shellcode = NULL;

int load_shellcode(char *file){
	FILE *f;
	long size;
	char *buff;
	int c;
	char *p;

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
	} else if((buff = mmap(NULL, size, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0)) == NULL){
		printf("mmap()\n");
		exit(1);
	} else if(fread(buff, 1, size, f) != size){
		printf("fread()\n");
		exit(1);
	} else {
		printf("loaded!\n");
		fclose(f);
		shellcode = buff;
		return 0;
	}
	return -1;
}

int run_shellcode(void){
	void (*f)(void);

	f = (void (*)(void)) shellcode;
	f();
	return 0;
}

int main(int argc, char *argv[]){
	pid_t pid;
	int child_in[2];
	int child_out[2];
	int child_err[2];
	char buff[1024];

	FILE *f_out;
	FILE *f_in;
	FILE *f_err;
	int c;
	int status;

	load_shellcode("../execve_sh.bin");

	if(pipe(child_in)){
		errx(1, "%s:%d", __FILE__, __LINE__);
	} else if(pipe(child_out)){
		errx(1, "%s:%d", __FILE__, __LINE__);
	} else if(pipe(child_err)){
		errx(1, "%s:%d", __FILE__, __LINE__);
	} else if((pid = fork()) < 0){
		errx(1, "%s:%d", __FILE__, __LINE__);
	} else {
		if(pid == 0){
			/* child */
			close(child_in[1]);
			close(child_out[0]);
			close(child_err[0]);
			close(0);
			close(1);
			close(2);
			dup2(child_in[0], 0);
			dup2(child_out[1], 1);
			dup2(child_err[1], 2);
			close(child_in[0]);
			close(child_out[1]);
			close(child_err[1]);

			//execl("/bin/sh", "sh", NULL);
			run_shellcode();
		} else {
			/* parent */
			close(child_in[0]);
			close(child_out[1]);
			close(child_err[1]);

			f_in = fdopen(child_in[1], "w");
			setlinebuf(f_in);
			f_out = fdopen(child_out[0], "r");
			f_err = fdopen(child_err[0], "r");

			printf("reading...\n");
			fputs("uname\n", f_in);
			if(fgets(buff, 1024-1, f_out) == NULL){
				fprintf(stderr, "fgets() returnd NULL\n");
				exit(-1);
			}
			printf("read\n");
			if(strcmp(buff, "Linux\n") != 0){
				fprintf(stderr, "uname didn't return Linux\n");
				fprintf(stderr, "%s\n", buff);
				exit(-1);
			}
			fputs("exit\n", f_in);
			if(fgetc(f_out) != EOF){
				fprintf(stderr, "exit didn't exit\n");
			}
			waitpid(pid, &status, 0);
			printf("%d\n", status);
		}
	}
	return 0;
}
