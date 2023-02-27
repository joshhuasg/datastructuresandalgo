from option1Build import buildOption1
from genCheckConfig import checkConfigClass

class option2EvaulationClass:
    def evaluate2(exp):
            checkConfigClass.checkConfig()
            tree = buildOption1.buildParseTree(exp)
            out=buildOption1.evaluate(tree)
            #print(out)
            if int(out)==float(out):#as int removes the decimal place, the output would be smaller than the float.
                                #for example, int(2.9) would be 2, thus the number is likely float
                                #but float(3.0)is the same as int(3)
                out= int(out)
            return out