
import vigenere
import re
import itertools
import time
from vigenereIC import keyLengthIC
import detectEnglish

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


ENG_LETT_FREQ= {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03,'C': 2.78,'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

def vigenereKeySolver(ciphertext, keyLength):
    
    possibleKeys = []
    # for case insensitivity, make everything uppercase
    ciphertext = ciphertext.upper()    
    
    # for storing each letters IMC value for each subsequence
    IMCT = {}
    for i in range(1, keyLength+1):
        #getting the subsequence of nth letters for a given keylength
        nthLetters = getNthSubkeysLetters(i, keyLength, ciphertext)
        nthLettersLen = len(nthLetters)

        #contains the IMC values for a subsequence of the nth letters when decrypted with each letter 
        IMC = []
        for letter in ALPHABET:
            currentIMC = 0
            #decrypt the subsequence with a single letter of the alphabet
            decryptedSubSeq = vigenere.vigenere(letter, nthLetters, 'decrypt')
            subSeqFreq = getFrequency(decryptedSubSeq, nthLettersLen)
            
            # find the sum for t(i) * e(i) for all letters
            for char in ALPHABET:
                currentIMC += subSeqFreq[char] * (ENG_LETT_FREQ[char]/100)

            IMC.append([currentIMC, letter])

        IMC.sort(key=lambda x: x[0], reverse=True)
   

        IMCT[str(i)] = IMC


    topTenKeys = getTopTenKeys(IMCT, keyLength)

    return topTenKeys
    #return a list containing the 10 most likely keys

def getTopTenKeys(allIMC, keyLength):
    # This function gets the top ten keys given the IMC(t) values and the key length
    # returns a list of the top 10 keys
    possibleKeys = []
    topTenKeys = []

    # This block finds the orders to be used. 
    # Hard coded for keylengths 1,2,3 to return the smallest amount of orders possible
    if keyLength == 1:
        orders = list(itertools.product(range(10), repeat=1))
    elif keyLength == 2:
        orders = list(itertools.product(range(4), repeat=2))
    elif keyLength == 3:
        orders = list(itertools.product(range(3), repeat=3))
    # once the keylength > 3, fin the orders consisting of only the first 2 places. 
    else:
        orders = list(itertools.product(range(2), repeat=keyLength))
   
    for order in orders:
        key, value = getKey(allIMC, order, keyLength)
        possibleKeys.append([value, key])

    #sort the possible keys by their values in descending order
    possibleKeys.sort(key=lambda x: x[0], reverse=True)
    #get the 10 highest key values in descending order
    for i in range(10):
        topTenKeys.append(possibleKeys[i][1])
    
    return topTenKeys

def getKey(allIMC, order, keyLength):
    # This function takes in the imc's calculated for each letter in each spot in the key
    # also takes in the key length and an order, returns the corresponding key and its value
    # The key, value corresponds to the order given i.e. ( 0,0,0,1)...
    key = ''
    value = 0
    for i in range(1, keyLength + 1):
        IMCt = allIMC[str(i)]
        value += IMCt[order[i-1]][0]
        key += IMCt[order[i-1]][1]

    return  key, value

def getFrequency(text, textLen):
    # This function takes in a text and text length, returns a dictionary of the
    # frequency of each letter in the alphabet
    textLetterFreq	= {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    for letter in text:
        #only increment in the dictionary if the letter is alphabetical 
        if letter.isalpha():
            textLetterFreq[letter] += 1

    for key in textLetterFreq.keys():
        textLetterFreq[key] = (textLetterFreq[key]/textLen)

    return textLetterFreq

# from VigenereHacker (Polyalphabetic Substitution Cipher)
# http://inventwithpython.com/hacking (BSD Licensed)
# Function taken from vigenere Hacker to avoid having to bundle additional libraries
def getNthSubkeysLetters(nth, keyLength, message):
    NONLETTERS_PATTERN = re.compile('[^A-Z]')
    # Returns every nth letter for each keyLength set of letters in text.
    # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
    #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
    #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

    # Use a regular expression to remove non-letters from the message:
    message = NONLETTERS_PATTERN.sub('', message)

    i = nth - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return ''.join(letters)

def hackVigenere(cipherText):

    possibleKeyLens = keyLengthIC(cipherText, 10)
    allPossibleKeys = []
    foundKeys = []
    keyDecipherments = {}

    for keyLength in possibleKeyLens:
        possibleKeys = vigenereKeySolver(cipherText, keyLength)
        allPossibleKeys += possibleKeys

    for key in allPossibleKeys:
        possibleDecipherment = vigenere.vigenere(key, cipherText, 'decrypt')
        keyDecipherments[key] = possibleDecipherment    
       
    singleKey = False
    wordPercent = 95
    totalRounds = 0
    while singleKey == False:
        foundKeys = []
        for key in keyDecipherments.keys():
            possibleDecipherment = keyDecipherments[key]
            isItEnglish = detectEnglish.isEnglish(possibleDecipherment, wordPercentage=wordPercent)
            if isItEnglish:
                foundKeys.append(key)
        
        if len(foundKeys) == 0:
            wordPercent -= 5
        elif len(foundKeys) == 1 or totalRounds > 25:
            # if a single key is found or the total rounds has been more than 25
            # break the loop and use the first key in the foundkeysList
            singleKey = True

        elif len(foundKeys) > 1:
            wordPercent += 1

        totalRounds += 1
        




    return foundKeys[0]

def crackPassword():
    start = time.time()
    file = 'password_protected.txt'
    fileContents = ''
    with open(file, 'r') as f:
        for line in f:
            fileContents += line
    key = hackVigenere(fileContents)
    print("\nTime Taken:", time.time()-start)
    print('Key used:', key)
    print('Decipherment:', vigenere.vigenere(key, fileContents, 'decrypt'))
    print()




def main():
    ciphertext = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCV\
KVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV" 
    a = vigenereKeySolver(ciphertext, 5)
    assert a[0] == 'EVERY'
    if a[0] == 'EVERY':
        print('First key is EVERY')

    ciphertext2 = 'QPWK ALVRXC QZIKGRB PFAEOMFL JMSD ZVDHXC XJ YEBIMTRQW NMEAI ZRVKC VKVLXN EIC FZPZCZZH KM LVZV ZIZR RQWDKECH OS NYXXL SPMYKV QXJT DCIOMEE XDQV SRXLRLKZH OV'
    print('\nFor hack Vignenere:')
    print("The key is:", hackVigenere(ciphertext2))
    print()

    crackPassword()




if __name__ == '__main__':
    main()



