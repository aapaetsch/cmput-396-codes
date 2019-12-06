
from bob import make_bob, otp_encrypt
import random
import bob

FILTERS="x+"
DIAGONAL="↗↖"
RECTILINEAR="↑→"
ALL=DIAGONAL+RECTILINEAR

def getKey(photons, disposalInstructions, messageLen):
    # this function takes in a list of photons and a list of boolean values for bobs correct filters
    # returns a key of those correct values, trunicating to be 5*lenMessage
    key = []
    
    for i in range(len(photons)):
        #only add a photon to the key if we instructed bob to keep it
        if disposalInstructions[i]:
            key.append(photons[i])

    #only produce a key if it is long enough
    if len(key) >= messageLen*5:
        key = key[:messageLen*5]
    
    else:
        return None    
    
    return key


def validateFilters(photons, filters):
    # This function takes in the photons sent to bob and the filters returned from bob
    # Returns a list of boolean indicating if the correct filter was used
    isValid = []
    correctPhotons = 0
    rectFilter = FILTERS[1]
    diagFilter = FILTERS[0]

    #
    for i in range(len(photons)):
        
        photon = photons[i]
        filt = filters[i]
        if filt != None:

            if ((photon in DIAGONAL) and (filt == diagFilter)) or ((photon in RECTILINEAR) and (filt == rectFilter)):
                isValid.append(True)
                correctPhotons += 1
            else:
                isValid.append(False)

        # This deals with bob not recieving a photon
        else:
            isValid.append(False)
    
    return isValid, correctPhotons


def generatePhotons(messageLen):
    
    # This function takes in a message length and multiplies it by a random
    # key length value between 12 and 13

    randomKeyLen = int(messageLen * (random.randint(10, 12) + random.random()))
    photons = bob.choices(ALL, randomKeyLen)
    return photons


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
    
    #1. Generates a key of length: messageLen * a value between 15 and 31.0
    messageLen = len(message)
    allPhotons = []
    allFilters = []
    correctPhotons = 0

    while correctPhotons < messageLen*5:

        photons = generatePhotons(messageLen)
        #2. 
        bobFilters = bob.quantum_channel(photons)
        
        allFilters += bobFilters
        allPhotons += photons

        #3.
        disposalInstructions, correctPhotons = validateFilters(allPhotons, allFilters)
        
        if correctPhotons >= messageLen*5:

            #4. 
            bob.dispose(disposalInstructions)
            #5. 
            key = getKey(allPhotons, disposalInstructions, messageLen)

    #6. 
    ciphertext = otp_encrypt(key, message)
    bob.message(ciphertext)


def problem2(bob, message):
    """
    If Bob selects the incorrect filter, there is a 10% chance that the photon will be lost
    The length of the list of filters returned by Bob is the number of photons that reached bob successfully
    """


    # This solution is identical to problem 1 as incorrect filters and Nones are both handled in validateFilters

    messageLen = len(message)
    allPhotons = []
    allFilters = []
    correctPhotons = 0
    
    while correctPhotons < messageLen*5:
        
        photons = generatePhotons(messageLen)
        bobFilters = bob.quantum_channel(photons)
        
        allPhotons += photons
        allFilters += bobFilters
        
        disposalInstructions, correctPhotons = validateFilters(allPhotons, allFilters)
        
        if correctPhotons >= messageLen*5:
        
            bob.dispose(disposalInstructions)
            key = getKey(allPhotons, disposalInstructions, messageLen)

    #6. 
    ciphertext = otp_encrypt(key, message)
    bob.message(ciphertext)


def problem3(bob, message):
    """
    Eve may be evesdropping and alter the polarity of photons, but no photons are lost
    """
    # raise NotImplemented("TODO")
    
    messageLen = len(message)
    allPhotons = []
    allFilters = []
    correctPhotons = 0


    while correctPhotons < messageLen*5:

        #Generate a random string of photons
        photons = generatePhotons(messageLen)
        #Generate a list len = len(photons) where bob should show what photon he recieved (I decided on every third photon)
        tellList = generateTell(photons)

        #transmit the photon list and tellList to bob
        bobFilters = bob.quantum_channel(photons, tellList)
        allPhotons += photons
        allFilters += bobFilters

        # Here we check for eve evesdropping
        allPhotons, allFilters = checkForEve(bob, allPhotons, allFilters)
        
        # If we get back Nones, eve is evesdropping and we stop the function as she has been reported
        if allPhotons == None and allFilters == None:
            return 
        
        # If eve is not evesdropping we can get disposal instructions and check if our key is long enough
        disposalInstructions, correctPhotons = validateFilters(allPhotons, allFilters)
        
        # If the key is long enough, tell bob what photons to drop and calculate the key
        if correctPhotons >= messageLen*5:
        
            bob.dispose(disposalInstructions)
            key = getKey(allPhotons, disposalInstructions, messageLen)

    # only send bob the cipher text if eve is not evesdropping
    ciphertext = otp_encrypt(key, message)
    bob.message(ciphertext)


