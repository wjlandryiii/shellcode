#!/usr/bin/python
#
# Copyright 2014 Joseph Landry
#

import struct
import socket

ASCII_TYPES = ["ascii"]

def parse_ascii(lnumber, type_, pattern):
    if pattern[0] != "\"" or pattern[-1] != "\"":
        raise Exception("%d: pattern expected double quotes", (lnumber,))
    pattern_value = pattern[1:-1].decode("string_escape")
    rule = (
        pattern_value,
        {
            "type": type_,
            "value": pattern,
            "depends": [],
        }
    )
    return rule


INT_TYPES = ["b", "B"]
INT_TYPES += ["<h", ">h", "<H", ">H"]
INT_TYPES += ["<i", ">i", "<I", ">I"]
INT_TYPES += ["<l", ">l", "<L", ">L"]
INT_TYPES += ["<q", ">q", "<Q", ">Q"]

def parse_integer(lnumber, type_, pattern):
    if type_ not in INT_TYPES:
        raise Exception("%d: Programmer error: %s not byte", (lnumber, type_))

    try:
        byte_value = int(pattern, 0)
        pattern_value = struct.pack(type_, byte_value)
    except struct.error as er:
        raise Exception("%d: struct err: %s" % (lnumber, str(er)))
    except ValueError as er:
        raise Exception("%d: value error: %s" % (lnumber, str(er)))

    value = "struct.pack(\"%s\", %s)" % (type_, pattern)

    rule = (
        pattern_value,
        {
            "type": type_,
            "value": value,
            "depends": ["struct"]
        }
    )
    return rule

HTON_TYPES = ["htons", "htonl"]

def parse_hton(lnumber, type_, pattern):
    if type_ not in HTON_TYPES:
        raise Exception("%d: Programmer error: %s not byte", (lnumber, type_))

    try:
        byte_value = int(pattern, 0)
    except ValueError as er:
        raise Exception("%d: value error: %s" % (lnumber, str(er)))

    value = "socket.%s(%s)" % (type_, pattern)
    rule = (
        pattern_value,
        {
            "type": type_,
            "value": value,
            "depends": ["socket"],
        }
    )
    return rule


def parse_line(lnumber, line):
    line = line.strip()

    if len(line) == 0 or line[0] == "#":
        return None

    rule = line.split(":", 1)
    if len(rule) != 2:
        raise Exception("Invalid Rule: %d" % (lnumber,))
    type_, pattern = rule

    if type_ in ASCII_TYPES:
        return parse_ascii(lnumber, type_, pattern)
    elif type_ in INT_TYPES:
        return parse_integer(lnumber, type_, pattern)
    elif type_ in HTON_TYPES:
        return parse_hton(lnumber, type_, pattern)
    else:
        raise Exception("Unknown type: %s" %(type_,))


def parse_file(f):
    rules = []
    for lnumber, line in enumerate(f.readlines()):
        rule = parse_line(lnumber, line)
        if rule is not None:
            rules += [rule]
    return rules


def load_types_file(filename):
    types = {}
    with open(filename, "rb") as f:
        rules = parse_file(f)
    return rules
