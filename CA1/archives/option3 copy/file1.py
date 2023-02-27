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
class option2h():
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

class Word():
    def __init__(self, word, x, y):
        self.__word = word.upper()
        self.__frequency = 1
        self.__locations = [(x, y)]
        self.__morse = ""
        self.__morse=option2h.encode(self.__word)
        self.__morse = self.__morse[:-1]

    def addLocation(self, x, y):
        self.__frequency += 1
        self.__locations.append((x, y))

    def getWord(self):
        return self.__word

    
    def split(self,x):
        return [self.__morse, self.__word, self.__frequency,self.__locations]
    

class analyze():
 def getFrequency(message):#message is the decoded thing
    message = message.split("\n")
    message = [x.split(" ") for x in message]
    saved = []
    for x, line in enumerate(message):
        for y, word in enumerate(line):
            newEntry = True
            for i in saved:
                if word.upper() == i.getWord():
                    i.addLocation(x, y)
                    newEntry = False
                    break
            if newEntry == True:
                saved.append(Word(word.upper(), x, y))
    return saved
import os
import re
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'morse_sos.txt')
file = open(filename, 'r')
content = file.read() #replace this to message you want to encode
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
        else: #in the event of a \n, , ect, it will be added into the decoded message here
            encodedWord += str(letter)
    return encodedWord
decoded = decode(new)
nnew=analyze.getFrequency(decoded)
print(nnew)
my_list = list(map(lambda x: x.split(' '), nnew))
print(my_list)
import pandas as pd
df = pd.DataFrame(my_list, columns =['morse', 'Word', 'Frequency', 'Position(S)'])


df=df.sort_values(by=['Frequency'])
print(df)