def checkForEve(bob, allPhotons, allFilters):
    # This function takes in the bob object, and the allPhotons list and allFilters list
    # returns fixedPhotons and fixedFilters list only if eve is not evesdropping

    # this is where each filter is stored, for ease of coding 
    rectFilter = FILTERS[1]
    diagFilter = FILTERS[0]

    fixedPhotons = []
    fixedFilters = []

    for i in range(len(allFilters)):

        filt = allFilters[i]
        photon = allPhotons[i]
        # if the photon was not dropped
        if filt != None:
            # we check if the sent photon and the recieved photon are in the same filter group
            if (photon in DIAGONAL) and (filt in DIAGONAL):
                # if they are but are the opposite orientation in a filter group, we know eve is evesdropping
                if DIAGONAL.index(photon) != DIAGONAL.index(filt):
            
                    # report eve and return Nones
                    bob.report_eve()
                    return None, None
            
            #same as above except for the opposite filter group
            elif ((photon in RECTILINEAR) and (filt in RECTILINEAR)):
            
                if RECTILINEAR.index(photon) != RECTILINEAR.index(filt):

                    bob.report_eve()
                    return None, None

            
            elif filt not in DIAGONAL and filt not in RECTILINEAR:
                # If a filter was recieved, bob did not tell us the photon and we can add it to the output lists
                fixedPhotons.append(photon)
                fixedFilters.append(filt)
        
        elif filt == None:
            # cases where tellList == True and filt == None have already been dealt with so we can include Nones here
            fixedPhotons.append(photon)
            fixedFilters.append(filt)

    return fixedPhotons, fixedFilters


def generateTell(photons):
    #Gets every third photon to ask bob.quantum_channel() to report
    tell = []
    
    for i in range(len(photons)):
        
        if i%3 == 0:
            tell.append(True)
        
        else:
            tell.append(False)

    return tell

def cleanFilters(bobFilters, photons, tellList):
    # This function cleans the photon and bobFilter lists 
    # returns both lists with the index's removed 
    # where bob recieved no Photon but where we told bob to show what he recieved
   
    bobFilters = list(bobFilters)
    count = 0 

    for i in range(len(bobFilters)):
        if tellList[i]:
            if bobFilters[i] == None:
                bobFilters[i] = ' '
                photons[i] = ' '
                count += 1

    for i in range(count):
        bobFilters.remove(' ')
        photons.remove(' ')

    return bobFilters, photons

def problem4(bob, message):
    """
    Eve may be evesdropping and alter the polarity of photons
    If Eve uses the wrong filter, there is a 10% that the packet will be lost
    If Bob uses the wrong filter, there is a 10% chance that the photon will be lost
    The length of the list of filters returned by Bob is the number of photons that reached bob successfully
    """
    # raise NotImplemented("TODO")
    messageLen = len(message)
    allPhotons = []
    allFilters = []
    correctPhotons = 0


    while correctPhotons < messageLen*5:

        photons = generatePhotons(messageLen)
        tellList = generateTell(photons)

        bobFilters = bob.quantum_channel(photons, tellList)

        # This is the only difference from problem 3, which deals with Nones in the filter list where
        # The tellList had a True
        bobFilters, photons = cleanFilters(bobFilters, photons, tellList)
        
        allPhotons += photons
        allFilters += bobFilters
        

        allPhotons, allFilters = checkForEve(bob, allPhotons, allFilters)

        if allPhotons == None and allFilters == None:
            return 
        
        disposalInstructions, correctPhotons = validateFilters(allPhotons, allFilters)
        
  
        if correctPhotons >= messageLen*5:
        
            bob.dispose(disposalInstructions)
            key = getKey(allPhotons, disposalInstructions, messageLen)
    
    ciphertext = otp_encrypt(key, message)
    bob.message(ciphertext)

def test():
    
    print("\nTesting Problem 1 :")
    problem1(make_bob(problemNumber=1), "HELLO BOB HOW ARE YOU DOING TODAY")
    print('\tSecond Test:')
    problem1(make_bob(problemNumber=1), "HELLO BOB")
    
    print('\nTesting problem 2 :')
    problem2(make_bob(problemNumber=2), "HELLO BOB HOW ARE YOU DOING TODAY")

    print("\nTesting Problem 3:")
    print("\tTest Using P3 Bob:")
    problem3(make_bob(problemNumber=3), "HELLO BOB HOW ARE YOU DOING TODAY")
    print('\tSecond Test:')
    problem3(make_bob(problemNumber=3), "HELLO BOB")
    print("\tTest Using P1 Bob:")
    problem3(make_bob(problemNumber=1), "HELLO BOB")

    print('\nTesting Problem 4:')
    print('\tTesting Using P4 Bob:')
    problem4(make_bob(problemNumber=4), "HELLO BOB HOW ARE YOU DOING TODAY")
    print('\tTesting Using P2 Bob:')
    problem4(make_bob(problemNumber=2), "HELLO BOB HOW ARE YOU DOING TODAY")
    print('\tTesting Using P1 Bob:')
    problem4(make_bob(problemNumber=1), "HELLO BOB HOW ARE YOU DOING TODAY")
    print('\tTesting using P3 Bob:')
    problem4(make_bob(problemNumber=3), 'HELLO BOB HOW ARE YOU DOING TODAY')
    return

if __name__ == "__main__":
    test()
