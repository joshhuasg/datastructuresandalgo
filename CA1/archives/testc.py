from wordCheck import wordCheck
from printsletter import decodeMorse


 
import os
here = os.path.dirname(os.path.abspath(__file__))
fileInput='morse_sos.txt'#str(input('input file name:'))#'morse_sos.txt'

decoded=decodeMorse.decodePrep(fileInput)

nnew=wordCheck.getFrequency(decoded)

my_list = list(map(lambda x: x.split(' '), nnew))

import numpy as np
my_list2=np.array(my_list,dtype=object)
import pandas as pd
df = pd.DataFrame(my_list, columns =['morse', 'Word', 'Frequency', 'Position(S)','Initial X', 'Initial Y'])
df=df.sort_values(by=['Initial X', 'Initial Y'],ascending=True)
df=df.sort_values(by=['Frequency'],ascending=False)
maximumFrequency=df['Frequency'].max()
stringList=[]
while maximumFrequency>0:
    l=str(f'\nMorse words with the value of: {maximumFrequency}\n')
    stringList.append(l)
    df2=df.loc[df['Frequency'] == maximumFrequency]
    maximumFrequency-=1
    for row in df2.itertuples(index=False):
      string=str(f'{row[0]} \n {row[1]} {row[2]} {row[3]}')
      stringList.append(string)
joined='\n'.join(stringList)
print(joined)
outName="outputAnalysis.txt"
currentLocation=os.path.join(here,outName)
f= open(currentLocation,"w+")
f.write(joined)