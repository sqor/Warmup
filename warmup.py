newLines= []
savedProdLines = []
localLines = []

START_LOCAL_DELIMETER = "<!--:START-LOCAL:-->"
END_LOCAL_DELIMETER = "<!--:END-LOCAL:-->"

START_PROD_DELIMETER =  "<!--::START-PROD::"
END_PROD_DELIMETER = "::END-PROD::-->"


IS_LOCAL = False

def readFile():
    global IS_LOCAL

    lines = open( "index.html", "r" )
    array = []
    for line in lines:

        # First we make sure to remove the old prod comments
        # so the lines in between can show
        if line.find(START_PROD_DELIMETER) >=0:
            line = next(lines)

        if line.find(END_PROD_DELIMETER) >=0:
            line = next(lines)

        # Next we make sure to now ignore all the local script tags
        if line.find(START_LOCAL_DELIMETER) >=0:
            IS_LOCAL = True

        if line.find(END_LOCAL_DELIMETER) >=0:
            IS_LOCAL = False
            line = ""

        if IS_LOCAL:
            localLines.append( line )
        else:
            newLines.append( line )



# Read file and parse
readFile()
# Write File
f = open('index2.html','w')
for line in newLines:
    f.write(line)
f.close()



