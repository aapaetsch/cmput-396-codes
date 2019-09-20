import sys
import random
import a1p1
import a1p2
import itertools
def main():

    random.seed(21)
    X = 5 #set the number of tests

    for i in range(X):
        
        #select a random amount of characters between 4 & 40
        message  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
       
        #convert the message to type list, shuffle the list then return message to type string
        
        messageList = list(message)
        random.shuffle(messageList)
        message = ''.join( messageList )
        
        keys = []
        key = []
        for keyLen in range(1, int(len(message)/2)):
            key.append(keyLen)
            
            keys.append(key.copy())
            
        print( "Test #%s: %s..." %(i+1, message[:50]))
        for k in keys:
            if k == [1,2]:
                permutations = [[1,2],[2,1]]
                for i in range(3):
                    permutations.append(random.choice(permutations))
            elif k == [1]:
                permutations = [[1] for i in range(5)]
            elif len(k) < 5 and k != [1,2]: 
            
                permutations = list(itertools.permutations(k))
                random.shuffle(permutations)
           
            else:
                permutations = []
                while len(permutations) < 5:
                    keyChoice = k.copy()
                    random.shuffle(keyChoice)
                    if keyChoice not in permutations:
                        permutations.append(keyChoice)
            
            permutations = permutations[:5]
            for p in permutations:
                print('    Testing Key: ' +str(p))
                myKey = list(p)
                encrypted = a1p1.encryptMessage(myKey, message)
                decrypted = a1p2.decryptMessage(myKey, encrypted)
            
                if message != decrypted:
                    print('Mismatch with key %s and message %s.'%(myKey, message))
                    print("Encrypted as: " + encrypted)
                    print('Decrypted as: ' + decrypted)
                    sys.exit()
                
    print('All Tests Passed')






if __name__ == '__main__':
    main()
