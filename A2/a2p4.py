# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import sys, util

NUM_SYM = 26
#key 0 to 25 inclusive
#mode is encrypt/decrypt otherwise terminate
#single quote for message

def caesar(key, message, mode):
    translated = []
    messageUpper = message.upper()
    
    newKey = []
    for letter in key.upper():
        #if mode == 'decrypt': 
            #newKey.append(-util.let2ind(letter))
        #else:
            #newKey.append(util.let2ind(letter))
        newKey.append(util.let2ind(letter))
    shift = 0
    keyLen = len(newKey)
    pos = 0 
    for i in range(len(message)):
        k = newKey[pos]
        num = util.let2ind(messageUpper[i])

        if (num < 0) or (num >= NUM_SYM):
            translated.append(messageUpper[i])

        else:
            shift += k
            if mode == 'encrypt':
                #shift += k
                num = (num + shift) % NUM_SYM
                
            
            elif mode == 'decrypt':
                
                num = (num - shift) % NUM_SYM
                
            
            letter = util.ind2let(num)

            if message[i].isupper():
                letter = letter.upper()
            
            else:
                letter = letter.lower()

            translated.append(letter)
        
            if pos == keyLen - 1:
                pos = 0 
            else:
                pos +=1


    
    return ''.join(translated)


def checkArgs():
    args = sys.argv

    if len(args) == 4:


        if not args[1].isalpha():
            print("Error, Invalid value for key, must be a word or string of alphabetical characters, Quitting...")
            sys.exit()

        if args[2].lower() != 'encrypt' and args[2].lower() != 'decrypt':
            print("Invalid Mode Entered, Must Be 'encrypt' Or 'decrypt', Quitting...")
            sys.exit()

        else:
            args[2] = args[2].lower()

    else:
        print('Incorrect Number Of Arguments Entered, Quitting...')
        sys.exit()

    return args

def main():
    
    args = checkArgs()
    key = args[1]
    mode = args[2]
    message = args[3]

    print(caesar(key, message, mode))





# def main():
#     args = checkArgs()
#     #message = util.getTextFromFile()
#     message = "The End Is Near"

    
#     key = 7

#     print(" Plaintext:", message)
#     ctext = caesar(key, message)
#     print("Ciphertext:", ctext)
#     ptext = caesar(-key, ctext)
#     print(" Decrypted:", ptext)
#     exit(0)

#     print("\nBrute-force decipherment:")
#     for shift in range(NUM_SYM):
#         guess = caesar(-shift, ctext)
#         print("Key =", shift, guess)
    

if __name__ == '__main__':
    main()

