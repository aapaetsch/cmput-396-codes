import a9p1
import a9p2

def bestSuccessor(mapping, ciphertext, frequencies, n):
    #Return the succesor with the highest score, otherwise return its successor
    ciphertext = a9p1.cleanText(ciphertext)
    score = a9p2.keyScore(mapping, ciphertext, frequencies, n)
    
    remainingSwaps = list(mapping.keys())
    if ' ' in remainingSwaps:
    	remainingSwaps.remove(' ')
    
    bestMapping = mapping.copy()

    # here we check every possible swap for a given mapping and save
    # the one with the highest mapping score
    while len(remainingSwaps) != 0:
    	#poping the first item in the list allows us to not have to visit it again
    	currentKey = remainingSwaps.pop(0)
    	
    	for keyToSwap in remainingSwaps:
            #here we save the possible successor mapping and its score
    		possibleSuccessor = swap(mapping.copy(), currentKey, keyToSwap)
    		possibleSuccessorScore = a9p2.keyScore(possibleSuccessor, ciphertext, frequencies, n)
    		# we only change the best mapping if the score is better than the previous best
            # Ties are dealt with by a first come basis. If two mappings are identical in score we take the first one. 
    		if possibleSuccessorScore > score:		
    			score = possibleSuccessorScore
    			bestMapping = possibleSuccessor.copy()
    			
    return bestMapping

def swap(mapping, k1, k2):
    # This function takes in a mapping and two keys
    # swaps their values and returns the resulting mapping
	temp = mapping[k1]
	temp2 = mapping[k2]
	mapping[k1] = temp2
	mapping[k2] = temp
	return mapping



def testSuccessor():
	freqText = 'aabbababbbeeab'
	cipherText = "aabbababbbeeab"
	n = 2
	frequencies = a9p1.ngramsFreqs(freqText, n)
	mapping1 = {'A': 'A', 'B': 'B', 'E': 'E'}
	mapping2 = {'A': 'E', 'B': 'B', 'E': 'A'}
	bestMapping1 = bestSuccessor(mapping1, cipherText, frequencies, n)
	print("Best Mapping found:", bestMapping1)
	print()
	bestMapping2 = bestSuccessor(mapping2, cipherText, frequencies, n)
	print("Best Mapping found:", bestMapping2)


def main():
    testSuccessor()



if __name__ == "__main__":
    main()
