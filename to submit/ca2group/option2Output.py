from option2Sort import SortedList
from option2Analyze import Analyze
from option2Freq import option2Sort
import os

# reading file that has message to be encoded
here = os.path.dirname(os.path.abspath(__file__))

class outputClass:
    def output(df, out):
        l = SortedList() 
        df = option2Sort.count(df)
        df = option2Sort.freq(df)

        for i in range(len(df)):
            l.insert(Analyze(df['Equation'][i],df['Frequency'][i],df['Bracket'][i],df['Answer'][i]))
        currentLocation=os.path.join(here,out)
        f= open(currentLocation,"w+")
        string = str(l)
        f.write(string)
        return l