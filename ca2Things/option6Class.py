from genCheckConfig import checkConfigClass
import os
class Printing:
    def __init__(self, mode):
        self.__mode = mode
    def changePrint(self):
        valid=True
        mode=checkConfigClass.checkPrint()
        if self.__mode=='':
            self.__mode=mode
        elif str(self.__mode) not in ['1','2','3']:
            valid=False
        if valid:
            print(f'Printing method has been changed to {self.__mode} as mode')
            return self.writeToFile()
        else:
            print('Error, invalid inputs')
            return None
    def writeToFile(self):
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'print.txt')
        # Read fruits from a file and sort in list
        f = open(filename, 'w')
        newPrint=f'{self.__mode}'
        f.write(newPrint)
        return print('Successfully overwritten file')