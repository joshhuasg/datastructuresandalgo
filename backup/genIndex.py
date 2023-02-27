from option1Class import option1Code
from option2Class import option2Code
from option2Output import outputClass
from option3Class import option3Code
from option4Class import option4Code
from genCheckConfig import checkConfigClass
from genUi import uIClass
from genCheckConfig import checkConfigClass
import os


##########################################
# main programme
# Initial printing of the main page
seperator, mode = checkConfigClass.checkConfig()
num = uIClass.mess()

while num != 5:
    try:
        num = int(num)
        # checks for input
        if num > 0 and num < 5:
            if num == 1:
                #exp = '((200 + (4*3.14)) / (2**3) )' (2+(4*5))
                message = input('Type the message you want to evaluate:\n')
                print('\nExpression Tree:')
                outputEqn = option1Code.evaluate(message)
                input('Press enter to continue')
            # option 2, checks for priting mode, default is h
            elif num == 2:
                inputFile = input(
                    'Enter input file (please include .txt at the end): ')
                # obtains current diectory location and checks for input file
                here = os.path.dirname(os.path.abspath(__file__))
                inputExists = os.path.join(here, inputFile)
                # input file check
                if os.path.exists(inputExists) or inputExists=='':
                    outputFile = input(
                        'output file does noter output file (.txt will be added automacially): ')
                    outputFile = str(outputFile)+'.txt'
                    if len(outputFile) != 0:
                        code2 = option2Code(inputFile)
                        df = code2.evaln()
                        output = outputClass.output(df, outputFile)
                        print('\n', output, '\n\n')
                        input('Press enter to continue')
                    else:
                        print('Bad input, input a file name')
                else:
                    print('Bad input, file does not exist')
            elif num == 3:
                print(f'Current seperator: {seperator}\nCurrent mode: {mode}\n\n')
                new_seperator = input(
                    'Enter new seperator (leave blank to leave unchanged)')
                new_mode = input(
                    'Enter new mode (leave blank to leave unchanged)')
                option3Code.changeConfig(new_seperator, new_mode)
                print(
                    f'Config File has been change to have {new_seperator} as seperator and {new_mode} as mode')
                input('Press enter to continue')
            elif num == 4:
                equationWrong=input('Input equation to autocorrect and evaulate:\n')
                equationCorrected=option4Code.autocorrectFun(equationWrong)
                strEqnCorrected=''.join(equationCorrected)
                print(strEqnCorrected)
                outputEqn = option1Code.evaluate(str(strEqnCorrected))
                input('Press enter to continue')
            num = uIClass.mess()
        elif num != 5:
            print('error, input a valid number')
            num = uIClass.mess()
    except ValueError:
        print('Error, input a valid number')
        num = uIClass.mess()
    except SyntaxError:
        print('Error, input a valid equation.')
        num = uIClass.mess()

print('Bye, thanks for using ST1507 DSAA: Expression Evaluator & Sorter')
