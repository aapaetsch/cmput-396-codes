# Transposition Cipher Encryption
# Adapted from https://www.nostarch.com/crackingcodes (BSD Licensed)

#The main function was used for testing, it will run and output the encrypted texts if you run "a1p1.py"
def main():
    
    message = 'CIPHERS ARE FUN'
    key = [2,4,1,5,3]
    encrypted = encryptMessage(key, message)
    print(encrypted+'|')
    
    message2 = 'ABCDEFG'
    key2 = [1,3,2]
    encrypted2 = encryptMessage(key2, message2)
    print(encrypted2+'|')
    
    message3 = 'EXCELLENT WORK YOU HAVE CRACKED THE CODE'
    key3 = [2,4,6,8,10,1,3,5,7,9]
    encrypted3 = encryptMessage(key3, message3)
    print(encrypted3+'|')
    
def encryptMessage(key, message):
    
    keyLen = len(key)
    colList = [[] for i in range(keyLen)]
    col = 0
    #for each character in the mesage
    for char in message:  
        #append it to its column
        colList[col].append(char)
        col += 1 #increment the column
        
        #if the current column is the last column, go back to the first
        if col == keyLen:
            col = 0
    
    #once we split the message up, encrypt the message based on the key
    hiddenMessage = ''
    for i in range(keyLen):
        currentPos = key[i]-1
        #we join the columns based on the order of the key
        hiddenMessage+= ''.join(colList[currentPos])
    #return the encrypted message
    return hiddenMessage
    
    
    


if __name__ == '__main__':
    main()