# Transposition Cipher Decryption
# Adapted from https://www.nostarch.com/crackingcodes (BSD LICENSED)

import math

def main():

    message = "XOV EK HLYR NUCO HEEEWADCRETL CEEOACT KD"
    key = [2,4,6,8,10,1,3,5,7,9]
    decryptedText = messageDecrypting(key, message)
    print(decryptedText + "|\n")



def messageDecrypting(key, message):
    print(key, message)
    keyLen = len(key)
    n = len(message)

    print(key, keyLen, message)

    numCols = int(math.ceil(len(message)/float(keyLen)))
    numRows = keyLen
    numShaded = (numRows * numCols) - n
    plainTextList = [[] for i in range(numCols)]

    col = 0
    row = 0
    #iterate over the encrypted message and separate it into the proper columns
    #taking care to account for shaded blocks
    for character in message:

        plainTextList[col].append(character)
        col += 1
        
        if (col == numCols) or (col == numCols - 1 and row >= numRows - numShaded):
        
            col = 0
            row += 1
    
    plainText = ''
    for substring in plainTextList:
        
        substringList = ['' for j in range(keyLen)]
        
        for i in range(len(substring)):
            substringList[key[i] - 1] = substring[i]
        plainText += ''.join(substringList)

    return plainText
    


if __name__ == '__main__':
    main()
