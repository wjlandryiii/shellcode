#!/usr/bin/python
#
# Copyright 2014 Joseph Landry
#

import typesfile
import sourcegen


with open("tests/files/execve.bin", "rb") as f:
    binary = f.read()

rules = typesfile.load_types_file("tests/files/execve.types")

datas = []


working_bin = binary



for rule in reversed(rules):
    rule_i = working_bin.rfind(rule[0])
    if rule_i < 0:
        raise Exception("Couldn't find rule: %s" % (rule[1]["value"],))
    if rule_i + len(rule[0]) < len(working_bin):
        d = working_bin[rule_i+len(rule[0]):]
        datas = [('u', d)] + datas
        working_bin = working_bin[:rule_i+len(rule[0])]
    datas = [('d', rule)] + datas
    working_bin = working_bin[:rule_i]
if len(working_bin) > 0:
    datas = [('u', working_bin)] + datas
    working_bin = ""


src = sourcegen.generate_source(datas)

test_globals = {}

exec (src, test_globals)


if test_globals["shellcode"] == binary:
    print src
else:
    print "verification failed"



