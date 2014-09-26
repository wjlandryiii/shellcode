/*
 * Copyright 2014 Joseph Landry
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/select.h>
#include <netinet/in.h>


int tcp_bind(unsigned long ip, unsigned short port){
	int fd;
	struct sockaddr_in addr;
	int y;

	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = port;
	addr.sin_addr.s_addr = ip;

	if((fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0){
		fprintf(stderr, "%s:%d socket()\n", __FILE__, __LINE__);
		exit(1);
	} else if(setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &y, sizeof(y))){
		fprintf(stderr, "%s:%d setsockopt()\n", __FILE__, __LINE__);
		exit(1);
	} else if(bind(fd, (void *)&addr, sizeof(addr))){
		fprintf(stderr, "%s:%d bind()\n", __FILE__, __LINE__);
		exit(1);
	} else if(listen(fd, 5)){
		fprintf(stderr, "%s:%d listen()\n", __FILE__, __LINE__);
		exit(1);
	} else {
		return fd;
	}
}

int tcp_accept(int fd){
	int conn_fd;
	struct sockaddr_in addr;
	int addrlen = sizeof(addr);

	while((conn_fd = accept(fd, (void *)&addr, &addrlen)) == -1){
		fprintf(stderr, "%s:%d accept()\n", __FILE__, __LINE__);
	}
	return conn_fd;
}

int tcp_connect(unsigned long ip, unsigned short port){
	int fd;
	struct sockaddr_in addr;

	memset(&addr, 0, sizeof(addr));
	addr.sin_family = AF_INET;
	addr.sin_port = port;
	addr.sin_addr.s_addr = ip;
	
	if((fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1){
		fprintf(stderr, "%s:%d: socket()\n", __FILE__, __LINE__);
		exit(1);
	} else if(connect(fd, (void *)&addr, sizeof(addr))){
		fprintf(stderr, "%s:%d: connect()\n", __FILE__, __LINE__);
		exit(1);
	} else {
		return fd;
	}
}

int hide_fd(int fd){
	dup2(fd, 500);
	close(fd);
}


int do_telnet(int fd){
	int nfds;
	fd_set readfds;
	fd_set writefds;
	fd_set exceptfds;
	char buff[1024];
	int nbytes_read;
	int nbytes_sent;
	int keyboard_EOF = 0;
	int network_EOF = 0;

	nfds = fd + 1;
	
	while(keyboard_EOF == 0 || network_EOF == 0){
		FD_ZERO(&readfds);
		if(!network_EOF)
			FD_SET(0, &readfds);
		if(!keyboard_EOF)
			FD_SET(fd, &readfds);

		FD_ZERO(&writefds);

		FD_ZERO(&exceptfds);


		if(select(nfds, &readfds, &writefds, &exceptfds, NULL) == -1){
			fprintf(stderr, "%s:%d select()\n", __FILE__, __LINE__);
			exit(1);
		}

		if(FD_ISSET(fd, &readfds)){
			nbytes_read = recv(fd, buff, sizeof(buff), 0);
			if(nbytes_read == 0){
				fprintf(stderr, "peer shutdown connection\n");
				network_EOF = 0;
				exit(1);
			} else if(nbytes_read < 0){
				fprintf(stderr, "errror recv from peer\n");
				exit(1);
			} else {
				nbytes_sent = write(1, buff, nbytes_read);
				if(nbytes_sent < 0){
					fprintf(stderr, "error writing to stdout\n");
					exit(1);
				} else if(nbytes_sent != nbytes_read){
					fprintf(stderr, "less bytes sent to sdout\n");
					exit(1);
				} else {
					// good to go
				}
			}
		}

		if(FD_ISSET(0, &readfds)){
			nbytes_read = read(0, buff, sizeof(buff));
			if(nbytes_read == 0){
				fprintf(stderr, "stdin EOF\n");
				keyboard_EOF=1;
				shutdown(fd, SHUT_WR);
			} else {
				nbytes_sent = send(fd, buff, nbytes_read, 0);
				if(nbytes_sent < 0){
					fprintf(stderr, "error writing to peer\n");
					exit(1);
				} else if(nbytes_sent != nbytes_read){
					fprintf(stderr, "less bytes sent to peer\n");
					exit(1);
				} else {
					// good to go
				}
			}
		}
	}
}


int main(int argc, char *argv[]){
	int listen_fd;
	int connect_fd;
	int c;
	char *p;
	unsigned short port;
	pid_t pid;
	int status;
	int opt_debug = 0;

	port = 1234;

	while((c = getopt(argc, argv, "dp:")) != EOF){
		if(c == 'd'){
			opt_debug = 1;
		} else if(c == 'p'){
			port = strtol(optarg, &p, 0);
			if(*p == 0){
				port = htons(port);
			} else {
				fprintf(stderr, "Invalid port: %s\n", optarg);
				exit(1);
			}
		} else {
			fprintf(stderr, "Unknown option: %c\n", c);
			exit(1);
		}
	}

	listen_fd = tcp_bind(htonl(INADDR_ANY), htons(port));

	pid = fork();
	if(pid < 0){
		fprintf(stderr, "%s:%d fork()\n", __FILE__, __LINE__);
		exit(1);
	} else if(pid == 0){
		/* CHILD */
		connect_fd = tcp_accept(listen_fd);
		hide_fd(connect_fd);
		execvp(argv[optind], &argv[optind]);
		exit(1);
	} else {
		/* PARENT */
		close(listen_fd);
		connect_fd = tcp_connect(htonl(INADDR_ANY), htons(port));
		do_telnet(connect_fd);
		wait(&status);
		return status;
	}
	
	return 0;
}
