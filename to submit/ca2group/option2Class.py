import os
import re
import pandas as pd
from option2Evaulate import option2EvaulationClass

# reading file that has message to be encoded
here = os.path.dirname(os.path.abspath(__file__))

class option2Code:
    def __init__(self, fileInput):
        self.__fileInput = fileInput

    def openfile(self):
        filename = os.path.join(here, self.__fileInput)
        file = open(filename, 'r')
        content = file.read()
        eqns = re.split('([\n])', content)
        count = 0 
        for eqn in eqns:
            if eqn == '\n' or eqn == '':
                eqns.remove('\n')
        for eqn in eqns:
            eqns[count] = eqn.replace(" ", "")
            count+=1
        print(eqns)
        return eqns

    def evaln(self):
        evals = []
        eqns = self.openfile()
        for eqn in eqns:
            evln = option2EvaulationClass.evaluate2(eqn)
            evals.append(evln)
        data={'Equation':eqns,'Answer':evals}
        df=pd.DataFrame(data)
        return df

