import re
import numpy as np
# dictonary for letter/number to morse
morse = {'A': [['.','-']], 'B': [['-','.','.','.']], 'C': [['-','.','-','.']], 'D': [['-','.','.']], 
        'E': [['.']], 'F': [['.','.','-','.']], 'G': [['-','-','.']],
        'H': [['.','.','.','.']], 'I':[[ '.','.']], 'J': [['.','-','-','-']], 'K': [['-','.','-']],
        'L': [['.','-','.','.']],
        'M': [['-','-']], 'N': [['-','.']],
        'O': [['-','-','-']], 'P': [['.','-','-','.']], 'Q': [['-','-','.','-']], 
        'R': [['.','-','.']], 'S': [['.','.','.']], 
        'T': [['-']], 'U': [['.','.','-']],
        'V': [['.','.','.','-']], 'W': [['.','-','-']], 'X': [['-','.','.','-']], 
        'Y': [['-','.','-','-']], 'Z': [['-','-','.','.']],
        '0': [['-','-','-','-','-']], '1': [['.','-','-','-','-']], '2': [['.','.','-','-','-']], 
        '3': [['.','.','.','-','-']], '4': [['.','.','.','.','-']], '5': [['.','.','.','.','.']],
        '6': [['-','.','.','.','.']], '7': [['-','-','.','.','.']], '8': [['-','-','-','.','.']], 
        '9': [['-','-','-','-','.']]
         }


# encoding function
class option2h():
 def encode(data):
    mCoded=[[]]

    if data[0:1].isalpha():    
        morseLetter =  np.transpose(morse[data[0:1]])
        mCoded=morseLetter.copy()
    elif data[0:1].isnumeric():
        morseLetter =  np.transpose(morse[data[0:1]])
        mCoded=morseLetter.copy()
    
    #combining the morse
    for letter in data[1:]:
        if letter.isnumeric() or letter.isalpha():
            morsedLetter=np.transpose(morse[letter])
            if len(mCoded) != len(morsedLetter):
                if len(mCoded) < len(morsedLetter):
                    blank = np.empty((1, len(mCoded[1])), dtype='str')
                    blank[:] = ' '
                    while len(mCoded) != len(morsedLetter):
                        mCoded = np.append(blank, mCoded, axis=0)
                elif len(mCoded) > len(morsedLetter):
                    blank = np.empty((1, 1), dtype='str')
                    blank[:] = ' '
                    while len(morsedLetter)!=len(mCoded):
                        morsedLetter=np.append(blank,morsedLetter, axis=0)
        else:
            morsedLetter=np.empty((len(mCoded),1), dtype='str')
            morsedLetter[:] = ' '
        mCoded = np.concatenate((mCoded, morsedLetter), axis=1)
    return print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in mCoded]))




coded = option2h.encode(content)
