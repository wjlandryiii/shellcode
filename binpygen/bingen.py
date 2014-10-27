#!/usr/bin/python
#
# Copyright 2014 Joseph Landry
#

import os

import typesfile
import sourcegen

def load_binary(filename):
    with open(filename, "rb") as f:
        binary = f.read()
    return binary

def write_source(filename, source):
    with open(filename, "wb") as f:
        f.write(source)

def apply_rules_to_bin(binary, rules):
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
    return datas


def validate_source(source, binary):
    test_globals = {}
    try:
        exec (source, test_globals)
    except Exception as e:
        print "ERROR IN GENERATED SOURCE"
        print source
        raise e
    if test_globals["shellcode"] != binary:
        raise Exception("Generated source did not evaluate to original binary")


def generate_python_shellcode(bin_filename, types_filename=None):
    binary = load_binary(bin_filename)
    if types_filename is None:
        rules = []
    else:
        rules = typesfile.load_types_file(types_filename)
    datas = apply_rules_to_bin(binary, rules)
    source = sourcegen.generate_source(datas)
    validate_source(source, binary)
    return source

def main(argv):
    import getopt

    optlist, args = getopt.getopt(argv[1:], "o:t:")

    if len(args) < 1:
        print "%s: [-t type file] [-o output file] [bin file]" % (argv[0],)
        return 1
    else:
        binary_filename = args[0]

    types_filename = None
    output_filename = None
    for o, a in optlist:
        if o == "-t":
            types_filename = a
        elif o == "-o":
            output_filename = a

    if types_filename is None:
        filename = os.path.splitext(binary_filename)[0] + ".types"
        if os.path.isfile(filename):
            types_filename = filename

    source = generate_python_shellcode(binary_filename, types_filename)
    if output_filename is not None:
        write_source(output_filename, source)
    else:
        sys.stdout.write(source)
    return 0



# src = generate_python_shellcode("tests/files/execve.bin", "tests/files/execve.types")
# print src

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))

