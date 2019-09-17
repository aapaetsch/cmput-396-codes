# Transposition Cipher Encryption
# Adapted from https://www.nostarch.com/crackingcodes (BSD Licensed)

def main():
    
    # Key and Message for first example
    message = 'CIPHERS ARE FUN'
    key = [2,4,1,5,3]
    ciphertext = encryptMessage(key, message)
    # print the first cypher text after running encryptMessage
    print(ciphertext + '|')
    
    # Key and Message for second example
    message2 = 'ABCDEFG'
    key2 = [1,3,2]
    # print the second cypher text after running encryptMessage
    ciphertext2 = encryptMessage(key2, message2)
    print(ciphertext2 + '|')

def encryptMessage(key, message):
    
    # Get the key length and sort the key
    keyLen = len(key)
    sortedKey = sorted(key)
    # create columns for the message
    originalMessage = [[] for i in range(keyLen)]
    #string repr for the encrypted message
    encrypted = ''

    # for each character in the message
    for character in message:
        #sort each character into its corresponding column
        currentPosition = sortedKey.pop(0)
        originalMessage[currentPosition -1].append(character)
        sortedKey.append(currentPosition)

    for i in range(keyLen):
        #encrypt the message based on the unsorted key
        currentPosition = key.pop(0)
        encrypted += ''.join(originalMessage[currentPosition - 1])
    
    #return the encrypted message
    return encrypted

#for running as a standalone file instead of importing the module
if __name__ == '__main__':
    main()

