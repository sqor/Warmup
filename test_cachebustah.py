#!/usr/bin/python
'''
Unittest, testing the functionality of cachebustah.py.
'''

import unittest
import cachebustah

class Test_apply_fake_params(unittest.TestCase):

    def test_updated_text_correctly(self):
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

        new_contents = cachebustah.apply_fake_params(test_contents, 'fakehash')
        self.assertEquals(new_contents, expected_result)

class Test_rand_str(unittest.TestCase):

    def test_length(self):
        length = 12
        self.assertEquals(length, len(cachebustah.rand_str(length)))

    def test_type(self):
        self.assertTrue(isinstance(cachebustah.rand_str(), str))

if __name__ == '__main__':
    unittest.main()
