class SortedList: 
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0 
    def __appendToHead(self, newNode): 
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode 
        self.length += 1
    def insert(self, newNode): 
        self.length += 1 
        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return 
        # Check if it is going to be new head 
        if newNode < self.headNode: 
            self.__appendToHead(newNode)
            return 
        # Check it is going to be inserted between any pair of Nodes (left,right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        while rightNode != None: 
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode
            # Once we reach here it must be added at the tail
        leftNode.nextNode = newNode
    #for checking purposes
    def __str__(self):
        output =""
        node= self.headNode
        ans = node.ans
        prevans = node.ans+1
        firstNode = True
        count = 0
        while node != None:
            ans = node.ans
            if prevans != ans:
                if count == 0:
                    output += (f'*** Expressions with value => {ans}')
                #whenever new count, print this
                else:
                    output += (f'\n\n*** Expressions with value => {ans}')
            if ans == node.ans:
                if firstNode:
                    output += ('\n'+ node.__str__())
                    firstNode = False
                else:
                    output += ('\n' + node.__str__())
            count+=1
            node= node.nextNode
            prevans = ans
        return output