import a9p1
import a9p2
import a9p3


def breakSub(ciphertext, freqtext, maxN):
	# This function takes in a ciphertext, frequency text and maxN
	# returns the deciphered texted based on the final mapping
	freqTextString = a9p1.cleanText(freqtext)
	#I keep a version of ciphertext that only has spaces fixed so that the final decipherment will keep punctuation. 
	ciphertext = ' '.join(ciphertext.split())
	cleanciphertext = a9p1.cleanText(ciphertext)
	
	#We make the initial mapping from the ciphertext and ETAOIN order
	mapping = makeMapping(cleanciphertext)


	n = maxN 
	#copy the dictonary so changes to mapping dont result in changes to inputMapping
	inputMapping = mapping.copy()
	
	#We run this loop from maxN till n = 1
	while n > 0:
		
		#We must create a new frequencies dictionary each time n changes
		frequencies = a9p1.ngramsFreqs(freqTextString, n)
		#Get the initial successor mapping
		successorMapping = a9p3.bestSuccessor(inputMapping.copy(), cleanciphertext, frequencies, n)

		# We must continue finding successor mappings until the best possible successor mapping has been found
		# for a given n value
		while True:
			# if a successorMapping matches an inputMapping it is the best possible successor
			# therefore we break the loop and decrease n by 1
			if successorMapping == inputMapping:
				break
			
			else:
				# if successorMapping and inputMapping do not match, the best possible successor has not been found
				inputMapping = successorMapping.copy()
				successorMapping = a9p3.bestSuccessor(inputMapping.copy(), cleanciphertext, frequencies, n)
		
		n -= 1

	plaintext = decipher(successorMapping, ciphertext)
	print("Best Mapping:", inputMapping)
	return plaintext


def decipher(mapping, ciphertext):
	# this function deciphers a cipher text based off of a mapping
	plaintext = ''
	for char in ciphertext:
		if char in mapping.keys():
			plaintext += mapping[char]
		else:
			# spaces are put into plaintext as is. preprocessing gets rid of all non ' ' or uppercase alphabetical characters
			plaintext += char
	return plaintext	


def makeMapping(ciphertext):
	# this function takes in a ciphertext and makes an initial mapping to ETAOIN frequency
	ciphertext = "".join(ciphertext.split(' '))
	cipherFreq = a9p1.ngramsFreqs(ciphertext, 1)
	cipherFreqList = dictToList(cipherFreq)
	cipherFreqList.sort(key = lambda x:x[1], reverse=True)

	ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
	mapping = {}
	for i in range(len(cipherFreqList)):
		mapping[cipherFreqList[i][0]] = ETAOIN[i]
	
	return mapping



def dictToList(dictionary):
	#this function changes a dictionary into a list of lists with k,v pairs
	dictList = []
	for key in dictionary.keys():
		dictList.append([key, dictionary[key]])
	return dictList



def testa9p4():
	ciphertext = "VE AYO Y FGVUQE INXK KYC VP YMGVX"
	plaintext = "IT WAS A BRIGHT COLD DAY IN APRIL"
	freqtextfile = "text_for_eng_freq.txt"
	maxN = 2
	freqTextString = ''
	with open(freqtextfile,'r') as f:
		for line in f:
			freqTextString += line
	decipherment = breakSub(ciphertext, freqTextString, maxN)
	print(decipherment)



def main():
	testa9p4()

if __name__ == '__main__':
	main()