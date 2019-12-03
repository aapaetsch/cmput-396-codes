from a9p1 import ngramsFreqs

def keyScore(mapping, ciphertext, frequencies, n):
	#returns the n-gram score (floating point number), 
	#computed given that a mapping, ciphertext (given as a string)
	#an ngram frequency dictionary (such as is returned by your ngramsFreqs function)
	#and the n-gram parameter n

	ciphertext = ciphertext.upper()
	ciphertext = " ".join(ciphertext.split())

	plainText = ""
	cipherTextLen = len(ciphertext)

	#this block deciphers a ciphertext with the input mapping
	for i in range(cipherTextLen):
		
		char = ciphertext[i]
		
		if char in mapping.keys():
			plainText += mapping[ciphertext[i]]

		else:
			plainText += char

	c = {}
	for i in range(cipherTextLen):
		#here we get an n-gram from the plain text
		gram = plainText[i:i+n]
		#increment the frequency of that n-gram
		if gram in c.keys():
			c[gram] += 1
		
		else:
			c[gram] = 1
		#Since n-grams are incremented 1 by 1 we must stop when the index of the end of the n-gram is
		# also the index of the end of the ciphertext
		if (i + n) == cipherTextLen:
			break

	scores = []
	for key in c.keys():
		#only add to the scores if the n-gram is also in the ciphertext
		try:
			scores.append(c[key] * frequencies[key])
		except:
			continue
	#return a sum of all the valid scores
	return sum(scores)




	





def testa9p2():
	freqText = 'aabbababbbeeab'
	cipherText = 'aabbababbbeeab'
	
	defaultMapping = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}
	
	newMapping = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'H', 'F': 'F', 'G': 'G', 'H': 'E', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}
	
	n = 2
	
	frequencies = ngramsFreqs(freqText, 2)

	defaultScore = keyScore(defaultMapping, cipherText, frequencies, n)
	newScore = keyScore(newMapping, cipherText, frequencies, n)
	
	print("\tScore for n=2, default mapping:", str(defaultScore))
	print("\tScore for n=2, new mapping:", str(newScore))

def main():
	testa9p2()


if __name__ == "__main__":

	main()
