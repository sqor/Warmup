#!/usr/bin/python
'''
Condenses near-by javascript tags into one javascript tag.
'''
import bs4

newLines = []

SCRIPT_TAG_DELIMETER = "<script"
SRC_DELIMETER = "src="

SCRIPT_TAG_DELIMETER = "<script"

def get_script_src(line):
    src = None
    if line.find(SCRIPT_TAG_DELIMETER) >=0:
        soup = bs4.BeautifulSoup(line)
        if soup.script is not None:
            srcRaw = soup.script.get('src')
            # We want to ignore remote files
            if srcRaw is not None:
                if srcRaw.find("http") == -1:
                    src = srcRaw

    return src


def write_file():
    src = "google.com"
    return "<script src='%s'></script>\n" % (src)

def read_file():
    scriptSources = []
    SCRIPT_BLOCK = False
    lines = open( "index.html", "r" )
    array = []
    for line in lines:
        src = get_script_src(line)
        if src:
            SCRIPT_BLOCK = True
            scriptSources.append(src)
        else:
            SCRIPT_BLOCK = False
        if len(scriptSources)> 0  and not SCRIPT_BLOCK:
            # Write out our compiled css
            new_script_tag = write_file()
            scriptSources = []
            newLines.append(new_script_tag)
        # Write the line out
        if not SCRIPT_BLOCK:
            newLines.append(line)

def main():
    # Read file and parse
    read_file()
    # Write File
    f = open('index3.html','w')
    for line in newLines:
        f.write(line)
    f.close()


if __name__  == '__main__':
    main()
