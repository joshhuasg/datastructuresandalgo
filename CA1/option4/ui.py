from printsVertical import option2v
from printsHorizontal import option2h
from option3 import option3Class
from index import indexClass
import os


##########################################
# main programme
pMode = 'h'
#Initial printing of the main page
num=indexClass.mess()
while num != 4:
    try:
        num = int(num)
        #checks for input
        if num > 0 and num < 4:
            #initialising the print mode
            pModeOut = indexClass.printModeMe(pMode)
            pMode=pModeOut[0]
            printMode=pModeOut[1]
            #option 1, print mode
            if num == 1:
                print(f'Current mode is {pMode}\n')
                pMode = input('Enter \'h\' for horizontal, and \'v\''
                                  'for vertical printing, then press enter: ')
                #printModeMe returns a tuple. which corresponds to the letter or a whole word
                pModeOut = indexClass.printModeMe(pMode)
                pMode=pModeOut[0]
                printMode=pModeOut[1]
                print(f'Mode is now {printMode}')
                input('Press enter to continue')
            #option 2, checks for priting mode, default is h
            elif num == 2:
                message=input('Type the message you want to convert to morse code:\n')
                if pMode=='v':      
                    outputMorse=option2v.encode(message)
                #option2h requires manually printing after calling encode
                elif pMode=='h':
                    outputMorse=option2h.encode(message)
                    print(outputMorse)
                input('Press enter to continue')
            elif num == 3:
                inputFile=input('Enter input file (please include .txt at the end): ')
                #obtains current diectory location and checks for input file
                here = os.path.dirname(os.path.abspath(__file__))
                inputExists=os.path.join(here,inputFile)
                #input file check
                if os.path.exists(inputExists):
                    #output file does not need a check as it can be manually created
                    outputFile=input('Enter output file (.txt will be added automacially): ')
                    outputFile=str(outputFile)+'.txt'
                    l=option3Class.option3Code(inputFile, outputFile)
                    input('Press enter to continue')
                else:
                    print('Bad input, file does not exist')
            num = indexClass.mess()
        elif num != 4:
            print('error, input a valid number')
            num = indexClass.mess()
    except ValueError:
        print('error, input a valid number')
        num = indexClass.mess()

print('Bye, thanks for using ST1507 DSAA: MorseCode Message Analyzer')
