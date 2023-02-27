from printsLetter import decodeMorse
from wordCheck import analyse
from essentialSort import startEssentialClass
from frequencySort import startWord
import pandas as pd
import os
here = os.path.dirname(os.path.abspath(__file__))

#base code for option3
class option3Class():
    def option3Code(inFile, outName):
        decoded=decodeMorse.decodePrep(inFile)
        stringList=''
        #for decoded message
        print('\n'*2,'*'*3,'Decoded Morse Text')
        print(decoded)
        stringList+=decoded
        #for analysis
        outPutCheck=analyse.getFrequency(decoded)
        my_list = list(map(lambda x: x.split(' '), outPutCheck))
        df = pd.DataFrame(my_list[:-1], columns =['morse', 'Word', 'Frequency', 'Locations','Initial X', 'Initial Y'])
        #for frequency
        dfWords=df[['Word','morse','Locations','Frequency']]
        WordsList=dfWords.values.tolist()
        frequency=startWord.startWordSort(WordsList)
        print(frequency)
        stringList+=str(frequency)
        #for essential
        dfCoor=df[['Word','Frequency', 'Initial X', 'Initial Y']]
        listCoor=dfCoor.values.tolist()
        messageE=startEssentialClass.startEssential(listCoor) 
        print('\n'*2,'*'*20,'\nEssential Message')
        print(messageE)
        stringList=stringList+'\n ***Essential Message'+'\n'+str(messageE)
        #for output
        currentLocation=os.path.join(here,outName)
        f= open(currentLocation,"w+")
        f.write(stringList)