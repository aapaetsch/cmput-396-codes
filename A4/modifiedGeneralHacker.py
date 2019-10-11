# Affine and Transposition Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import os, sys, util, a1p2, detectEnglish
import cryptomath, caesar, affineCipher, transposition
from itertools import permutations
SILENT_MODE = True
outputFile = 'deciphered.txt'
def hack(cipherType, ciphertext, allPermutations):
    if cipherType == 'caesar':
        keyRange = range(caesar.NUM_SYM)
    elif cipherType == 'transposition':
        keyRange = allPermutations
    elif cipherType == 'affine':
        keyRange = range(len(affineCipher.SYMBOLS) ** 2)
    else:
        print("Unknown cipher type: %s" % cipherType)
        sys.exit()

    print('Hacking...')
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    for key in keyRange:

        if cipherType == 'caesar':
            decrypted = caesar.caesar(-key, ciphertext)
        elif cipherType == 'transposition':
            decrypted = a1p2.decryptMessage(key, ciphertext)
        elif cipherType == 'affine':
            keyA = affineCipher.getKeyParts(key)[0]
            if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
                continue
            decrypted = affineCipher.decryptMessage(key, ciphertext)

        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decrypted[:40]))

        if detectEnglish.isEnglish(decrypted):
            print('\nPossible encryption hack:', ciphertext)
            print('Key %s: %s' % (key, decrypted[:200]))
            print('\nEnter D for done, or press Enter')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                with open(outputFile, 'a') as f:
                    f.write(cipherType + '    '+decrypted )
                return decrypted

    return None

def main():
    ciphertexts = []
    allPermutations = []
    currentSet = []
    for i in range(1,10):
        currentSet.append(i)
        allPermutations += list(permutations(currentSet))

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        
        if not os.path.exists(filename):
            print('The file %s does not exist' % (filename))
            sys.exit()
        
        else:
            with open(filename, 'r') as f:
                for ct in f:
                    ciphertexts.append(ct)
    else:
        print('Error, no cipher file provided.')
        sys.exit()


    for line in range(len(ciphertexts)):
        ciphertext = ciphertexts[line]
        for cipherType in ['caesar', 'affine', 'transposition']:
        
            if len(sys.argv) > 2:
                cipherType = sys.argv[2]

            hackedMessage = hack(cipherType, ciphertext, allPermutations)

            if hackedMessage == None:
                print('Failed to hack encryption with type', cipherType)
                if cipherType == 'transposition':
                    with open(outputFile, 'a') as f:
                        f.write(str(line+1) +'failed\n')
            else:
                print(hackedMessage)
                break
    

if __name__ == '__main__':
    main()
