#!/usr/bin/python
'''
Attempts to block chrome's caching mechanism by inserting fake
parameters/arguments in the GET fields for the script tag src files.
Takes an html file and rewrites that html file with the fake GET params.
'''
import sys
import argparse
import random
import string

START_JS_CACHE = "<!--CACHE-BUSTAH-START-->"
END_JS_CACHE = "<!--CACHE-BUSTAH-END-->"

def parse_args(input_args):
    '''
    Parse the command line arguments and return an object containing the
    arguments.

    PARAM input_args list
        List of input arguments to parse.
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('input_html_file',
      help='HTML file to rewrite with script tag random string hash.')

    return parser.parse_args(input_args)

def rand_str(str_len=5):
    '''
    Create a random sequence of letters and numbers and return it as a string.

    PARAM str_len int
        Length of the random string to return.

    RETURN str
        String of random letters and numbers of given length.
    '''
    char_set = string.ascii_uppercase + string.digits
    return ''.join(random.sample(char_set*6, str_len))

def apply_fake_params(html_contents, fake_hash):
    '''
    Given html file contents, append fake string arguments to specific script
    src's.

    Applies to:
        js src's between the CACHE-BUSTAH-START and CACHE-BUSTAH-END comments.
        main.css

    PARAM html_contents str
        String to apply fake string args to specific script src's.

    PARAM fake_hash str
        String to apply to specific script src's GET args.

    RETURN str
        Updated html_contents with fake hash applied to specific script src's
        GET args.
    '''
    # updated main.css in html contents
    updated_html_contents = html_contents.replace(
      "main.css", "main.css?%s=%s" % (fake_hash, fake_hash))

    file_top, js_lines = updated_html_contents.split(START_JS_CACHE)
    js_lines, file_bottom = js_lines.split(END_JS_CACHE)

    # update the js lines with fake hash
    updated_js_lines = js_lines.replace(
      '.js', '.js?%s=%s' % (fake_hash, fake_hash))

    return file_top.rstrip() + updated_js_lines.rstrip() + file_bottom

def update_html_file(input_html_file):
    '''
    Read given html file and add fake GET args on specific script src files.

    PARAM input_html_file str
        html file to update.
    '''
    # retrieve given files' contents and run string manipulation
    with open(input_html_file, 'r') as html_fh:
        new_contents = apply_fake_params(html_fh.read(), rand_str())

    # write string to old filename
    with open(input_html_file, 'w') as html_fh:
        html_fh.write(new_contents)

    #@TODO: make temp file?

def main():
    '''
    Given html file, append specific script filenames with a random string
    sequence.

    i.e.
        <script src="/javascript/runner.js"></script>

        becomes:
        <script src="/javascript/runner.js?rAnD0M=rAnD0M"></script>

    Then write updated text back into given file.
    Write a temp copy of the original file.
    '''
    # get the commandline arguments
    args = parse_args(sys.argv[1:])

    update_html_file(args.input_html_file)

if __name__ == '__main__':
    main()
