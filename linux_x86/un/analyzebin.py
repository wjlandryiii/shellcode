#!/usr/bin/python
#
# Copyright 2014 Jospeh Landry
#

def usgae():
    print "analyzebin.py [filename]"

def main(argv):
    if len(argv) < 2:
        usage()
        return 1
    with open(argv[1], "rb") as f:
        contents = f.read()
    stats = {}
    for x in contents:
        key = ord(x)
        if key in stats:
            stats[key] += 1
        else:
            stats[key] = 1
    keys = sorted(stats.keys())

    for key in keys:
        filelen = len(contents)
        n = stats[key]
        print "%02X: %3d %s" % (key, n, "*" * int(75 * n / filelen))
    return 0


if __name__ == "__main__":
    import sys
    status = main(sys.argv)
    sys.exit(status)
