import random
import string
newLines = []
localLines = []

START_JS_CACHE = "<!--CACHE-BUSTAH-START-->"
END_JS_CACHE = "<!--CACHE-BUSTAH-END-->"

def get_rand_str():
    char_set = string.ascii_uppercase + string.digits
    return ''.join(random.sample(char_set*6, 6))

def read_file():
    IS_LOCAL = False

    lines = open( "index2.html", "r" )
    array = []

    rand_ = get_rand_str()
    for line in lines:



        # Next we make sure to now ignore all the local script tags
        if line.find(START_JS_CACHE) >=0:
            IS_LOCAL = True
            line = ""

        if line.find(END_JS_CACHE) >=0:
            IS_LOCAL = False
            line = ""

        line =  line.replace("main.css", "main.css?" + str(rand_ ) + "=" + str(rand_));
        if IS_LOCAL:
            line =  line.replace(".js", ".js?"  + str(rand_ ) + "=" + str(rand_) );
            newLines.append( line )

        else:
            newLines.append( line )

# Read file and parse
read_file()
# Write File
f = open('index.html','w')
for line in newLines:
    f.write(line)
f.close()



