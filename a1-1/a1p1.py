




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
    
    for char in message:  
        colList[col].append(char)
        col += 1
    
        if col == keyLen:
            col = 0
    
    hiddenMessage = ''
    for i in range(keyLen):
        currentPos = key[i]-1
        hiddenMessage+= ''.join(colList[currentPos])
    
    return hiddenMessage
    
    
    


if __name__ == '__main__':
    main()