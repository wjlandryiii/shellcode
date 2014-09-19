#
# Copyright 2014 Joseph Landry
#

import unittest
import StringIO
import sourcegen

class TestSourceGen(unittest.TestCase):
    def test_generate_undefined(self):
        sio = StringIO.StringIO()
        sourcegen.generate_undefined(sio, "\x00\x11\x22")
        value = sio.getvalue()
        self.assertEqual(value, "shellcode += \"\\x00\\x11\\x22\"\n")

        sio = StringIO.StringIO()
        sourcegen.generate_undefined(sio, "\x00\x11\x22\x33\x44\x55\x66\x77"\
                "\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF")
        value = sio.getvalue()
        self.assertEqual(value, "shellcode += \""\
                "\\x00\\x11\\x22\\x33\\x44\\x55\\x66\\x77"\
                "\\x88\\x99\\xAA\\xBB\\xCC\\xDD\\xEE\\xFF\"\n")

        sio = StringIO.StringIO()
        sourcegen.generate_undefined(sio, "\x00\x11\x22\x33\x44\x55\x66\x77"\
                "\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF")
        value = sio.getvalue()
        self.assertEqual(value, "shellcode += \""\
                "\\x00\\x11\\x22\\x33\\x44\\x55\\x66\\x77"\
                "\\x88\\x99\\xAA\\xBB\\xCC\\xDD\\xEE\\xFF\"\n")

        sio = StringIO.StringIO()
        sourcegen.generate_undefined(sio, "\x00\x11\x22\x33\x44\x55\x66\x77"\
                "\x88\x99\xAA\xBB\xCC\xDD\xEE\xFF\x01");
        value = sio.getvalue()
        self.assertEqual(value, "shellcode += \""\
                "\\x00\\x11\\x22\\x33\\x44\\x55\\x66\\x77"\
                "\\x88\\x99\\xAA\\xBB\\xCC\\xDD\\xEE\\xFF\"\n"\
                "shellcode += \"\\x01\"\n")

        sio = StringIO.StringIO()
        sourcegen.generate_undefined(sio, \
                "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E"\
                "\x0F"\
                "\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E"\
                "\x1F")
        value = sio.getvalue()
        self.assertEqual(value, "shellcode += \""\
                "\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07"\
                "\\x08\\x09\\x0A\\x0B\\x0C\\x0D\\x0E\\x0F\"\n"\
                "shellcode += \""\
                "\\x10\\x11\\x12\\x13\\x14\\x15\\x16\\x17"\
                "\\x18\\x19\\x1A\\x1B\\x1C\\x1D\\x1E\\x1F\"\n")

        sio = StringIO.StringIO()
        sourcegen.generate_undefined(sio, \
                "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E"\
                "\x0F"\
                "\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E"\
                "\x1F\x20")
        value = sio.getvalue()
        self.assertEqual(value, "shellcode += \""\
                "\\x00\\x01\\x02\\x03\\x04\\x05\\x06\\x07"\
                "\\x08\\x09\\x0A\\x0B\\x0C\\x0D\\x0E\\x0F\"\n"\
                "shellcode += \""\
                "\\x10\\x11\\x12\\x13\\x14\\x15\\x16\\x17"\
                "\\x18\\x19\\x1A\\x1B\\x1C\\x1D\\x1E\\x1F\"\n"\
                "shellcode += \"\\x20\"\n")

    def test_generate_data(self):
        sio = StringIO.StringIO()
        sourcegen.generate_data(sio, {"value": "foo"})
        value = sio.getvalue()
        self.assertEqual(value, "shellcode += foo\n")

    def test_collect_depends(self):
        sio = StringIO.StringIO()
        datas = [
            ('d', {"depends": []}),
            ('d', {"depends": ["struct"]}),
            ('d', {"depends": ["struct"]}),
            ('d', {"depends": ["socket", "struct"]}),
        ]
        deps = sourcegen.collect_depends(datas)
        self.assertIn("struct", deps)
        self.assertIn("socket", deps)

    def test_generate_source(self):
        datas = [
            ('u', "\x00\x11\x22\x33\x44"),
            ('d', {"value": "daste", "depends": ["foo","bar"]})
        ]
        test_source = sourcegen.generate_source(datas)
        print test_source
        source = "import bar\n"\
                "import foo\n"\
                "\n"\
                "shellcode = \"\"\n"\
                "shellcode += \"\\x00\\x11\\x22\\x33\\x44\"\n"\
                "shellcode += daste\n"
        print source
        self.assertEqual(test_source, source)
