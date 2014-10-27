#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/mman.h>

#include "tests/runner.h"


void (*shellcode_fn)(void);

static int load_shellcode(char *file){
	FILE *f;
	long size;
	unsigned char *buff;
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
	} else if(fread(buff+1, 1, size, f) != size){
		printf("fread()\n");
		exit(1);
	} else {
		fclose(f);
		buff[0] = 0x90;
		shellcode_fn = (void *) buff;
		return 0;
	}
	return -1;
}

int main(int argc, char *argv[]){
	int fd;

	//fd = connect_tcp(inet_addr("192.168.56.1"), htons(1234));
	fd = connect_tcp(htonl(INADDR_LOOPBACK), htons(1234));
	printf("FD IS %d\n", fd);

	send(fd, "ok\n", 3, 0);

	load_shellcode("reusefd_findip.bin");

	shellcode_fn();

	close(fd);

	return 0;
}
