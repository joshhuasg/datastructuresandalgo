from printsletter import decodeMorse
from wordCheck import analyze
from essencial import startEssencial
import pandas as pd
import os
here = os.path.dirname(os.path.abspath(__file__))
###############################################
###############################################
###############################################
###############################################
class option3Class():
    def option3Code(inFile, outName):
        decoded=decodeMorse.decodePrep(inFile)
        nnew=analyze.getFrequency(decoded)
        my_list = list(map(lambda x: x.split(' '), nnew))
        df = pd.DataFrame(my_list[:-1], columns =['morse', 'Word', 'Frequency', 'Position(S)','Initial X', 'Initial Y'])
        
        maximumFrequency=df['Frequency'].max()
        stringList=[]
        while maximumFrequency>0:
            l=str(f'\nMorse words with the value of: {maximumFrequency}\n')
            stringList.append(l)
            df2=df.loc[df['Frequency'] == maximumFrequency].reset_index()
            df2=df2[['morse', 'Word', 'Frequency', 'Position(S)','Initial X', 'Initial Y']].apply(lambda x: list((sorted(x, key=lambda item: (-len(item), item.lower())))))
            #df2=df2.iloc[df2.agg({"Word":len}).sort_values(['Word'], ascending=True).index]
            print(df2)

            maximumFrequency-=1
            for row in df2.itertuples(index=False):
                string=str(f'{row[1]} \n {row[2]} {row[3]} {row[4]}')
                stringList.append(string)
            joined='\n'.join(stringList)
        
        dfCoor=df[['Word','Frequency', 'Initial X', 'Initial Y']]
        listCoor=dfCoor.values.tolist()
        messageE=option3Class.essential(outName,listCoor)
        print('\n'*2,'*'*20,'Decoded Message')
        print(decoded)
        print('\n'*2,'*'*20,'Analysis:')
        print(joined)
        print('\n'*2,'*'*20,'\nEssential Message')
        print(messageE)
        currentLocation=os.path.join(here,outName)
        f= open(currentLocation,"w+")
        outPut=joined+'\n'*3+'Essential Message'+ str(messageE)
        f.write(outPut)
    def essential(outName, listCoor):
        l=startEssencial.startEssencial(listCoor)
        return l
        