from option1Build import buildOption1
from genCheckConfig import checkConfigClass

class option1Code:
    def evaluate(exp, opt=0):
        checkConfigClass.checkConfig()
        mode = checkConfigClass.checkPrint()
        tree = buildOption1.buildParseTree(exp)
        out=buildOption1.evaluate(tree, opt)
        if int(mode) == 1:
            tree.printInorder(0)
        elif int(mode) == 2:
            tree.printPreorder(0)
        elif int(mode) == 3:
            tree.printPostorder(0)
        else:
            raise SyntaxError
            
        if int(out)==float(out):#as int removes the decimal place, the output would be smaller than the float.
                                #for example, int(2.9) would be 2, thus the number is likely float
                                #but float(3.0)is the same as int(3)
            out= int(out)
        else:
            out=float(out)
        print (f'The expression: {exp} evaluates to: \n{out}')
    
