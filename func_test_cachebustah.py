#!/usr/bin/python
'''
Unittest, testing the functionality of cachebustah.py.
'''

import os
import unittest
import cachebustah
import tempfile
from mock import patch

class Test_apply_fake_params(unittest.TestCase):

    def setUp(self):
        test_contents = '''<!DOCTYPE html>
<html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.js"></script>
        <link rel="stylesheet" href="/css/main.css">
    </head>
    <body>
        <!--CACHE-BUSTAH-START-->
        <script src="/javascript/tempHack.js"></script>
        <!--CACHE-BUSTAH-END-->
    </body>
</html>
'''
        self.test_file = tempfile.mkstemp(dir='/var/tmp', suffix='.html')[1]
        with open(self.test_file, 'w') as fh:
            fh.write(test_contents)

    def tearDown(self):
        os.remove(self.test_file)

    @patch('cachebustah.rand_str')
    def test_updated_text_correctly(self, rand_str_mock):
        expected_result = '''<!DOCTYPE html>
<html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.js"></script>
        <link rel="stylesheet" href="/css/main.css?fakehash=fakehash">
    </head>
    <body>
        <script src="/javascript/tempHack.js?fakehash=fakehash"></script>
    </body>
</html>
'''
        rand_str_mock.return_value = 'fakehash'
        cachebustah.sys.argv = ['script', self.test_file]
        cachebustah.main()
        with open(self.test_file, 'r') as fh:
            self.assertEquals(fh.read(), expected_result)

if __name__ == '__main__':
    unittest.main()
