#ifndef TESTS_RUNNER_H
#define TESTS_RUNNER_H

#include <stdio.h>
#include <unistd.h>

typedef  void (testfn_t)(FILE *, FILE *, FILE *, pid_t child);
int test_shellcode(char *filename, testfn_t *testfn);
void stop_before_running_shellcode(void);
void set_prerun_callback(void (*callback)(void));
void set_prerun_postcontinue_callback(void (*callback)(void));
int bind_tcp(unsigned long ip, unsigned short port);
int accept_tcp(int fd);
int connect_tcp(unsigned long ip, unsigned short port);

#endif
