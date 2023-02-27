import os
class checkConfigClass:
    def checkConfig():
        here = os.path.dirname(os.path.abspath(__file__))
        inputExists=os.path.join(here,'config.txt')
        file = open(inputExists, 'r')
        content = file.read()
        content=content.split('\n')
        try:
            separator=content[0]
            mode=content[1]
        except IndexError:
            separator='.'
            mode='1'
            newConfig=f'{separator}\n{mode}'
            file = open(inputExists, 'w')
            file.write(newConfig)
            return separator, mode
        return separator, mode
    def checkPrint():
        here = os.path.dirname(os.path.abspath(__file__))
        inputExists=os.path.join(here,'print.txt')
        file = open(inputExists, 'r')
        content = file.read()
        try:
            mode=content[0]
        except IndexError:
            mode='1'
            newConfig=f'{mode}'
            file = open(inputExists, 'w')
            file.write(newConfig)
            return mode
        return mode
