# Transposition Cipher Encryption
# Adapted from https://www.nostarch.com/crackingcodes (BSD Licensed)

def main():
    
    # Key and Message for first example
    message = 'CIPHERS ARE FUN'
    #key = [2,4,1,5,3]
    key = [2,1]
    ciphertext = messageEncrypting(key, message)
    # print the first cypher text after running encryptMessage
    print(ciphertext + '|')
    
    # Key and Message for second example
    message2 = 'ABCDEFG'
    key2 = [1,3,2]
    # print the second cypher text after running encryptMessage
    ciphertext2 = messageEncrypting(key2, message2)
    print(ciphertext2 + '|')

    message3Encrypted = 'XOV EK HLYR NUCO HEEEWADCRETL CEEOACT KD'
    key3 = [2,4,6,8,10,1,3,5,7,9]
    message3 = 'EXCELLENT WORK YOU HAVE CRACKED THE CODE' 
    ciphertext3 = messageEncrypting(key3, message3)
    if ciphertext3 == message3Encrypted:
        print("Working")
    else:
        print("not working")

def messageEncrypting(key, message):
    
    # Get the key length and sort the key
    keyLen = len(key)
    sortedKey = sorted(key)
    
    # create columns for the message
    originalMessage = [[] for i in range(keyLen)]
    #string repr for the encrypted message
    encrypted = ''
    j = 0
    
    # for each character in the message
    for character in message:
        #sort each character into its corresponding column
        currentPosition = sortedKey[j]
        originalMessage[currentPosition -1].append(character)
        sortedKey.append(currentPosition)
        j += 1
        if j == keyLen:
            j = 0

    for i in range(keyLen):
        #encrypt the message based on the unsorted key
        currentPosition = key[i]
        encrypted += ''.join(originalMessage[currentPosition - 1])
    #return the encrypted message
    return encrypted

#for running as a standalone file instead of importing the module
if __name__ == '__main__':
    main()

