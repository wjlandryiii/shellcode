/*
 * Copyright 2014 Joseph Landry
 */

#ifndef TESTS_H
#define TESTS_H

#include <unistd.h>

int test_exit0(FILE *in, FILE *out, pid_t pid);
int test_ok(FILE *in, FILE *out, pid_t pid);
int test_sh(FILE *in, FILE *out, pid_t pid);
int test_readfile(FILE *in, FILE *out, pid_t pid);

#endif
