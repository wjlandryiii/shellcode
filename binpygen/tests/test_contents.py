#
# Copyright 2014 Joseph Landry
#

import unittest

import binpygen

class TestContents(unittest.TestCase):
    def test_contents(self):
        f = open("tests/test_contents.py", "rb")
        contents = f.read()
        f.close()
        self.assertEqual(contents, binpygen.read_bin("tests/test_contents.py"))
