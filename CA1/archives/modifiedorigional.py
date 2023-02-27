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
filename = os.path.join(here, 'text_sos.txt')
file = open(filename, 'r')
content = file.read() #replace this to message you want to encode



# encoding function
def encode(data):
    encodedWord = ''
    mCoded = []
    for letter in data:
        if letter.isalpha():
            morseLetter = ''.join(str(item) for innerlist in morse[letter] for item in innerlist)
            mCoded.append(morseLetter)
        elif letter.isnumeric():
            morseLetter = ''.join(str(item) for innerlist in morse[letter] for item in innerlist)
            mCoded.append(morseLetter)
        else: #non-letter items here, such as \n and spaces
            mCoded.append(morseLetter)
    #combining the morse
    for letter in range (len(mCoded)):
        if mCoded[letter]!='\n':#check for morse
            if letter != 0:#check for if the morse is not index 0, which means that it is not at start
                if '\n' in mCoded: #check if there is '\n'
                    if letter !=(mCoded.index('\n')+1):
                        encodedWord += "," + mCoded[letter]
                    else: #if word comes after an "\n", dont add a ","
                        encodedWord +=  mCoded[letter]
                else:
                    encodedWord += "," + mCoded[letter]
            else: #if index==0, do not add a "," before
                encodedWord +=  mCoded[letter]
        else: #if an "\n", it will be added here
            encodedWord+=mCoded[letter]
    return encodedWord


coded = encode(content)
print(coded)

# decoding part, opeing file
filename = os.path.join(here, 'morse_sos.txt')
file1 = open(filename, 'r')
content = file1.read()

morseTxt = re.split('([,|\n])', content) #input coded message here, splits string by the ',' and '\n', keeps them after seperation
#the line above seperates the string with seperators ',' or '\n' in this case
noC = list(filter(lambda a: a != ',', morseTxt)) #removes ',', since not needed
print(noC)
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
