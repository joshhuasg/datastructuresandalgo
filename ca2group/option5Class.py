import re

class Convert():
    def __init__(self, exp):
        self.__exp = exp
    def isBinary(self):
        # regular expression to find the strings
        # which have characters other than 0 and 1
        yon = re.compile('[^01]')
        
        # use findall() to get the list of strings
        # that have characters other than 0 and 1.
        if(len(yon.findall(str(self.__exp)))):
            return False
        else:
            return True
    def convert(self):
        if self.isBinary():
            dec = int(str(self.__exp), 2)
            print(dec)
            return dec
        else:
            raise ValueError
