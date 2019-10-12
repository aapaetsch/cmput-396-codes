#encryptMessage modified from simple substitution cipher
#decryptMessage modified from simple substitution cipher
#keyIsValid Taken from simple substitution cipher
#https://www.nostarch.com/crackingcodes (BSD Licensed)


import re, sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encryptMessage(subKey, codeBook, message):
	translated = ''
	charsA = LETTERS
	charsB = subKey
	# check if the key given is valid, otherwise quit
	if not keyIsValid(subKey):
		sys.exit('There is an error in the key or symbol set.')

	# Split the message by spaces into a list
	message = message.split(' ')
	for word in range(len(message)):
		# Get the keys from the code book
		keys = codeBook.keys()
		for key in keys:
			# Search the codebook using lowercase to get rid of case sensitivity in the dictionary
			if key.lower() == message[word].lower():
				# if a word matches a key, replace it with a random choice of its number values
				message[word] = random.choice(codeBook[key]) 
				# once we replace the word, break from this loop
				break
	# Turn the message back into a string from the list
	message = ' '.join(message)

	# After replacing the codebook words with numbers, replace the letters by the corresponding symbol
	for symbol in message:
		if symbol.upper() in charsA:
			#find the corresponding letter in the key for each letter in plain text
			symIndex = charsA.find(symbol.upper())
			# Keep the case for each replacement
			if symbol.isupper():
				translated += charsB[symIndex].upper()
			else:
				translated += charsB[symIndex].lower()
		# do nothing to symbols, only add them back into the cipher text as is
		else:
			translated += symbol
		
	return translated

def decryptMessage(subKey, codeBook, message):
	# Decrypt message reverses what chars A and B are to do the reverse of encrypting the message
	charsA = subKey
	charsB = LETTERS
	translated = ''
	# check if the key given is valid, otherwise quit
	if not keyIsValid(subKey):
		sys.exit('There is an error in the key or symbol set.')

	# for each symbol in the message, replace the cipherletter with its corresponding plain text letter
	for symbol in message:
		if symbol.upper() in charsA:
			symIndex = charsA.find(symbol.upper())
			# keep the proper cases
			if symbol.isupper():
				translated += charsB[symIndex].upper()
			else:
				translated += charsB[symIndex].lower()
		# do nothing to symbols, adding them back in as is 
		else:
			translated += symbol

	# now we split the now plaintext with numbers by spaces
	translated = translated.split(' ')
	for word in range(len(translated)):
		# for each number that is in the plain text
		keys = codeBook.keys()
		try:
			#search the values of each key for that number
			i = int(translated[word])
			for key in keys:
				if translated[word] in codeBook[key]:
					#then replace the number with the key from the codebook
					translated[word] = key
		# if a number does not exist in the code book then it is just a number
		except:
			continue
	# turn the list back into plaintext and return it.
	translated = ' '.join(translated)

	return translated







def keyIsValid(key):

	keyList = list(key)
	lettersList = list(LETTERS)
	keyList.sort()
	lettersList.sort()
	return keyList == lettersList

def regexMatch(expression, text):
	if re.match(expression, text):
		print('Cipher Text Matches')
	
	else:
		print('Cipher Text Incorrect')
	
	print(text,'\n')

def correctDecipher(message, deciphered):
	if message == deciphered:
		print('Deciphered text matches original message')

	else:
		print('Deciphered text does not match original message')
	
	print(deciphered, '\n')

def main():
	
	mySubKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
	codebook = {'university':['1', '2', '3'], 'examination':['4','5'], 'examinations':['6','7','8'], 'WINTER':['9']}
	plaintext = '''At the university of Alberta, examinations take place in December and April
for the Fall and WINTER terms'''
	ciphertext1 = encryptMessage(mySubKey, codebook, plaintext)
	regexToken = '^Lj jia [123] py Lmfacjl, [678] jlka bmlwa sx Oawanfac lxo Lbcsm ypc jia Ylmm lxo 9 jacnr$'
	regexMatch(regexToken, ciphertext1)

	ciphertext2 = encryptMessage(mySubKey, codebook, plaintext)
	regexMatch(regexToken, ciphertext2)

	deciphertext1 = decryptMessage(mySubKey, codebook, ciphertext1)
	correctDecipher(plaintext, deciphertext1)

	deciphertext2 = decryptMessage(mySubKey, codebook, ciphertext2)
	correctDecipher(plaintext, deciphertext2)

if __name__ == '__main__':
	main()
