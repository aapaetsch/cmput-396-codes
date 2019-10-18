import os

# f1: the name of a file containing the original plaintext of an encrypted message
# f2: the name of a file containing an imperfect plaintext that was deciphered by some method
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def evalFile(f1, f2):
    # correct and total are used for calculating decipher accuracy
    correct = 0
    total = 0

    # For recording if a character has been mapped correctly
    keyAccuracyDict = {}

    # Open the two files that need to be compared as strings
    f1Contents = openFileAsString(f1)
    f2Contents = openFileAsString(f2)
    
    # Get the length of the files to be compared (both files are of the same length)
    fileLength = len(f1Contents)
    for i in range(fileLength):

    	# Since substitution cipher only substitutes alphabetical characters and leaves other characters alone
    	# we only need to check if the character in one file is alphabetical
    	if f1Contents[i] in LETTERS:

    		# Check if the char in the first file at index i matches the char in the second file at index i
    		if f1Contents[i] == f2Contents[i]:
    			
    			# If it matches add 1 to our decipher accuracy score
    			correct += 1

    			# If we have not yet seen this character and it is correct
    			if f1Contents[i] not in keyAccuracyDict.keys():
    				# Update the key accuracy dictionary to say this character was mapped correctly
    				keyAccuracyDict[f1Contents[i]] = 1 

    		else:

    			# If we have not yet seen this character and it is incorrect
    			if f1Contents[i] not in keyAccuracyDict.keys():
    				# Update the key accuracy dictionary to say this character was mapped incorrectly
    				keyAccuracyDict[f1Contents[i]] = 0
    		
    		# Add one to the total characters seen only if it is alphabetical
    		total += 1

    # Calculate decipher accuracy, correct
    decipherAccuracy = correct/total

    # Find the total distinct alphabetical characters and total correctly mapped distinct alphabetical characters
    keyAccuracy = {'Correct': 0, 'Total':0 }
    for key in keyAccuracyDict.keys():
    	# We can just add 1 to Total for each key and add the key's value to the correct count as we recorded them as a 1 or 0
    	keyAccuracy['Correct'] += keyAccuracyDict[key]
    	keyAccuracy['Total'] += 1
    	
    return (keyAccuracy['Correct']/keyAccuracy['Total'] , decipherAccuracy)
    	





def openFileAsString(fileName):
	fileAsString = ''
	with open(fileName, 'r') as f:
		for line in f:
			fileAsString += line

	return fileAsString.upper()


def main():

	files = os.listdir('texts')
	for file in files:
		name = file.split('_')
		if name[1] == 'plain':
			f1 = 'texts/'+file
			f2 = file
			print(file + ':')
			print(evalFile(f1, f2))
			print()

			


if __name__ == '__main__':
    main()
