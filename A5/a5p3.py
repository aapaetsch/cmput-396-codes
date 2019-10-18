import subEval
import simpleSubHacker
import os, sys

def getFileNames():
	fileNames = []
	files = os.listdir('texts')
	for file in files:
		name = file.split('_')
		if name[1] == 'plain':
			fileNames.append(file)
	return fileNames


def main():
	fileNames = getFileNames()
	freqAnalysisResults = {}
	simpleSubHackerResults = {}
	onlineResults = {}
	# Here we get the values from our freq analysis in part 1
	for file in fileNames:
		# The proper plain texts
		f1 = 'texts/'+file
		# The plain texts from frequency analysis
		f2 = file
		freqAnalysisResults[file] = subEval.evalFile(f1, f2)
		
		# Here we get the values of simpleSubHacker (the unmodified version)
		# we have to create new files here so that subEval can analyze it 
		cipherFileName = file.split('_')[0] + '_cipher' 
		cipherFileContent = subEval.openFileAsString('texts/'+cipherFileName)
		letterMapping = simpleSubHacker.hackSimpleSub(cipherFileContent)
		decryptedMessage = simpleSubHacker.decryptWithCipherletterMapping(cipherFileContent, letterMapping)
		
		hackSimpleSubFileName = file.split('_')[0] + '_plain_hackSimpleSub'
		with open(hackSimpleSubFileName, 'w') as f:
			f.write(decryptedMessage)

		simpleSubHackerResults[file] = subEval.evalFile(f1, hackSimpleSubFileName)

		# Here we get the values of the online hacker
		o2 = file+'_online'
		onlineResults[file] = subEval.evalFile(f1, o2)
	print('|----------|---------------------------------------|---------------------------------------|---------------------------------------|')
	print('|          |           Frequency Analysis          |            Textbook Solver            |              Online Solver            |')
	print('|Ciphertext|---------------------------------------|---------------------------------------|---------------------------------------|')
	print('|          |      Key Acc      |     Deciph Acc    |       Key Acc     |     Deciph Acc    |       Key Acc     |     Deciph Acc    |')
	print('|----------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|')
	for file in fileNames:
		f = file.split('_')[0]
		resultsString = ''
		flen = 10-len(f)
		resultsString+= '|'+ f +(' '*flen) + '|'
		fakey = str(freqAnalysisResults[file][0])
		fadec = str(freqAnalysisResults[file][1])
		txkey = str(simpleSubHackerResults[file][0])
		txdec = str(simpleSubHackerResults[file][1])
		resultsString += fakey + (' '*(19-len(fakey)))+'|' + fadec + (' '*(19-len(fadec)))+'|'
		resultsString += txkey + (' '*(19-len(txkey))) + '|'
		resultsString += txdec + (' '*(19-len(txdec))) + '|'
		olkey = str(onlineResults[file][0])
		oldec = str(onlineResults[file][0])
		resultsString += olkey + (' '*(19-len(olkey))) + '|'
		resultsString += oldec + (' '* (19-len(oldec))) + '|'

		print(resultsString)
		print('|----------|-------------------|-------------------|-------------------|-------------------|------------------|------------------|')









if __name__ == '__main__':
	main()