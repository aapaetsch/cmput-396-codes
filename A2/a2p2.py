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
    if mode == 'decrypt':
        key = -key
    shift = 0
    for i in range(len(message)):
        num = util.let2ind(messageUpper[i])

        if (num < 0) or (num >= NUM_SYM):
            translated.append(messageUpper[i])

        else:
            
            if mode == 'encrypt':
                num = (num + key) % NUM_SYM
                key = num
            elif mode == 'decrypt':
                num = (num - key) % NUM_SYM
                key = (num + key) % NUM_SYM
            letter = util.ind2let(num)

            if message[i].isupper():
                letter = letter.upper()
            else:
                letter = letter.lower()

            translated.append(letter)
            
    
    return ''.join(translated)


def checkArgs():
    args = sys.argv

    if len(args) == 4:

        try:
            args[1] = int(args[1])

        except:
            print("Error, Invalid value for key, must be an Int, Quitting...")
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

