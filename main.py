import sys
from afd import processFile

def printFile(file):
    line = file.readline()
    while line != "":
        print(line, end="")
        line = file.readline()
    
if len(sys.argv) < 2:
    print("No input file.")
    exit(1)

file = open(sys.argv[1])
output = processFile(file)
file.close()

if len(sys.argv) > 2 and output != None:
    output_file = open(sys.argv[2], 'w')
    output_file.write(output)
    output_file.close()