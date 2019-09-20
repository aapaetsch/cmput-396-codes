import math

def main():
    message = 'XOV EK HLYR NUCO HEEEWADCRETL CEEOACT KD'
    key = [2,4,6,8,10,1,3,5,7,9]
    decrypted = decryptMessage(key, message)
    print(decrypted + '|')
    
    message2 = 'IS HAUCREERNP F'
    key2 = [2,4,1,5,3]
    decrypted2 = decryptMessage(key2, message2)
    print(decrypted2 + '|')
    
    message3 = 'ADGCFBE'
    key3 = [1,3,2]
    decrypted3 = decryptMessage(key3, message3)
    print(decrypted3 + '|')


def decryptMessage(key, message):
    keyLen = len(key)
    numCols = keyLen
    numRows = int(math.ceil(len(message)/float(keyLen)))
    numShade = (numCols * numRows) - len(message)
    
    dictText = []
    for i in range(numRows):
        dictionary = {}
        for j in range(numCols):
            dictionary[j+1] = ''
        dictText.append(dictionary)
    
    for i in range(numShade):
        dictText[numRows-1][numCols - numShade + i + 1] = '*'
    
    col = 0
    row = 0
    visited = 0
    while visited < len(message):
        char = message[visited]
        if dictText[row][key[col]] != '*':
            dictText[row][key[col]] = char
            visited += 1
        row += 1 
        if row == numRows:
            row = 0
            col += 1
            
    plainText = ''
    for i in range(numRows):
        for j in range(keyLen):
            plainText += dictText[i][j+1]

    return plainText.replace('*','')
        
        
        
        
    
    
if __name__ == '__main__':
    main()