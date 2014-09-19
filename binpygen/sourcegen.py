#!/usr/bin/python
#
# Copyright 2014 Joseph Landry
#

import StringIO


def generate_undefined(sio, data):
    l = len(data)
    for i in xrange(0, l, 16):
        sio.write("shellcode += \"")
        ll = l - i
        if ll > 16:
            ll = 16
        for j in xrange(i, i+ll):
            sio.write("\\x%02X" % (ord(data[j]), ))
        sio.write("\"\n")


def generate_data(sio, data):
    sio.write("shellcode += ")
    sio.write(data["value"])
    sio.write("\n")


def collect_depends(datas):
    deps = set()

    for d in datas:
        if d[0] == 'd':
            deps.update(d[1][1]["depends"])
    return deps


def generate_source(datas):
    """datas is an array of tuples:
        item[0] is in ['u', 'd']
        item[0] == 'u':
            item[1] = raw string
        item[1] == 'd':
            item[1] = rule tuple
    """
    sio = StringIO.StringIO()
    deps = collect_depends(datas)
    deps = sorted(deps)
    if len(deps) > 0:
        for d in deps:
            sio.write("import %s\n" % (d,))
        sio.write("\n")

    sio.write("shellcode = \"\"\n")

    for d in datas:
        if d[0] == 'd':
            generate_data(sio, d[1][1])
        elif d[0] == 'u':
            generate_undefined(sio, d[1])
    return sio.getvalue()
