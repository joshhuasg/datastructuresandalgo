from genCheckConfig import checkConfigClass
import os
class option3Code:
    def changeConfig(newSeperator, newMode):
        valid=True
        separator, mode=checkConfigClass.checkConfig()
        
        if newSeperator=='':
            newSeperator=separator
        if newMode=='':
            newMode=mode
        elif str(newMode) not in ['1','2']:
            valid=False
        if valid:
            return option3Code.writeToFile(newSeperator.strip(),newMode.strip())
        else:
            print('Error, invalid inputs')
            return None
    
    def writeToFile(newSeperator,newMode):
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'config.txt')
        # Read fruits from a file and sort in list
        f = open(filename, 'w')
        newConfig=f'{newSeperator}\n{newMode}'
        f.write(newConfig)
        return print('Successfully overwritten file')
