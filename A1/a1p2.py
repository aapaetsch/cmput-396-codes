# Transposition Cipher decryption
# Adapted from https://www.nostarch.com/crackingcodes (BSD Licensed)
import math

# main function will run if "python3 a1p2.py" is run, it returns decrypted messages from the test cases
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
    
    #we make a dictionary for sorting the characters later on
    dictText = []
    for i in range(numRows):
        dictionary = {}
        for j in range(numCols):
            dictionary[j+1] = ''
        dictText.append(dictionary)
    #populate the dictionary with ** representing shade blocks ( that way if * is used in the text, it will still be valid)
    for i in range(numShade):
        dictText[numRows-1][numCols - numShade + i + 1] = '**'
    
    col = 0
    row = 0
    visited = 0
    #for each character in the message
    while visited < len(message):
        #set the current character
        char = message[visited]
        #If we are not dealing with a shaded block
        if dictText[row][key[col]] != '**':
            #sort the character into its place based on the key
            dictText[row][key[col]] = char
            #only increment visited if we dont visit a shade block
            visited += 1
        row += 1 
        #once we reach the end of a row, start the next column and return to the start of the row
        if row == numRows:
            row = 0
            col += 1
    
    #turn the dictionary into a plaintext of the decrypted message
    plainText = ''
    for i in range(numRows):
        for j in range(keyLen):
            plainText += dictText[i][j+1]
    #return the plaintext, getting rid of all the shade indicators
    return plainText.replace('**','')
        
        
        
        
    
    
if __name__ == '__main__':
    main()
