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

	if not keyIsValid(subKey):
		sys.exit('There is an error in the key or symbol set.')

	message = message.split(' ')
	for word in range(len(message)):
		keys = codeBook.keys()
		for key in keys:
			if key.lower() == message[word].lower():
				message[word] = random.choice(codeBook[key]) 
				break
	message = ' '.join(message)

	for symbol in message:
		if symbol.upper() in charsA:
			symIndex = charsA.find(symbol.upper())
			if symbol.isupper():
				translated += charsB[symIndex].upper()
			else:
				translated += charsB[symIndex].lower()
		else:
			translated += symbol
		


	return translated

def decryptMessage(subKey, codeBook, message):
	charsA = subKey
	charsB = LETTERS
	translated = ''
	
	if not keyIsValid(subKey):
		sys.exit('There is an error in the key or symbol set.')

	for symbol in message:
		if symbol.upper() in charsA:
			symIndex = charsA.find(symbol.upper())
			if symbol.isupper():
				translated += charsB[symIndex].upper()
			else:
				translated += charsB[symIndex].lower()
		else:
			translated += symbol


	translated = translated.split(' ')
	for word in range(len(translated)):
		keys = codeBook.keys()
		try:
			i = int(translated[word])
			for key in keys:
				if translated[word] in codeBook[key]:
					translated[word] = key
		except:
			continue
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
