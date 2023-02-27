class indexClass():
    #menu layout + obtaining user input
    def mess():
        print('*'*57, '\n*\t ST1507 DSAA: MorseCode Message Analyzer\t*\n*', '-'*53, '*\n*',
              ' '*53, '*\n*\t Done by: Joshua Yap', ' '*26, '*\n*\t Class: DAAA/03', ' '*31, '*')
        print('*'*57, '\n*\nPlease Select your choice (\'1\',\'2\',\'3\',\'4\'):',
              '\n\t1.Change Printing Mode', '\n\t2.Convert Morse Code to Text',
              '\n\t3.Analyze Morse Code Message', '\n\t4.Exit')

        inputNum = input('Enter your choice: ')
        return inputNum
    #for print mode, returns the letter and the full word of the print mode
    def printModeMe(printMode):
        while printMode != 'h' or printMode != 'v':
            if str(printMode) == 'h':
                printModeLong = 'Horizontal'
                printMode='h'
                return printMode, printModeLong

            elif str(printMode) == 'v':
                printModeLong = 'Vertical'
                printMode='v'
                return printMode, printModeLong
            else:
                print('invalid input, printing mode will change to default')
                printModeLong = 'Horizontal'
                printMode='h'
                return printMode, printModeLong