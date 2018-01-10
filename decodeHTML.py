"""Takes input of json file. Decodes base64 encoded HTML file at each line 
in the JSON file. Outputs all decoded HTML into single output file."""

import base64
import json
from pprint import pprint

decoder = json.JSONDecoder()
decodedList = []

i = 0 #line counter

with open('2016scraped-traintest27.json') as fin: #open input file
    for line in fin.readlines():
    	#decode HTML lines
        decodedHTML = base64.b64decode(decoder.decode(line)['html_base64'])
        print("decoded", i) #track how many lines have been updated
        decodedList.append(decodedHTML) #add decoded HTML to list
        i += 1
		
j = 0 #line counter

#write decoded HTML to file
outputFile = open('2016scraped-traintest27decoded.html', 'w')
for item in decodedList:
    outputFile.write("%s\n" % item)
    print("output", j)
    j += 1

    
    
