#!/usr/bin/python
'''
Condenses near-by javascript tags into one javascript tag.
'''
import bs4
import tempfile

SCRIPT_TAG_DELIMETER = "<script"
SRC_DELIMETER = "src="

SCRIPT_TAG_DELIMETER = "<script"

def is_url(src_raw):

    if src_raw.find("http") == -1:
        return src_raw

def get_script_src(line):
    '''
    Get src from script tag. If none found, return None.

    @arg line str
        Line to retrieve SRC (<script src='SRC'...) from.

    @return str
        src from script tag if found. otherwise return None.
    '''
    # does <script exist in line?
    soup = bs4.BeautifulSoup(line)

    # does script tag exist in line?
    if soup.script is None:
        return None

    # does src attribute exist in script tag?
    return soup.script.get('src')

def generate_combined_src_file(srcs):
    ''''''
    # given srcs
    # get contents of each src file
    # write those contents to a new file
    # new file filename is randomly generated.
    tempfile.mkstemp(prefix='compiled_', suffix='.js')

def combine_src_strings(srcs):
    # create js file
    #   contents of file are contents of each src file
    return "<script src='%s'></script>\n" % ('goog.com')

def minimize_file_srcs(input_file):
    lines = open(input_file, "r")

    new_lines = []
    script_sources = []
    for line in lines:
        src = get_script_src(line)

        # if we're entering a script-src block, append script src to sources
        # list.
        if src:
            script_sources.append(src)

        # if we are not in a script block, add text to new_lines list.
        else:
            # if we left a script block, combine script src's into a js file
            # and append script tag as a script src=js tag.
            if script_sources:
                # Write out our compiled css
                new_lines.append(combine_src_files(script_sources))
                script_sources = []

            new_lines.append(line)

    #@TODO: apply the lines that may still exist in script_sources.

    return new_lines

def main():
    # Read file and parse
    new_lines = minimize_file_srcs('index.html')
    # Write File
    f = open('index3.html','w')
    for line in new_lines:
        f.write(line)
    f.close()


if __name__  == '__main__':
    main()
