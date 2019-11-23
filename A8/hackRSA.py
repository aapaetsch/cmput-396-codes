import cryptomath
import primeNum
import os
import sys
import publicKeyCipher as pkc


# t = threshold, assume no primes larger than this
# n, e = public RSA key

def finitePrimeHack(t, n, e):
    #this function finds p, q, d for a given public key set

    primeFactors = []
    
    # Factor n and append the factor to primeFactors if the number is prime
    for i in range(1, n + 1):
        
        if i > t:
            break

        if n % i == 0:
            if primeNum.isPrime(i):
                primeFactors.append(i)

    # p should already be < q, this is done as a quick check
    p,q = getpq(primeFactors)
    
    #Finding d
    r = (p-1) * (q-1)
    # getting the modular inverse
    d = cryptomath.findModInverse(e, r)

    return [p, q, d]


def getpq(primeFactors):
    # This function gets p and q from the prime factors list, p <= q
    if primeFactors[0] <= primeFactors[1]:
        p = primeFactors[0]
        q = primeFactors[1]
    
    else:
        p = primeFactors[1]
        q = primeFactors[0]
    
    return p,q




def blockSizeHack(block, n, e):
    # This function decrypts the message from the given blocks, as well as the public key
    # block size is 1
    
    primeFactors = []
    
    blockSize = 1
    messageLength = len(block)

    #Finding the prime factors of n 
    for i in range(1, n + 1):

        if n % i == 0 :
            if primeNum.isPrime(i):

                primeFactors.append(i)

        #since n is semiprime, there are no composite numbers as factors other than itself. once we find the first 2 prime factors we can break 
        if len(primeFactors) >= 2:
            break

    p, q = getpq(primeFactors)


    r = (p-1) * (q-1)
    d = cryptomath.findModInverse(e, r)

    # use the decryptmessage from publicKeyCipher.py to figure out the message
    decryptedMessage = pkc.decryptMessage(block, messageLength, (n,d), blockSize)

    return decryptedMessage






 





    

#<-------------------- For testing ------------->
def main():
    
    print("Testing Finite Prime Hack:")
    finitePrimeTest1 = finitePrimeHack(100, 493, 5)
    print("\nTest 1:")
    testFinitePrimeHack(finitePrimeTest1, [17, 29, 269])
            

    print("\nTest 2:")
    finitePrimeTest2 = finitePrimeHack(300,221, 5)
    testFinitePrimeHack(finitePrimeTest2, [13, 17, 77])

    test_a8_pubkeys()

    print("\nTesting Block Size Hack")
    blocks = [2361958428825, 564784031984, 693733403745, 693733403745, 2246930915779, 1969885380643]    
    n = 3328101456763
    e = 1827871
    blockSizeHackTest1 = blockSizeHack(blocks, n, e)
    if blockSizeHackTest1 == 'Hello.':
        print('Test 1 passed')
    else: 
        print('Test 1 Failed:',blockSizeHackTest1, 'returned instead of Hello')
    print(blockSizeHackTest1)
    testBlockHack()

def testBlockHack():
    test1 = 'Bawdy feat. Big Freedia'
    test2 = 'abcdefghijklmnopqrstuvwxyz1234567890.!ABCDZHSKHFLKJAHSLKJFS'
    keys = [[617723468413, 913289], [461749934963, 888499],[752347391021, 831701] , [703025612207, 1008121], [493, 5], [221, 5]]
    test = [test1, test2]
    count = 1
    for testPhrase in test:
        print("Testing:", testPhrase)
        for key in keys:
            blocks = pkc.encryptMessage(testPhrase, key, 1)
            n = key[0]
            e = key[1]
            decryptedMessage = blockSizeHack(blocks, n, e)
            print('\tTesting key:', count)
            if decryptedMessage == testPhrase:
                print('\tDecryption Passed')
            else:
                print('\tDecryption Failed')
            count +=1
            print()
        count = 1



def testFinitePrimeHack(calculated, expected):
    isCorrect = True
    if calculated[0] != expected[0]:
        isCorrect = False
        print("\tP value Incorrect:", calculated[0])
    if calculated[1] != expected[1]:
        isCorrect = False
        print("\tQ value Incorrect:", calculated[1])
    if calculated[2] != expected[2]:
        print('\tD value Incorrect:', calculated[2])
        isCorrect = False
    if isCorrect:
        print("\tPassed!")

def test_a8_pubkeys():
    files = os.listdir('a8_pubkeys')

    for file in files:
        with open('a8_pubkeys/' + file) as f:
            for pubkey in f:
                print('\nTesting ' + file + ":")
                pubkey = pubkey.split(',')
                pubkey[0] = int(pubkey[0])
                pubkey[1] = int(pubkey[1])
                pubkey[2] = int(pubkey[2])
                
                finitePrimeTest = finitePrimeHack(2**pubkey[0], pubkey[1], pubkey[2])
                print('\t[p,q,d]:',finitePrimeTest)


if __name__ == '__main__':
    main()
