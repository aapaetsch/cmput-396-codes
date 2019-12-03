def ngramsFreqs( text , n ):
	#return a dictionary 
		#keys = character n-gram ( single string)
		#values = relative frequency of ngram in string of text
			#n-gram occurance/ total # of character n-grams in string
	text = text.upper()
	text = " ".join(text.split())
	frequency = {}
	total = 0
	textLen = len(text)

	#here we find the frequency of an ngram in the text
	for i in range(textLen):

		gram = text[i:i+n]

		if gram in frequency.keys():
			frequency[gram] += 1

		else:
			frequency[gram] = 1

		total += 1
		# break onces the index of the end of the ngram is also the end index of the text
		if (i + n) == textLen:
			break

	# here we calculate each ngram frequency over the total ngrams in a text
	for key in frequency.keys():

		frequency[key] = frequency[key] / total

	return frequency



def cleanText(inputText):
	# this function cleans all extra spaces and non alphabetical characters
	inputText = inputText.upper()
	inputText = " ".join(inputText.split())
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	outputText = ''
	for char in inputText:
		if char in LETTERS or char == " ":
			outputText += char
	return outputText




def main():
	text = "AN EXAMPLE"
	
	for i in range(1,6):
		ngramsFreqs(text, i)
	
	textTxt = ""
	with open("text_for_eng_freq.txt",'r') as f:
		for line in f:
			textTxt += line
	textTxt = cleanText(textTxt)
	

	freq = ngramsFreqs(textTxt, 1)
	print("KV pairs:")
	
	for key in freq.keys():
		print("\tKey:", key, "Value:",freq[key])





	

if __name__ == '__main__':
	main()
