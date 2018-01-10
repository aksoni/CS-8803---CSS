"""Takes input of text file with website text and writes lines that have
killing or police keywords to a new file. Only writes a line to file if it starts 
with an alphabetic character."""

outputFile = open('2016scraped-traintest18KeywordOutput2.txt', 'w', encoding='utf-8')

#killing and police keyword list
keywords = ["kill", "kills", "killing", "killings", "killed", "shot", 
"shots", "shoot", "shoots", "shooting", "murder", "murders", "murdered", 
"beat", "beats", "beating", "beaten", "fatal", "homicide", "homicides", 
"fire", "police", "officer", "officers", "cop", "cops", "detective", 
"sheriff", "policeman", "policemen", "constable", "patrolman", "sergeant", 
"detectives", "patrolmen", "policewoman","constables", "trooper", 
"troopers", "sergeants", "lieutenant", "deputies", "deputy"]

#Check if line has any keywords and if it starts with an alphabetic character.
#If it does, then the line is written to a file.
with open('2016scraped-traintest18text.txt', 'r', encoding="utf8") as handle:
    for line in handle:
        for key in keywords:
            if key in line:
                line = line.lstrip(' ')
                if line and line[0].isalpha() and not line.startswith('o [') and not line.startswith('Headlines'):
                    outputFile.write(line)
                
 
