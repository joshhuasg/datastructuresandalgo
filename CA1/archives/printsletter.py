import os
import re
import numpy as np
# dictonary for letter/number to morse
morse = {'A': [['.','-']], 'B': [['-','.','.','.']], 'C': [['-','.','-','.']], 'D': [['-','.','.']], 
        'E': [['.']], 'F': [['.','.','-','.']], 'G': [['-','-','.']],
        'H': [['.','.','.','.']], 'I':[[ '.','.']], 'J': [['.','-','-','-']], 'K': [['-','.','-']],
        'L': [['.','-','.','.']],
        'M': [['-','-']], 'N': [['-','.']],
        'O': [['-','-','-']], 'P': [['.','-','-','.']], 'Q': [['-','-','.','-']], 
        'R': [['.','-','.']], 'S': [['.','.','.']], 
        'T': [['-']], 'U': [['.','.','-']],
        'V': [['.','.','.','-']], 'W': [['.','-','-']], 'X': [['-','.','.','-']], 
        'Y': [['-','.','-','-']], 'Z': [['-','-','.','.']],
        '0': [['-','-','-','-','-']], '1': [['.','-','-','-','-']], '2': [['.','.','-','-','-']], 
        '3': [['.','.','.','-','-']], '4': [['.','.','.','.','-']], '5': [['.','.','.','.','.']],
        '6': [['-','.','.','.','.']], '7': [['-','-','.','.','.']], '8': [['-','-','-','.','.']], 
        '9': [['-','-','-','-','.']]
         }

# reading file that has message to be encoded
here = os.path.dirname(os.path.abspath(__file__))
# decoding part, opeing file
filename = os.path.join(here, 'morse_sos.txt')
file1 = open(filename, 'r')
content = file1.read()

morseTxt = re.split('([,|\n])', content) #input coded message here, splits string by the ',' and '\n', keeps them after seperation
#the line above seperates the string with seperators ',' or '\n' in this case
noC = list(filter(lambda a: a != ',', morseTxt)) #removes ',', since not needed
new=[]
l=0
for i in noC:
    if [list(noC[l])] in morse.values():
        new.append([list(noC[l])])
    else:
        new.append(noC[l])
    l+=1

# decoding function
def decode(data):
    encodedWord = ''
    for letter in data:
        if letter in morse.values():#checks if letter is in the values
            indexL=list(morse.values()).index(letter) #index of matching value
            encodedLetter = list(morse.keys())[indexL] #key of index obtained above
            encodedWord += encodedLetter
        else: #in the event of a \n, \t, ect, it will be added into the decoded message here
            encodedWord += str(letter)
    return encodedWord


decoded = decode(new)
print(decoded)
