import vigenere
import time
import random

def antiKasiski(key, plaintext, chars):
    
    key = key.upper()
    # Turn chars into a list to use random.choice
    chars = list(chars)
    repetitions = True

    while repetitions:

        # we must get the new cipher text after each insertion 
        cipherText = vigenere.vigenere(key, plaintext, 'encrypt')
        # find the first instance of a repeating subsequence
        substring, index= locateRepetitions(cipherText)

        # stop the loop once no more repetitions are found 
        if substring == None :
            repetitions = False
        else:
            plaintext = insertChar(index, chars, plaintext)
            repetitions = True

    return plaintext
    	
def insertChar(index, chars, plaintext):
    # This function chooses a random character from chars to insert into the plain text
    # before the start of the repeat sequence
    char = random.choice(chars)
    plaintext = plaintext[:index] + char + plaintext[index:]
    return plaintext



def locateRepetitions(cipherText):
    # This function takes in the cipherText and returns the string and index
    # of the first repeating subsequence
    lengthOfSubstring = 3
    textLen = len(cipherText)
    visited = {}
    # The repeating sequence is max half the length of the entire cipher text
    while lengthOfSubstring <= textLen//2:
        for index in range(textLen - lengthOfSubstring):

            substring = cipherText[index: index+lengthOfSubstring]
            if substring not in visited.keys():
                visited[substring] = [index, index+lengthOfSubstring]
            else:
                # only return the subsequence if it doesnt start in the original instance
                # i.e. from ssss it will not return sss, [1,3] if the original sss is [0,2]  
                if index > visited[substring][1]-1:
                    return substring, index

        lengthOfSubstring += 1


    return None, None

	






def main():
    #-----------------------------------------------------/V--------
    plaintext = 'THOSEPOLICEOFFICERSOFFEREDHERARIDEHOMETHEYTELLTHEMAJOKETHOSEBARBERSLENTHERALOTOFMONEY'
    antiPlainText = antiKasiski('WICK', plaintext, 'X')
    if antiPlainText == 'THOSEPOLICEOFFICERSXOFFEREDHERARIDEHOMETHEYTELLXTHEMAJOKETHOSEBARBERSLENXTHERALOTOFMONEY':
        print('Texts Match:')
        print(antiPlainText)
    else:
        print("Texts Do Not Match:")
        print("Created: " + antiPlainText)
        print("Actual : " + 'THOSEPOLICEOFFICERSXOFFEREDHERARIDEHOMETHEYTELLXTHEMAJOKETHOSEBARBERSLENXTHERALOTOFMONEY')
        print("CipherText        :" + vigenere.vigenere('WICK', antiPlainText, 'encrypt'))
        print("Actual Cipher Text:" + vigenere.vigenere('WICK', 'THOSEPOLICEOFFICERSXOFFEREDHERARIDEHOMETHEYTELLXTHEMAJOKETHOSEBARBERSLENXTHERALOTOFMONEY', 'encrypt' ))		

    
    text2 = 'TIMMYTIMMYTIMMYAAAAATIMMY'
    apt = antiKasiski('WICK', text2, 'XYZ')
    print(apt)
    print(vigenere.vigenere('wick', apt, 'encrypt'))

if __name__ == '__main__':
    main()

