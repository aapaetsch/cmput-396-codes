import sys
import random
from a1p1 import encryptMessage
from a1p2 import transpositionDecrypt

def main():

    random.seed(21)
    X = 5 # set the number of tests

    for i in range(X):
        #select a random amount of characters between 4 & 40
        message  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        #convert the message to type list, shuffle the list then return message to type string
        message = random.shuffle( list( message))
        print(message)
        print(type(message))
        message = ''.join( message )
        print(message)







if __name__ == '__main__':
    main()
