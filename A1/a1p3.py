import sys
import random
import a1p1
import a1p2
import itertools
def main():

    random.seed(21)
    X = 3 #set the number of tests

    for i in range(X):
        
        #select a random amount of characters between 4 & 40
        #message  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        messages = ["CIPHERS ARE FUN", "ABCDEFG", 'EXCELLENT WORK YOU HAVE CRACKED THE CODE']
        #convert the message to type list, shuffle the list then return message to type string
        message = messages[i]
        messageList = list(message)
        random.shuffle(messageList)
        message = ''.join( messageList )
        
        keys = [[1,2]]
        key = [1,2]
        for keyLen in range(3, int(len(message)/2)):
            key.append(keyLen)
            keys.append(key.copy())
            
        print( "Test #%s: %s..." %(i+1, message[:50]))
        jj = 0 #test content
        for k in keys:
            
            permutations = list(itertools.permutations(k))
            random.shuffle(permutations)
            
            while len(permutations) < 5:
                permutations.append(permutations[random.randint(0, len(k))])
            
            pp = 0
            for p in permutations:
                pp += 1
                print(i,":",jj,':',pp,":",p)
                myKey = list(p)
                encrypted = a1p1.messageEncrypting(myKey, message)
                decrypted = a1p2.messageDecrypting(myKey, encrypted)
            
                if message != decrypted:
                    print('Mismatch with key %s and message %s.'%(myKey, message))
                    print("Encrypted as: " + encrypted)
                    print('Decrypted as: ' + decrypted)
                    sys.exit()
                if pp == 5:
                    break
            jj += 1
    print('All Tests Passed')






if __name__ == '__main__':
    main()
