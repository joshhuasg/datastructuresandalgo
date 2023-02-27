import printsvertical2
import printshorizontal
def mess():
    print('*'*57, '\n*\t ST1507 DSAA: MorseCode Message Analyzer\t*\n*', '-'*53, '*\n*',
          ' '*53, '*\n*\t Done by: Joshua Yap', ' '*26, '*\n*\t Class: DAAA/03', ' '*31, '*')
    print('*'*57, '\n*\nPlease Select your choice (\'1\',\'2\',\'3\',\'4\'):',
          '\n\t1.Change Printing Mode', '\n\t2.Convert Morse Code to Text',
          '\n\t3.Analyze Morse Code Message', '\n\t4.Exit')

    inputNum = input('Enter your choice: ')
    return inputNum


printMode = 'h'


def printModeMe(printMode):
    while printMode != 'h' or printMode != 'v':
        if printMode == 'h':
            printModeLong = 'Horizontal'
            return printModeLong

        elif printMode == 'v':
            printModeLong = 'Vertical'
            return printModeLong
        else:
            print('invalid input')


num = mess()


##########################################
# main programme
while num != 4:
    try:
        num = int(num)
        if num > 0 and num < 4:
            pMode = printModeMe(printMode)
            print(num)
            if num == 1:
                print(f'Current mode is {pMode}\n')
                printMode = input('Enter \'h\' for horizontal, and \'v\''
                                  'for vertical printing, then press enter: ')
                pMode = printModeMe(printMode)
                print(f'Mode is now {pMode}')
            elif num == 2:
                message=input('Print the message you want to convert to morse code:\n')
                if printMode=='v':
                    outputMorse=printsvertical2.option2h.encode(message)
                    print(outputMorse)
                elif printMode=='h':
                    outputMorse=printshorizontal.encode(message)
                    print(outputMorse)


            elif num == 3:
                print(num)

            num = mess()
        elif num != 4:
            print(num)
            print('error, input a valid number')
            num = mess()
    except ValueError:
        print(num)
        print('error, input a valid number')
        num = mess()

print('exit')
