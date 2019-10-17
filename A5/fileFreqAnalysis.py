#Partially adapted from freqAnalysis https://www.nostarch.com/crackingcodes (BSD Licensed)

import os
import freqAnalysis

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def freqDict( f1, frequency):
	# Keys are cipher characters, values are plaintext equiv
    cipherDict = {}
    # Keys are each letter in the alphabet, start with each value being 0
    for letter in LETTERS:
    	cipherDict[letter] = ''
    
    # Open the file and get its contents as a string
    inputFileContents = openFileAsString(f1)

    # Do frequency analyis using the function from freqAnalysis (Tested against my own implementation, results are identical, calling this function is cleaner)
    fromFreqAnalysis = freqAnalysis.getFrequencyOrder(inputFileContents)
    for i in range(len(frequency)):
    	cipherDict[fromFreqAnalysis[i]] = frequency[i] 

    # Return cipherDict which is the mapping to be used in decrypt
    return cipherDict
    

def freqDecrypt( f1, f2, frequency):
    
    # Get the frequency mapping from freqDict
    mapping, mapping2 = freqDict(f1, frequency)
    # Get the input file as a string
    cipherText = openFileAsString(f1)

    plainText = ''
    # Using the cipherText uppercase letters
    for letter in cipherText.upper():
    	# Check if a character is in LETTERS (the alphabet)
    	if letter in LETTERS:
    		# If it is, use the mapping and append the plaintext letter to plainText
    		plainText += mapping[letter]
    	else:
    		# If not, simply add the character to the planText string
    		plainText += letter

    # Make a file named from f2 and write the plainText as its content
    makeFile(f2, plainText)
    

def getItemAtIndexOne(items):
	# This function is used in sort, gets the item in index 1 and returns it
	return items[1]


# def countLetters(content, letterFreqDict):
# 	# This function takes in content and a dictionary with k,v pairs k = Letter in alphabet, v = 0 (to be incremented)
# 	# Turns the content to uppercase
# 	for letter in content.upper():
# 			# Checks if the character is in LETTERS ( the alphabet)
# 			if letter in LETTERS:
# 				# Increments the Letter by 1 to get its frequency
# 				letterFreqDict[letter] += 1
# 	# Returns the input dictionary with the frequency
# 	return letterFreqDict


def openFileAsString(fileName):
	# This function takes in a file name, reads it and returns a string of the file contents
	fileContents = []
	with open(fileName, 'r') as f:
		for line in f:
			fileContents.append(line)
	return ''.join(fileContents)


def makeFile(fileName, content):
	# This function takes in a file name and some content and
	# Creates a file with that name, writing the content to it
	with open(fileName, 'w') as f:
		f.write(content)


def main():

    #gets all the files in the texts folder, uses those ending in cipher as
    #the cipher text and creates the output name from the part before cipher+_plain
	files = os.listdir('texts')
	for file in files:
		name = file.split('_')
		if name[1] == 'cipher':
			freqDecrypt('texts/' + file , name[0] + '_plain', ETAOIN)


if __name__ == '__main__':
    main()
