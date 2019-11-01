import sys
import re
import vigenere

def stringIC(inputstr):
	# This function takes in a string and calclulates its IC value from it 
	# returns 0 in calses of a divide by 0 error
	N = len(inputstr)
	chars = {}
	# making sure that this is case insensitive
	for char in inputstr.upper():
		#incrementing a character if it is in the keys, make a new k,v pair if not = 1
		if char in chars.keys():
			chars[char] += 1
		else:
			chars[char] = 1
	numerator = 0
	denominator = N*(N - 1)
	
	if denominator == 0:
		return 0

	for key in chars.keys():
		numerator += (chars[key]*(chars[key]-1))

	return numerator/denominator


def subseqIC(ciphertext, keylen):
	# This function takes in the cipher text and key length 
	# returns the IC value for a given ciphertext 
    ICScores = []

    for i in range(keylen):
        nth = i+1
        subseq = getNthSubkeysLetters(nth, keylen, ciphertext.upper())
        ICScores.append(stringIC(subseq))

    return sum(ICScores)/len(ICScores)


def keyLengthIC(ciphertext, n):
	# This function returns the top n possible key lengths
	# has been edited from the a6 version. Only does key lengths from 1 -> 10
	# now implements subseqIC for scores
	keyIC = []
	#calculate the avg IC Scores for each key length
	for keyLen in range(1,11):
		
		ICScores = []
		for j in range(keyLen):
			nth = j + 1
			#get a subsequence for that key length
			
			# calculates the sum of fi^2 for a given subsequence
			
			ICscore = subseqIC(ciphertext, keyLen)
			ICScores.append(ICscore)
		
		lenICScores = len(ICScores)
		sumICScores = sum(ICScores)
		avgICScores = sumICScores / lenICScores
		# Append the averages to the key IC list
		keyIC.append([avgICScores, keyLen])

	#sort the keyIC by the scores in descending order	
	keyIC.sort(key=lambda x: x[0], reverse=True)
	
	#Extract the key lengths from the 2d list
	keyValues = []
	for i in range(n):
		keyValues.append(keyIC[i][1])
	
	return keyValues

def calculateFiValues(subseq):
	# This function calculates the sum of fi ^2 for an input subsequence

	chars = {}
	
	for char in subseq.upper():
		if char in chars.keys():
			chars[char] += 1
		else:
			chars[char] = 1
	
	N = len(subseq)
	if N == 0:
		return 0
	
	Fi2Values = []
	for key in chars.keys():
		Fi = chars[key] / N
		Fi2 = (Fi**2) 
		Fi2Values.append(Fi2)
	
	return sum(Fi2Values)


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


def main():
    # inputstr = 'ABA'
    # print(stringIC(inputstr))
    # print()
    # inputstr2 = 'A'
    # print(stringIC(inputstr2))
    # print()
    # for i in range(3):
    #     print('subseqIC("PPQCAXQVEKGYBNKMAZUHKNHONMFRAZCBELGRKUGDDMA",', str(3+i), ')')
    #     print(subseqIC("PPQCAXQVEKGYBNKMAZUHKNHONMFRAZCBELGRKUGDDMA", 3+i))
    #     print()

    # Testing Key Length IC
    # ct = "PPQCAXQVEKGYBNKMAZUHKNHONMFRAZCBELGRKUGDDMA"
    # klIC = keyLengthIC(ct, 10)
    # print(klIC)
   
    ciphertext1 = vigenere.vigenere('WAVING','ASHFORDISATOWNINFONDDULACCOUNTYWISCONSINUNITEDSTATESTHEPOPULATIONWASATTHECENSUSTHEUNINCORPORATEDCOMMUNITIESOFASHFORDANDELMOREARELOCATEDINTHETOWN', 'encrypt' )
    ciphertext2 = vigenere.vigenere('QWERTYUI', 'CONSIDEREDBYSOMETOBEAFATHEROFTHECOMPUTERBABBAGEISCREDITEDWITHINVENTINGTHEFIRSTMECHANICALCOMPUTERTHATEVENTUALLYLEDTOMORECOMPLEXELECTRONICDESIGNSTHOUGHALLTHEESSENTIALIDEASOFMODERNCOMPUTERSARETOBEFOUNDINBABBAGESANALYTICALENGINEHISVARIEDWORKINOTHERFIELDSHASLEDHIMTOBEDESCRIBEDASPREEMINENTAMONGTHEMANYPOLYMATHSOFHISCENTURY', 'encrypt')
    print("First Test:")
    print(keyLengthIC(ciphertext1, 5))
    print('\nSecond Test:')
    print(keyLengthIC(ciphertext2, 5))



if __name__ == '__main__':
    main()



