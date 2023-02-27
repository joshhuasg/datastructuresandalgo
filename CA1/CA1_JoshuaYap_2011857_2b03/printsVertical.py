import numpy as np
from morseDict import morse


# encoding function
class option2v():
    def encode(data):
        data=data.upper()
        mCoded=[[]]
        #initialises the first letter and correspinding morse for appending later 
        if data[0:1] in morse.keys():    
            morseLetter =  np.transpose(morse[data[0:1]])
            mCoded=morseLetter.copy()
    
        #combining the morse
        for letter in data[1:]:
            #checks if it is a valid letter/number
            if letter in morse.keys():
                morsedLetter=np.transpose(morse[letter])
                #checks if same length
                if len(mCoded) != len(morsedLetter):
                    #checks if the message has fewer rows
                    if len(mCoded) < len(morsedLetter):
                        blank = np.empty((1, len(mCoded[1])), dtype='str')
                        blank[:] = ' '
                        while len(mCoded) != len(morsedLetter):
                            mCoded = np.append(blank, mCoded, axis=0)
                    #checks if the new letter has fewer rows
                    elif len(mCoded) > len(morsedLetter):
                        blank = np.empty((1, 1), dtype='str')
                        blank[:] = ' '
                        while len(morsedLetter)!=len(mCoded):
                            morsedLetter=np.append(blank,morsedLetter, axis=0)
            #replaces bad inputs with a space
            else:
                morsedLetter=np.empty((len(mCoded),1), dtype='str')
                morsedLetter[:] = ' '
            #conceating the morse to the side instead of to the bottom
            mCoded = np.concatenate((mCoded, morsedLetter), axis=1)
        return print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
                        for row in mCoded]))


