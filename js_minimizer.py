import bs4

scriptSources = []
newLines = []

SCRIPT_TAG_DELIMETER = "<script"
SRC_DELIMETER = "src="

SCRIPT_TAG_DELIMETER = "<script"

SCRIPT_BLOCK= False

def get_script_src(line):
    if line.find(SCRIPT_TAG_DELIMETER) >=0:
        pass
    return None

def readFile():
    global SCRIPT_BLOCK

    lines = open( "index.html", "r" )
    array = []
    for line in lines:
        pass

# Read file and parse
readFile()
# Write File
f = open('index2.html','w')
for line in newLines:
    f.write(line)
f.close()



