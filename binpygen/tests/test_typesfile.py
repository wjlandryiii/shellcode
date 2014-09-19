#
# Copyright 2014 Joseph Landry
#

import unittest
import typesfile

class TestParseElements(unittest.TestCase):
    def test_parse_ascii(self):
        rule = typesfile.parse_ascii(0, "ascii", "\"Hello World!\\n\\x00\"")
        self.assertEqual("Hello World!\n\x00", rule[0])
        pattern_dict = rule[1]
        type_ = pattern_dict["type"]
        self.assertEqual(type_, "ascii")
        value = pattern_dict["value"]
        self.assertEqual(value, "\"Hello World!\\n\\x00\"")

        with self.assertRaises(Exception) as ex:
            typesfile.parse_ascii(0, "ascii", "\"durp")

        with self.assertRaises(Exception) as ex:
            typesfile.parse_ascii(0, "ascii", "durp\"")

        with self.assertRaises(Exception) as ex:
            typesfile.parse_ascii(0, "ascii", "durp")

    def test_parse_integer(self):
        rule = typesfile.parse_integer(0, "b", "4")
        self.assertEqual("\x04", rule[0])
        pattern_dict = rule[1]
        type_ = pattern_dict["type"]
        self.assertEqual(type_, "b")
        value = pattern_dict["value"]
        self.assertEqual(value, "struct.pack(\"b\", 4)")

        rule = typesfile.parse_integer(0, "b", "-4")
        self.assertEqual("\xFC", rule[0])
        pattern_dict = rule[1]
        self.assertEqual(pattern_dict["type"], "b")
        value = pattern_dict["value"]
        self.assertEqual(value, "struct.pack(\"b\", -4)")

        rule = typesfile.parse_integer(0, "B", "0xFF")
        self.assertIn("\xFF", rule[0])
        pattern_dict = rule[1]
        self.assertEqual(pattern_dict["type"], "B")
        value = pattern_dict["value"]
        self.assertEqual(value, "struct.pack(\"B\", 0xFF)")

        with self.assertRaises(Exception) as ex:
            typesfile.parse_integer(0, "b", "aaa")
        with self.assertRaises(Exception) as ex:
            typesfile.parse_integer(0, "b", "256")



class TestParseLine(unittest.TestCase):
    def test_line_ascii(self):
        rule = typesfile.parse_line(0, "ascii:\"Hello World!\n\x00\"")
        self.assertIn("Hello World!\n\x00", rule)

    def test_line_integer(self):
        rule = typesfile.parse_line(0, "b:0x45")
        self.assertEqual("\x45", rule[0])
        self.assertEqual(rule[1]["type"], "b")
        self.assertEqual(rule[1]["value"], "struct.pack(\"b\", 0x45)")

        rule = typesfile.parse_line(0, "B:0x85")
        self.assertEqual("\x85", rule[0])
        self.assertEqual(rule[1]["type"], "B")
        self.assertEqual(rule[1]["value"], "struct.pack(\"B\", 0x85)")

    def test_line_unknown(self):
        with self.assertRaises(Exception) as ex:
            typesfile.parse_line(0, "xxx:example.com")
