#ifndef TESTS_RUNNER_H
#define TESTS_RUNNER_H

#include <stdio.h>
#include <unistd.h>

typedef  void (testfn_t)(FILE *, FILE *, FILE *, pid_t child);
int test_shellcode(char *filename, testfn_t *testfn);

#endif
