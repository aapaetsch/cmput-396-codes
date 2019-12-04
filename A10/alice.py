
from bob import make_bob, otp_encrypt
import random
import bob

FILTERS="x+"
DIAGONAL="↗↖"
RECTILINEAR="↑→"
ALL=DIAGONAL+RECTILINEAR

def problem1(bob, message):
    """
    An example of quantum key exchange and OTP message sending
    All photons arrive at bob and there is no eavesdropping on the line
    """
    """
    1.  Generate a sufficiently large random key; the key must be at least 5
        times the length of the message and on average half of bobs guess
        filters will be wrong
    2.  Get the filters bob used by using bob.quantum_channel(data)
    3.  Create the list of correct filters sent and figure out which filters
        Bob used correctly
    4.  Tell Bob which filters he guessed incorrectly and should remove
    5.  Create the key and to make sure it's >= 5*len(message) and shorten the
        key to 5*len(message) if it is currently longer
    6.  Call otp_encrypt(key, message) to encrypt the message and then use
        bob.message(ciphertext) to send Bob the coded message
    """
    # raise NotImplemented("TODO")

    #1. Generates a key of length: messageLen * a value between 11 and 21.0
    messageLen = len(message)
    photons = generateKey(messageLen)
    
    #2. 
    bobFilters = bob.quantum_channel(photons)

    #3.
    disposalInstructions = validateFilters(photons, bobFilters)
    
    #4. 
    bob.dispose(disposalInstructions)

    #5. 
    


def validateFilters(photons, filters):
    # This function takes in the photons sent to bob and the filters returned from bob
    # Returns a list of boolean indicating if the correct filter was used
    diag = DIAGONAL + "x"
    rect = RECTILINEAR + "+"
    isValid = []
    
    for i in range(len(photons)):
        
        photon = photons[i]
        filt = filters[i]
        
        if ((photon in diag) and (filt in diag)) or ((photon in rect) and (filt in rect)):
            isValid.append(True)
        
        else:
            isValid.append(False)
    
    return isValid







def generateKey(messageLen):
    # This function takes in a message length and multiplies it by a random
    # key length value between 11 and 21.0
    randomKeyLen = int(messageLen * (random.randint(11,20) + random.random()))
    photons = bob.choices(ALL, randomKeyLen)
    return photons


def problem2(bob, message):
    """
    If Bob selects the incorrect filter, there is a 10% chance that the photon will be lost
    The length of the list of filters returned by Bob is the number of photons that reached bob successfully
    """
    raise NotImplemented("TODO")


def problem3(bob, message):
    """
    Eve may be evesdropping and alter the polarity of photons, but no photons are lost
    """
    raise NotImplemented("TODO")


def problem4(bob, message):
    """
    Eve may be evesdropping and alter the polarity of photons
    If Eve uses the wrong filter, there is a 10% that the packet will be lost
    If Bob uses the wrong filter, there is a 10% chance that the photon will be lost
    The length of the list of filters returned by Bob is the number of photons that reached bob successfully
    """
    raise NotImplemented("TODO")

def test():
    problem1(make_bob(problemNumber=1), "HELLO BOB HOW ARE YOU DOING TODAY")
    # problem2(make_bob(problemNumber=2), "HELLO BOB HOW ARE YOU DOING TODAY")
    # problem3(make_bob(problemNumber=3), "HELLO BOB HOW ARE YOU DOING TODAY")
    # problem4(make_bob(problemNumber=4), "HELLO BOB HOW ARE YOU DOING TODAY")
    return

if __name__ == "__main__":
    test()
