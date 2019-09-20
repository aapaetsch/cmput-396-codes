# Transposition Cipher filecipher
# Adapted from https://www.nostarch.com/crackingcodes (BSD Licensed)
import time
import os
import sys
import a1p1
import a1p2

def main():
    #strings for the input and output text
    inputFile = 'mystery.txt'
    outputFile = 'mystery.dec.txt'
    #do we want to encrypt or decrypt the file
    mode = 'decrypt'
    
    #set the key for encryption/decryption here
    key = [2,4,6,8,10,1,3,5,7,9]
    
    #quit if the input file does not exist
    if not os.path.exists(inputFile):
        print('The file %s does not exist, quitting...' %(inputFile))
        sys.exit()
    #if the output file is going to be overwritten, ask if this is ok
    if os.path.exists(outputFile):
        print("This will overwrite output file %s, is that ok? (y)es or (n)o" %(outputFile))
        response = input('> ')
        #quit if its not ok to overwrite
        if response.lower()[0]=='n':
            print('Quitting..')
            sys.exit()
    
    
    startTime = time.time()     
    #open the file and get the content
    with open(inputFile, 'r') as f:
        content = f.read()
    #this is the mode we will use for this assignment
    if mode == 'decrypt':
        modifiedText = a1p2.decryptMessage(key, content)
    
    #only kept this in to keep it close to the textbook material
    elif mode == 'encrypt':
        modifiedText = a1p1.encryptMessage(key, content)
    
    else:
        print("Invalid mode selected, quitting...")
        sys.exit()
    
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' %(mode.title(), totalTime))
    
    #write the modified text to the indicated output file
    with open(outputFile, 'w') as f:
        f.write(modifiedText)
    
    print('Done %sing %s (%s characters).' %(mode, inputFile, len(content)))
    print('%sed file is %s.' %(mode.title(), outputFile))
    


if __name__ == '__main__':
    main()