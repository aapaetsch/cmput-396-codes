import sys
import random
import a1p1
import a1p2

def main():

    random.seed(21)
    X = 5 # set the number of tests

    for i in range(X):
        
        #select a random amount of characters between 4 & 40
        message  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        
        #convert the message to type list, shuffle the list then return message to type string
        messageList = list(message)
        random.shuffle(messageList)
        message = ''.join( messageList )
        
        keys = [[1,3,5,7,9,2,4,6,8], [1,3,4,2]]
        print( "Test #%s: %s..." %(i+1, message[:50]))

        for k in range(len(keys)):
            
            print('k1: ',keys[k])            
            encrypted = a1p1.messageEncrypting(keys[k], message)
            print('k2: ',keys[k])
            decrypted = a1p2.messageDecrypting(keys[k], encrypted)
            
            if message != decrypted:
                print('Mismatch with key %s and message %s.'%(keys[k], message))
                print('Decrypted as: ' + decrypted)
                sys.exit()
    
    print('All Tests Passed')






if __name__ == '__main__':
    main()
