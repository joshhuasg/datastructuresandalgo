import re
class option4Code:
    def autocorrectFun(l):
        tokens=re.sub('(\d+(\.\d+)?|\)|\(|\-)', r' \1 ', l)
        #same split as in option 1
        tokens = tokens.split()#split into list using spaces as delimeter
        for i in range(len(tokens)):
            if i+1<=len(tokens):
            #checks for - -, thus making it become functionally similiar to -(- something)
                if str(tokens[i])=='-' and str(tokens[i])==str(tokens[i+1]) and str(tokens[i+2]) not in ['(','+', '-', '*', '/', '**',')'] :
                    tokens[i+1]=tokens[i+1]+tokens[i+2]
                    tokens.pop(i+2)
                if str(tokens[i])=='-' and str(tokens[i])==str(tokens[i+1]) and str(tokens[i+2]) in ['(','+', '-', '*', '/', '**',')']:
                    tokens[i]=tokens[i+1]+tokens[i]
                    tokens.pop(i+1)
                        #checks if item before - is not a number and after is a number, so it adds -ve to the number
                if str(tokens[i])=='-' and str(tokens[i-1]) in ['(','+', '-', '*', '/', '**'] and str(tokens[i+1]) not in ['(','+', '-', '*', '/', '**',')'] :
                    tokens[i]=tokens[i]+tokens[i+1]
                    tokens.pop(i+1)
        equn=tokens
        

        #counts the number of open and close brackets, and symbols.
        #symbols is the minium amount of open and close bracket pairs needed 
        numberOpen=0
        numberClosed=0
        numberSymbol=0
        for i in equn:
            #counts the number of open brackets 
            if i=='(':
                numberOpen+=1
            #counts the number of closed brackets
            if i==')':
                numberClosed+=1
            #counts the number of valid symbols (the correct number of bracket pairs)
            if i in ['+', '-', '*', '/','**', '--']:
                numberSymbol+=1
        
        #initialises equation to be (some equation)
        if numberOpen==0 and numberClosed==0:
            for i in range(numberSymbol):
                equn.insert(0,'(')
                numberOpen+=1
        
        for i in range(len(equn)):
            try:
                #checks for instances of 2+3)+(4+5
                if equn[i] in ['+', '-', '*', '/','**', '--']:
                    if equn[i-1]==')' and equn[i+1]=='(':
                        if (equn[i+2].isnumeric() or isinstance(float(equn[i+2]), float)) and (equn[i-2].isnumeric() or isinstance(float(equn[i-2]), float)):
                            if equn[i-3] in ['+', '-', '*', '/','**', '--'] and equn[i+3] in ['+', '-', '*', '/','**', '--']:
                                if equn[0]!='(':
                                    equn.insert(0,'(')
                                    numberOpen+=1
                                if equn[-1]!=')':
                                    equn.append(')')
                                    numberClosed+=1
            except:
                return equn
        
        #checks for instances of 1+2)+3+4...
        for i in range(len(equn)):
            try:
                if equn[i]==')':
                    if equn[i+1]in ['+', '-', '*', '/','**', '--'] and (equn[i+2].isnumeric() or isinstance(float(equn[i+2]), float)):
                        if equn[i+3]!=')':
                            equn.insert(i+3,')')
                            numberClosed+=1
            except:
                numberClosed+=1
                equn.append(')')
        #checks for instances of 1+2)+3)+4)...
        for i in range(numberClosed):
            equn.insert(0,'(')
            numberOpen+=1
        #ensures that every equation is within '( )'
        try:
            if (equn[-1].isnumeric() or isinstance(float(equn[-1]), float)):
                if equn[-1]!=')':
                    equn.append(')')
                    numberClosed+=1
                if equn[-1]!='(':
                    equn.insert(0,'(')
                    numberOpen+=1
        except:
            pass
        #while True is used so the checking always runs. if statement will be used to break
        #this checks for any errenous input that may be missed by the above
        while True:
            #assumes that in the case of more closed brackets, the missing open brackets belong in the front
            while numberClosed>numberOpen:
                equn.insert(0,'(')
                numberOpen+=1
            #if the equation is similiar to '(2**9)-(9-0)', the code may not add the brackets to the front and rear
            #this if checks for such occurences and changes them to be '((2**9)-(9-0))'
            if equn[0]=='('and equn[-1]==')' and (numberSymbol-numberClosed==1 and numberSymbol-numberOpen==1):
                equn.insert(0,'(')
                numberOpen+=1
                equn.insert(-1,')')
                numberClosed+=1
            #adds brackets into the middle of the equation
            #for occurences where there is fewer '('
            if numberClosed>=numberOpen: 
                    for i in range(len(equn)):
                        try:
                            if equn[i] in ['+', '-', '*', '/','**', '--'] and equn[i+1] !='(' and equn[i+2] in ['+', '-', '*', '/','**', '--']:
                                equn.insert(i+1, "(")
                                numberOpen+=1
                        except:
                            pass
            #for occurences where there is fewer '('
            if numberClosed<=numberOpen:
                    for i in range(len(equn)):
                        try:
                            if equn[i] in ['+', '-', '*', '/','**', '--'] and equn[i+1] !='(' and equn[i+2] in ['+', '-', '*', '/','**', '--']:
                                equn.insert(i+2, ")")
                                numberClosed+=1
                        except IndexError:
                            equn.append(')')
                            numberClosed+=1
            #checks for instance of 'symbol number' patterns and starts with a number    
            for i in range(len(equn)):
                try:
                    #checks for '2**9-9-0', changes to '2**9)-(9-0'
                    if equn[i] in ['+', '-', '*', '/','**', '--']:
                        if (equn[i-1].isnumeric() or isinstance(float(equn[i-1]), float)) and (equn[i+1].isnumeric() or isinstance(float(equn[i+1]), float)):
                            if equn[i-2] in ['+', '-', '*', '/','**', '--'] and equn[i+2] in ['+', '-', '*', '/','**', '--']:
                                equn.insert(i+1,'(')
                                numberOpen+=1
                                equn.insert(i-1,')')
                                numberClosed+=1
                    #checks for '2**9-9', changes to '2**9)-9'
                    if (equn[i].isnumeric() or isinstance(float(equn[i]), float)):
                        if equn[i-1] in ['+', '-', '*', '/','**', '--'] and equn[i+1] in ['+', '-', '*', '/','**', '--']:
                            if (equn[i-2].isnumeric() or isinstance(float(equn[i-2]), float)) and (equn[i+2].isnumeric() or isinstance(float(equn[i+2]), float)):
                                equn.insert(i-1,')')
                                numberClosed+=1
                except:
                    pass
            #if somehow, the equation is still not encased in '( )', this helps to add ')' to the rear
            if numberSymbol-numberClosed==2:
                equn.append(')')
                numberClosed+=1
            #breaks out of loop when the number of brackets match the number of Symbols
            if numberOpen>=numberSymbol and numberClosed>=numberSymbol:
                break
        if numberOpen>numberClosed:
            equn.pop(0)
            numberOpen-=1

        #checks for (((1+2)+3))
        if equn[0]==equn[1]=='(' and equn[-2]==equn[-1]==')':
            equn.pop(0)
            equn.pop(-1)

        #returns corrected equation
        return equn















