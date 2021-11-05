
#This will search for the names of famous soccer players
import re

def find_name(line):
    pattern = r"(M|A|K)\.?( [A-Z][a-z]*)( [A-Z][A-Za-z]*)*"
    result = re.findall(pattern,line)

    pattern = r"Roberto Carlos"
    result = result + re.findall(pattern,line)
    return result

f = open("namefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
        
        
