# Simple Substitution Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import re, copy, simpleSubCipher, wordPatterns, makeWordPatterns


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

    # Determine the possible valid ciphertext translations:

    print('Hacking...\n')
    hackedMessage = hackSimpleSub(message)
    print('Original Message:')
    print(message)
    print("\nHacking Results:")
    # Display the results to the user:
    print(hackedMessage)


def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping.
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def addLettersToMapping(letterMapping, cipherword, candidate):
    # The `letterMapping` parameter is a "cipherletter mapping" dictionary
    # value that the return value of this function starts as a copy of.
    # The `cipherword` parameter is a string value of the ciphertext word.
    # The `candidate` parameter is a possible English word that the
    # cipherword could decrypt to.

    # This function adds the letters of the candidate as potential
    # decryption letters for the cipherletters in the cipherletter
    # mapping.


    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])



def intersectMappings(mapA, mapB):
    # To intersect two maps, create a blank map, and then add only the
    # potential decryption letters if they exist in BOTH maps.
    intersectedMapping = getBlankCipherletterMapping()
    for letter in LETTERS:

        # An empty list means "any letter is possible". In this case just
        # copy the other map entirely.
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        else:
            # If a letter in mapA[letter] exists in mapB[letter], add
            # that letter to intersectedMapping[letter].
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
    # Cipherletters in the mapping that map to only one letter are
    # "solved" and can be removed from the other letters.
    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'
    # maps to ['N'], then we know that 'B' must map to 'N', so we can
    # remove 'N' from the list of what 'A' could map to. So 'A' then maps
    # to ['M']. Note that now that 'A' maps to only one letter, we can
    # remove 'M' from the list of letters for every other
    # letter. (This is why there is a loop that keeps reducing the map.)

    loopAgain = True
    while loopAgain:
        # First assume that we will not loop again:
        loopAgain = False

        # `solvedLetters` will be a list of uppercase letters that have one
        # and only one possible mapping in `letterMapping`:
        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # If a letter is solved, than it cannot possibly be a potential
        # decryption letter for a different ciphertext letter, so we
        # should remove it from those other lists:
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        # A new letter is now solved, so loop again.
                        loopAgain = True
    return letterMapping


def hackSimpleSub(message):
    #open the dictionary file and save it into a list so we only have to open it once
    dictionaryFile = 'dictionary.txt'
    dictionaryList = []
    with open(dictionaryFile, 'r') as f:
        for i in f:
            # Strip all '\n' characters from each of the dictionary words
            dictionaryList.append(i.strip('\n'))

    #<---Start of textbook code --->
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
    for cipherword in cipherwordList:
        # Get a new cipherletter mapping for each ciphertext word:
        candidateMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue # This word was not in our dictionary, so continue.

        # Add the letters of each candidate to the mapping:
        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)

        # Intersect the new mapping with the existing intersected mapping:
        intersectedMap = intersectMappings(intersectedMap, candidateMap)

    # Remove any solved letters from the other lists:
    firstMapping = removeSolvedLettersFromMapping(intersectedMap)
    underscoredText = decryptWithCipherletterMapping(message, firstMapping)
    #<---End of textbook code--->

    #<-------------- Start of my code ---------->
    # Turn the original text and the underscored text produced from the first mapping into two lists
    underscoredTextList = underscoredText.split(' ')
    originalMessageList = message.split(' ')

    # allPossibleLetters is a list of dictionaries that will be populated from the possible letter mappings
    # That are produced below
    allPossibleLetters = []
    for wordIndex in range(len(underscoredTextList)):
        # Get a word from the text and the matching cipher word
        word = underscoredTextList[wordIndex]
        cipherWord = originalMessageList[wordIndex]

        #if there's a missing character in the word we continue
        if '_' in word:
            
            # Strip all punctuation that would affect the dictionary search           
            punctuation = ['.',',','!','?',')','(','*','-', "'",'"']
            for i in punctuation:
                word = word.strip(i)
                cipherWord = cipherWord.strip(i)
            regularexpression = word

            # Here we create the regex token
            # If the word has an s at the end, search the dictionary for the word with and without an S
            # I assume that s denotes plural and plural words will not be in the dictionary
            if regularexpression[-1].lower() == 's':
                regularexpression = regularexpression + '?'
            # Replace _ with . to search for anything in that place     
            regularexpression = '^'+regularexpression.upper().replace('_', '.')+'$'

            # call checkWord function, returns a list of possible dictionary matches 
            foundWords = checkWord(regularexpression, dictionaryList)

            # Create a dictionary for possible letter matches, keys are the cipherWord letter
            # value is a list of possible letters to replace that cipherLetter
            possibleLetters = {}
            for i in range(len(word)):
                if word[i] == '_':
                    # Find the corresponding letter in the possible word[s] for a missing letter
                    possibleLetters[cipherWord[i].upper()] = []
                    for possibleWord in foundWords:
                        possibleLetters[cipherWord[i].upper()].append(possibleWord[i])
                    
            allPossibleLetters.append(possibleLetters)
    
    # here we update the initial mapping
    # for each set of possible letters, this is per word that contained a _ after the initial mapping
    for letterSet in allPossibleLetters:
        # For each key in the letter set, check if it is in the initial mapping, if not remove it from the set
        for key in letterSet.keys():
            for possibleLetter in letterSet[key]:
                    if possibleLetter not in firstMapping[key]:
                        letterSet[key].remove(possibleLetter)

            # Assuming at this point, we should be left with one to one pairs in the letterSet
            if len(letterSet[key]) == 1:
                # update the mapping to those one to one pairs 
                # This is only done if the first mapping is not already a one to one pair (not really needed but an additional check) 
                if letterSet[key][0] in firstMapping[key]:
                    if len(firstMapping[key]) > 1:
                        firstMapping[key] = letterSet[key]
    # remove solved letters from mapping to get rid of any mappings that still might contain multiple letters (again this is a precaution)
    secondMapping = removeSolvedLettersFromMapping(firstMapping)
    # return the complete message after decoding the ciphertext with the updated mapping
    completedMessage = decryptWithCipherletterMapping(message, secondMapping)
    
    return completedMessage


#This function is from the repython slides from class
#It has been modified to take in a dictionary so we do not have to open it each time we search
#https://eclass.srv.ualberta.ca/pluginfile.php/5220613/mod_resource/content/2/rePython.pdf
def checkWord(regex, dictionaryList):
    resList = []
    # If a word in the dictionary list matches the regex token, append to the results list
    for word in dictionaryList:
        if re.match(regex,word):
            resList.append(word)

    return resList

def decryptWithCipherletterMapping(ciphertext, letterMapping):
    # Return a string of the ciphertext decrypted with the letter mapping,
    # with any ambiguous decrypted letters replaced with an _ underscore.

    # First create a simple sub key from the letterMapping mapping:
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key.
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext:
    return simpleSubCipher.decryptMessage(key, ciphertext)


if __name__ == '__main__':
    main()