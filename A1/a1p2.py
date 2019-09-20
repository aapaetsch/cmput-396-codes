#tranion Cipher Decryption
# Adapted from https://www.nostarch.com/crackingcodes (BSD LICENSED)

import math

def main():

    message = "XOV EK HLYR NUCO HEEEWADCRETL CEEOACT KD"
    key = [2,4,6,8,10,1,3,5,7,9]
    decryptedText = messageDecrypting(key, message)
    print(decryptedText + "|\n")
    
    message2 = 'ADGCFBE'
    key2 = [1,3,2] 
    decrypted2 = messageDecrypting(key2, message2)
    print(decrypted2+'|\n')
    
    message3 = 'IHR R UCPESAEFN'
    key3 = [2,4,1,5,3]
    print(messageDecrypting(key3, message3))

def messageDecrypting(key, message):
    
    keyLen = len(key)
    n = len(message)

    numRows = int(math.ceil(len(message)/float(keyLen)))
    numCols = keyLen
    numShaded = (numRows * numCols) - n
    plainTextList = [[] for i in range(numRows)]

    col = 0
    row = 0
    #iterate over the encrypted message and separate it into the proper columns
    #taking care to account for shaded blocks
    character = 0
    while character < len(message):
        if (key[col] != keyLen):
            plainTextList[row].append(message[character])
        elif (key[col] == keyLen):
            if (row >= numRows - numShaded):
                plainTextList[row].append('*')
                character -= 1
            elif (row < numRows - numShaded):
                plainTextList[row].append(message[character])
        row += 1

        if (row == numRows):
            col += 1
            row = 0  
        character += 1
        
    plainText = ''
   # print(plainTextList)
   # for substring in plainTextList:
        
      #  substringList = ['' for j in range(keyLen)]
        
       # for i in range(len(substring)):
        #    substringList[key[i] - 1] = substring[i]
       # plainText += ''.join(substringList)
    print(plainTextList, 'herh')
    plainTextList = list(zip(*plainTextList))
    
    substringList = [[] for i in range(numCols)]
    
    for i in range(keyLen):
        print(len(plainTextList))
        substringList[key[i] - 1] = plainTextList[i]
    print(substringList)
    substringList = list(zip(*substringList))
    print(substringList)
    for i in range(len(substringList)):
            substringList[i] = ''.join(list(substringList[i]))
    plainText = ''.join(substringList)   
    plainText = plainText.replace('*','')
    return plainText 
    


if __name__ == '__main__':
    main()
