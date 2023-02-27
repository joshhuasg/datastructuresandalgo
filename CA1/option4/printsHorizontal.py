from morseDict import morse
# reading file that has message to be encoded
class option2h():
 # encoding function
    def encode(data):
        encodedWord = ''
        mCodedLine=[]
        #ensures that the user input is in all capitals
        data=data.upper()
        #split
        rowMessage = data.split("\n")
        #iterates through row
        for row in rowMessage:
            row = row.split(" ")
            mCoded = []
            #iterates through each word
            for word in row:
                wordSplit=list(word)
                #iterates through letter in word
                for letter in wordSplit:
                    if letter.isalpha():
                        morseLetter = ''.join(str(item) for innerlist in morse[letter.upper()] for item in innerlist)
                        mCoded.append(morseLetter)
                    elif letter.isdigit():
                        morseLetter = ''.join(str(item) for innerlist in morse[letter] for item in innerlist)
                        mCoded.append(morseLetter)
                    
                mCoded.append(' ')
            mCodedLine.append((','.join(mCoded)).strip(', '))
        encodedWord='\n'.join(mCodedLine)#as each record in mCodedLine is one line, need to combine them by \n
        return encodedWord
