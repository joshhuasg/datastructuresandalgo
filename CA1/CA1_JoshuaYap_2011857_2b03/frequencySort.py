from essentialSort import Node

class wordClass(Node):
    #initialise values
    def __init__(self, word, morseWord, locations,freq):
        self.word = word
        self.freq=freq
        self.locations=locations
        self.morseWord=morseWord
        super().__init__()
    #checks if words have different frequencies, then their length, then their alphabet order
    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError('\'<\' not supported between instances of \'AnalyzeWord\' and \'NoneType\'')

        elif self.freq == otherNode.freq:
            if len(str(self.word)) == len(str(otherNode.word)):
                return str(self.word).upper() < str(otherNode.word).upper()
            else:
                return len(str(self.word)) < len(str(otherNode.word))

        return self.freq > otherNode.freq

    def __str__(self):
        s= f'{self.morseWord}\n [{self.word}] ({self.freq}) {self.locations}\n'
        return s
    



class sortedListF:

    def __init__(self):
        self.headNode = None
        self.currentNode = None
        
    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        

    def insert(self, newNode):
        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return

        # Check if it is going to be new head
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return
        #goes to next nodes
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None:
            if newNode == rightNode:
                if newNode < rightNode:
                    leftNode.nextNode = newNode
                    newNode.nextNode = rightNode
                    return
            elif newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode

    # When there is one wordFreq left, it will have to be added to the end
        leftNode.nextNode = newNode
    def __str__(self):
        # We start at the head
        output =''
        node= self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = f"Words with frequency: {node.freq}\n"+node.__str__()
                firstNode = False
            else:
                output += (' ' + node.__str__())
            currentNode=node
            node = node.nextNode
            if node != None:
                if currentNode.freq>node.freq:
                    output+=(f"Words with frequency: {node.freq}\n")
        return output+' '

#inserts each word and its corresponding information
class startSortF:
    def sort(wordFreqs,l):
        for wordFreq in wordFreqs:
            l.insert(wordClass(wordFreq[0],wordFreq[1],wordFreq[2],wordFreq[3]))   
        return(l)


class startWord:
    #initialises sortedListF
    def startWordSort(listThings):
        l = sortedListF()
        filteredMessage=startSortF.sort(listThings,l)
        return filteredMessage

