import os
import re
from morseDict import morse

# reading file that has message to be encoded
here = os.path.dirname(os.path.abspath(__file__))
# decoding part, opeing file
class decodeMorse():
    def decodePrep(fileInput):
        filename = os.path.join(here, fileInput)
        file = open(filename, 'r')
        content = file.read()
        
        morseTxt = re.split('([,|\n])', content) 
        #the line above seperates the string with seperators ',' or '\n' in this case
        noC = list(filter(lambda a: a != ',', morseTxt)) #removes ',', since not needed
        new=[]
        l=0
        #checks if it is a possible morse
        for i in noC:
            if [list(noC[l])] in morse.values():
                new.append([list(noC[l])])
            else:
                new.append(noC[l])
            l+=1
        
        return decodeMorse.decode(new)
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
