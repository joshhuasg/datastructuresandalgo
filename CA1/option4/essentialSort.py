class Node:
    # Constructor
    def __init__(self):
        self.nextNode = None

class wordMessage(Node):
    #required information
    def __init__(self,word,frequency,coorX,coorY):
        self.word = word
        self.freq = frequency
        self.coorX = coorX
        self.coorY = coorY
        super().__init__()


    def __lt__(self, otherNode):
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'wordSet' and 'NoneType'")
        #comparison checks for the essential message
        elif self.freq == otherNode.freq:
            if self.coorX == otherNode.coorX:
                return self.coorY < otherNode.coorY
            else:
                return self.coorX < otherNode.coorX
        return self.word < otherNode.word
    #output per word node
    def __str__(self):
        s= f'{self.word}'
        return s



class sortedListE:

    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0
    #cheks for first node, filters out if in stop_words.txt
    def __appendToHead(self, newNode):
        if  self.headNode.word not in filterList:
            oldHeadNode = self.headNode
            self.headNode = newNode
            self.headNode.nextNode = oldHeadNode
            self.length += 1

    #insert function
    def insert(self, newNode):
        self.length += 1
        if newNode.word not in filterList:
            # If list is currently empty
            if self.headNode == None:
                self.headNode = newNode
                return

            # Check if it is going to be new head
            if newNode > self.headNode:
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

    # When there is one wordSet remaining, it will have to be added to the end
            leftNode.nextNode = newNode
    #printing of the output
    def __str__(self):
        # We start at the head
        output =""
        node= self.headNode
        firstNode = True
        output=[]
        while node != None:
            if firstNode:
                output = " "+node.__str__()
                firstNode = False
            else:
                output += (' ' + node.__str__())
            node= node.nextNode
        return output+" "
#initialises the sort using a for loop
class startSort:
    def sort(wordSets,l):
        for wordSet in wordSets:
            l.insert(wordMessage(wordSet[0],wordSet[1],wordSet[2],wordSet[3]))
        return(l)

import os 
#initialises the classes needed for determining essntial message 
class startEssentialClass:
    def startEssential(listThings):
        #opens the stop words file 
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'stop_words.txt')
        f = open(filename, "r")
        stopWords=f.read().upper()
        #makes the list of stop words global, so it does not need to be manually passed into the above classes
        global filterList
        filterList=stopWords.split('\n')
        #initialises SortedList
        l = sortedListE()
        #starting sort
        filteredMessage=startSort.sort(listThings,l)
        return filteredMessage
