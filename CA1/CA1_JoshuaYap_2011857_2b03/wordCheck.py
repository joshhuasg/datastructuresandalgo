from printsHorizontal import option2h
class wordCheck():
    #values that are stored
    def __init__(self, word, coorX, coorY, frequency=1):
        self.__word = word
        self.__morse=option2h.encode(self.__word)
        self.__frequency = frequency
        #brackets are placed here for printing later
        self.__locations = [(coorX, coorY)]
        #for use in essential message, storing the first occurence of the word
        self.__initialX=coorX
        self.__initialY=coorY

    #if a word occurs more than once, this will be called
    def addNewLocation(self, coorX, coorY):
        self.__frequency = self.__frequency+1
        self.__locations.append((coorX, coorY))

    #custom split
    def split(self,x):
        return [self.__morse, self.__word, self.__frequency,
        self.__locations,self.__initialX,self.__initialY]

        #to check if a word as occured more than once
    def getWord(self):
        return self.__word
    
        

class analyse():
    def getFrequency(message):
        message=message.upper()
        message = message.split("\n")
        passedWords = []
        #loop considers the coorX (xth row), and coorY (yth position)
        for coorX in enumerate(message):
            #splits the row into words
            row = coorX[1].split(" ")
            for coorY in enumerate(row):
                #assumes that the new entry is true initially 
                newEntry = True
                #checks if word has occured before 
                for i in passedWords:
                    if coorY[1] == i.getWord():
                        #adds the new location
                        i.addNewLocation(coorX[0], coorY[0])
                        newEntry = False
                        break
                #if word has not occured prior
                if newEntry == True:
                    passedWords.append(wordCheck(coorY[1], coorX[0], coorY[0]))
        return passedWords