#!/usr/bin/python
#
# Copyright 2014 Joseph Landry
#

import sys
import StringIO

blist = []
outs = StringIO.StringIO()

def dump_b(b):
    global outs
    l = len(b)
    for i in xrange(0, l, 16):
        ll = l - i
        if ll > 16:
            ll = 16
        outs.write("shellcode += \"")
        for j in xrange(i, i+ll):
            outs.write("\\x%02X" % (ord(b[j]), ))
        outs.write("\"\n")


def dump_s(s):
    global outs
    outs.write("shellcode += \"%s\"\n" % (repr(s)[1:-1]))


def dump_blist():
    global blist
    global outs
    outs.write("shellcode = \"\"\n")
    for b in blist:
        if b[0] == 'b':
            dump_b(b[1])
        elif b[0] == 's':
            dump_s(b[1])
        else:
            raise Exception("Unknown type: %s" % (b[0],))


def add_byte(b):
    global blist
    if len(blist) == 0:
        blist += [['b', b]]
    elif blist[-1][0] == 'b':
        blist[-1][1] += b
    else:
        blist += [['b', b]]


def add_string(s):
    global blist
    blist += [['s', s]]


def sc_to_py(sc, strs):
    i = 0
    skip = 0
    while(i < len(sc)):
        skip = 0
        for s in strs:
            if sc.find(s) == i:
                add_string(s)
                i += len(s)
                skip = 1
        if skip == 0:
            add_byte(sc[i])
            i += 1
    dump_blist()


def read_bin(filename):
    f = open(filename, "rb")
    contents = f.read()
    f.close()
    return contents


def main(argv):
    global blist
    global outs
    contents = read_bin("execve.bin")
    sc_to_py(contents, ["-c\x00", "/bin/sh\x00\x00", "sh\x00"])
    print outs.getvalue()
    return 0

if __name__ == "__main__":
    exit(main(sys.argv))
