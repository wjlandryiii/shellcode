#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>
#include <sys/socket.h>
#include <string.h>
#include <netinet/in.h>


void (*shellcode_fp)(void);

void *shellcode_buff;

int load_shellcode(int fd){
	char *p;
	int bytes;

	shellcode_buff = mmap(NULL, 1024*1024*4, PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_EXECUTABLE | MAP_ANONYMOUS, 0, 0);

	//memset(shellcode_buff, 0xc3 /*ret*/, 1024*1024*4);

	if(shellcode_buff == NULL){
		printf("allocation error");
		exit(1);
	}

	p = shellcode_buff;
	bytes = 1;
	while(bytes > 0){
		bytes = read(fd, p, 512);
		p += bytes;
	}
	shellcode_fp = shellcode_buff;
	return p - (char *)shellcode_buff;
}

void run_shellcode(void){
	shellcode_fp();
}

void tcp_server(unsigned short port, int dupfd){
	int listen_sock;
	int connect_sock;
	int reuse;
	struct sockaddr_in addr;

	listen_sock = socket(AF_INET, SOCK_STREAM, 0);
	if(listen_sock < 0){
		printf("socket() error\n");
		exit(1);
	}

	reuse = 1;
	if(setsockopt(listen_sock, SOL_SOCKET, SO_REUSEADDR, &reuse, sizeof(reuse)) != 0){
		printf("setsockopt() error\n");
		exit(1);
	}

	memset(&addr, 0, sizeof(addr));
	addr.sin_port = htons(port);
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = INADDR_ANY;

	if(bind(listen_sock, (struct sockaddr*)&addr, sizeof(addr)) != 0){
		printf("bind() error\n");
		exit(1);
	}

	if(listen(listen_sock, 5) != 0){
		printf("listen() error\n");
		exit(1);
	}

	connect_sock = accept(listen_sock, NULL, NULL);

	if(connect_sock < 0){
		printf("accept() error\n");
		exit(1);
	}

	close(listen_sock);

	dup2(connect_sock, dupfd);

	run_shellcode();
}

void print_usage(char *filename){
	printf("%s: [-l port dupfd] [shellcode file]\n", filename);
	printf("\t-l listens on TCP port, then dups the connection socket to dupfd before running the shellcode\n");
}

int main(int argc, char *argv[]){
	int fd;
	unsigned short port;
	int dupfd;

	if(argc == 5){
		if(strcmp(argv[1], "-l") == 0){
			port = atoi(argv[2]);
			dupfd = atoi(argv[3]);

			fd = open(argv[4], 0);
			if(fd < 0){
				printf("open() error\n");
				exit(1);
			}
			load_shellcode(fd);
			close(fd);

			tcp_server(port, dupfd);
			return 0;
		}
	}
	if(argc == 2){
		fd = open(argv[1], 0);
		if(fd < 0){
			printf("open() error\n");
			exit(1);
		}
		load_shellcode(fd);
		close(fd);
		run_shellcode();
	}
	print_usage(argv[0]);
	return 0;
}
