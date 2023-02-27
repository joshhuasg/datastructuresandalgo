class uIClass():
    #menu layout + obtaining user input
    def mess():
        print('*'*57, '\n*\t ST1507 DSAA: Expression Evaluator & Sorter\t*\n*', '-'*53, '*\n*',
              ' '*53, '*\n*\t Done by: Joshua (2011857) & Jennifer (2030920)', '*\n*\t Class: DAAA/03', ' '*31, '*')
        print('*'*57, '\n*\nPlease Select your choice (\'1\',\'2\',\'3\',\'4\',\'5\'):',
              '\n\t1.Evaluate Expression', '\n\t2.Sort Expressions','\n\t3.Change Seperator and/or Mode', 
              '\n\t4.Autocorrect and Evaulate','\n\t5.Exit')

        inputNum = input('Enter your choice: ')
        return inputNum
