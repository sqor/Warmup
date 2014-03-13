oldLines = []
savedProdLines = []

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


        if line.find(START_PROD_DELIMETER) >=0:
            IS_PROD = True
            next(lines)

        if line.find(END_PROD_DELIMETER) >=0:
            IS_PROD = False
            next(lines)



        if IS_PROD:
            if not IS_LOCAL:
                oldLines.append( line )
                    #savedProdLines.append( line )

        if line.find(START_LOCAL_DELIMETER) >=0:
            IS_LOCAL = True

        if line.find(END_LOCAL_DELIMETER) >=0:
            IS_LOCAL = False


        if line.find(END_PROD_DELIMETER) >=0:
            IS_PROD = False




import pprint

readFile()
pprint.pprint(savedProdLines)




