#!/usr/bin/python
import unittest
import js_minimizer
from mock import patch

class Test_get_script_src(unittest.TestCase):
    def test_script_src_is_correct(self):
        value = 'value'
        line = "<script src='%s'></script>" % (value)
        src = js_minimizer.get_script_src(line)
        self.assertEquals(src, value)

    def test_script_src_is_None(self):
        line = "<script></script>"
        src = js_minimizer.get_script_src(line)
        self.assertEquals(src, None)

    def test_fake_tag(self):
        line = "<foo></foo>"
        src = js_minimizer.get_script_src(line)
        self.assertEquals(src, None)

    def test_bad_data(self):
        line = "blabhalbhalbahb"
        src = js_minimizer.get_script_src(line)
        self.assertEquals(src, None)

    def test_br(self):
        line = "<br>"
        src = js_minimizer.get_script_src(line)
        self.assertEquals(src, None)

class Test_minimize_file_srcs(unittest.TestCase):

    @patch('__builtin__.open')
    def test_collects_non_script_lines(self, open_mock):
        sample_html = "<html>\n</html>"
        open_mock.return_value = sample_html.split('\n')
        new_lines = js_minimizer.minimize_file_srcs('')
        self.assertEquals(new_lines, sample_html.split('\n'))

if __name__ == '__main__':
    unittest.main()
