from option2Node import Node

class Analyze(Node): 
    def __init__(self, eqn, freq, count, ans):
        self.eqn = eqn
        self.freq = freq
        self.count = count
        self.ans = ans
        super().__init__() 
    def __eq__(self, otherNode): 
        if otherNode == None:
            return False
        else: 
            return self.ans == otherNode.ans 
    def __str__(self):
        s= f'{self.eqn} ==> {self.ans}'
        return s
    def __len__(self):
        return len(self.eqn)

    #Sorts according to count(number of times the word has been repeated in the message) first, then alphabetically
    def __lt__(self, otherNode): 
        if otherNode == None:
            raise TypeError("'<' not supported between instances of 'Analyze' and 'NoneType'")
        if self.ans < otherNode.ans:
            return True
        elif self.ans == otherNode.ans and len(self.eqn) == len(otherNode.eqn):
            return self.count > otherNode.count
        elif self.ans == otherNode.ans:
            return len(self.eqn) < len(otherNode.eqn)
        else:
            return False