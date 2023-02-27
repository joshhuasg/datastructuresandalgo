import re
from genCheckConfig import checkConfigClass
from option1BinaryTreeFile import BinaryTree
from option1StackFile import Stack

class buildOption1:#(2-(3**-1.5))
    def buildParseTree(exp):
        #print('\n Parse Tree:')
        tokens=re.sub('(\d+(\.\d+)?|\)|\(|\-)', r' \1 ', exp)
        #re.sub replaces those that match the pattern of XX.XX, a float, and paranteses '(',')', 
        #and spaces are added between each character and patters
        #replacing the matching pattern with the pattern itself
        #for example, it replaces a matched pattern of '3.14', with '3.14' and keeps it
        #'((' is seperated into '( ('
        #however, '**' is ignored and left as '**'
        #does not consider '* *'
        tokens = tokens.split()#split into list using spaces as delimeter
        #print(tokens)
        #(9--(8-0))
        for i in range(len(tokens)):
            if i+1<=len(tokens):
                try:
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
                except:
                    raise SyntaxError
              
        stack = Stack()
        tree = BinaryTree('?')
        stack.push(tree)
        currentTree = tree
        for t in tokens:
            if t in ['+', '-', '*', '/', ')', '(','**', '--'] or t.isnumeric() or isinstance(float(t), float):
                # RULE 1: If token is '(' add a new node as left child
                # and descend into that node
                if t == '(':
                    currentTree.insertLeft('?')
                    stack.push(currentTree)
                    currentTree = currentTree.getLeftTree()
                # RULE 2: If token is operator set key of current node
                # to that operator and add a new node as right child
                # and descend into that node
                elif t in ['+', '-', '*', '/','**', '--']:
                    currentTree.setKey(t)
                    currentTree.insertRight('?')
                    stack.push(currentTree)
                    currentTree = currentTree.getRightTree()
                # RULE 3: If token is number, set key of the current node
                # to that number and return to parent
                elif t not in ['+', '-', '*', '/', ')','**', '--'] :
                    currentTree.setKey(t)
                    parent = stack.pop()
                    currentTree = parent
                # RULE 4: If token is ')' go to parent of current node
                elif t == ')':
                    currentTree = stack.pop()
                else:
                    raise ValueError
            else:
                    raise ValueError
        return tree
    def evaluate(tree):
        _,mode=checkConfigClass.checkConfig()
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        if int(mode)==1:
            if leftTree != None and rightTree != None:
                if op == '+':
                    return float(buildOption1.evaluate(leftTree)) + float(buildOption1.evaluate(rightTree))
                elif op == '-':
                    return float(buildOption1.evaluate(leftTree)) - float(buildOption1.evaluate(rightTree))
                elif op == '*':
                    return float(buildOption1.evaluate(leftTree)) * float(buildOption1.evaluate(rightTree))
                elif op == '/':
                    try:
                        return float(buildOption1.evaluate(leftTree)) / float(buildOption1.evaluate(rightTree))
                    except ZeroDivisionError:
                        print('Error occured. Cannot divide by zero. Returning 0')
                        return 0
                    except:
                        print('unknown error occured. Please check input')
                        return 0
                elif op=='**':
                    return float(buildOption1.evaluate(leftTree)) ** float(buildOption1.evaluate(rightTree))
                elif op=='--':
                    return float(buildOption1.evaluate(leftTree)) + float(buildOption1.evaluate(rightTree))
            else:
                return tree.getKey()
        elif int(mode)==2:
            if leftTree != None and rightTree != None:
                if op == '+':
                    return max(float(buildOption1.evaluate(leftTree)), float(buildOption1.evaluate(rightTree)))
                elif op == '-':
                    return min(float(buildOption1.evaluate(leftTree)), float(buildOption1.evaluate(rightTree)))
                elif op == '*':
                    return round(float(buildOption1.evaluate(leftTree)) * float(buildOption1.evaluate(rightTree)))
                elif op == '/':
                    try:
                        return round(float(buildOption1.evaluate(leftTree)) / float(buildOption1.evaluate(rightTree)))
                    except ZeroDivisionError:
                        print('Error occured. Cannot divide by zero. Returning 0')
                        return 0
                        
                    except:
                        print('unknown error occured. Please check input')
                        return 0
                elif op=='**':
                    try:
                        return float(buildOption1.evaluate(leftTree)) % float(buildOption1.evaluate(rightTree))
                    except ZeroDivisionError:
                        print('Error occured. Cannot divide by zero. Returning 0')
                        return 0
                    except:
                        print('unknown error occured. Please check input')
                        return 0
                elif op=='--':
                    return max(float(buildOption1.evaluate(leftTree)), float(buildOption1.evaluate(rightTree)))
            else:
                return tree.getKey()
        else:
            print('Evaulation mode is erronours. Please change mode to be either \'1\' or \'2\'')
