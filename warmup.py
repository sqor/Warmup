newLines= []
savedProdLines = []
localLines = []

START_LOCAL_DELIMETER = "<!--:START-LOCAL:-->"
END_LOCAL_DELIMETER = "<!--:END-LOCAL:-->"

START_PROD_DELIMETER = "<!--:START-PROD::"
END_PROD_DELIMETER = "::END-LOCAL::-->"


IS_LOCAL = False
IS_PROD = False

def readFile():
    lines = open( "index.html", "r" )
    array = []
    for line in lines:

        # First we make sure to remove the old prod comments
        # so the lines in between can show
        if line.find(START_PROD_DELIMETER) >=0:
            IS_PROD = True
            next(lines)

        if line.find(END_PROD_DELIMETER) >=0:
            IS_PROD = False
            next(lines)

        # Next we make sure to now ignore all the local script tags
        if line.find(START_LOCAL_DELIMETER) >=0:
            IS_LOCAL = True
            next(lines)

        if line.find(END_LOCAL_DELIMETER) >=0:
            IS_LOCAL = False
            next(lines)

        if not IS_LOCAL:
            newLines.append( line )
        else:
            localLines.append( line )



import pprint

readFile()
pprint.pprint(savedProdLines)




