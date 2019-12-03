import a9p1
import a9p2
import a9p3
import a9p4

def incrementMaxN(ciphertext, plaintext, freqtext):
	ciphertext = ciphertext.upper()
	plaintext = plaintext.upper()
	maxN = 1
	previousDecipherAcc = 0

	while True:
		print("maxN:",maxN)
		decipherment = a9p4.breakSub(ciphertext, freqtext, maxN)
		plaintext = " ".join(plaintext.split())
		decipherAcc = getDecipherAcc(decipherment, plaintext)
		print("Attempted cipherment:", decipherment)
		print("Decipher Accuracy:", decipherAcc)
		print()
		if decipherAcc > previousDecipherAcc:
			#as long as we get higher decipherment accuracies, increase maxN
			previousDecipherAcc = decipherAcc

		else:
			break
		maxN += 1
	print("END\n")



def getDecipherAcc(attemptedDecipherment, correctDecipherment):
	# Since assignment 5 used files directly for decipherment scores, it was easier to rewrite 
	# a function based off of it. 
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	correct = 0
	total = 0

	attemptedDecipherment = attemptedDecipherment.upper()
	correctDecipherment = correctDecipherment.upper()
	print(correctDecipherment)
	for i in range(len(attemptedDecipherment)):
		# only count alphabetical characters
		if attemptedDecipherment[i] in LETTERS:
			# if the decipherment character matches the correct character, increment correct character count by 1
			if attemptedDecipherment[i] == correctDecipherment[i]:
				correct += 1
			total += 1
	#decipherment accuracy is the total correct characters(not keys) over the total characters in the text
	return correct/total

def main():
	ciphertext = 'VE AYO Y FGVUQE INXK KYC VP YMGVX'
	plaintext = 'IT WAS A BRIGHT COLD DAY IN APRIL'

	freqtextfile = "text_for_eng_freq.txt"
	freqTextString = ''
	with open(freqtextfile,'r') as f:
		for line in f:
			freqTextString += line

	incrementMaxN(ciphertext, plaintext, freqTextString)

	#Testing with the actual files
	ciphertext2 = ''
	with open('ciphertext.txt','r') as f:
		for line in f:
			ciphertext2 += line

	plaintext2 = ''
	with open('plaintext.txt', 'r') as f:
		for line in f:
			plaintext2 += line
	

	incrementMaxN(ciphertext2, plaintext2, freqTextString)



	

if __name__ == '__main__':
	main()