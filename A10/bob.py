from random import choice, randint
from operator import itemgetter
from itertools import islice
from string import ascii_uppercase

def choices(items, k):
    """Reimplementation of random.choices to support older versions of Python"""
    ret = []
    for _ in range(k):
        ret.append(choice(items))
    return ret

FILTERS="x+"
DIAGONAL="↗↖"
RECTILINEAR="↑→"
ALL=DIAGONAL+RECTILINEAR

def make_bob(problemNumber):
    def drop_photon_chance():
        return randint(1, 2) == 1
    assert problemNumber in range(1, 5), "Provide a valid problem number Eg. 1, 2, 3, or 4"
    key = tuple()
    # All photons make it to Bob
    def apply_filter0(qfilter, datum):
        correct = {
            "x": DIAGONAL,
            "+": RECTILINEAR,
        }[qfilter]
        return datum if datum in correct else choice(correct)
    # Chance that incorrect guesses are dropped
    def apply_filter1(qfilter, datum):
        correct = {
            "x": DIAGONAL,
            "+": RECTILINEAR,
        }[qfilter]
        if datum not in correct and drop_photon_chance():
            return None
        return datum if datum in correct else choice(correct)
    # All photons are intercepted by Eve and make it to bob
    def apply_filter2(qfilter, datum):
        correctMap = {
            "x": DIAGONAL,
            "+": RECTILINEAR,
        }
        eveFilter = choice(FILTERS)
        correct = correctMap[eveFilter]
        datum = datum if datum in correct else choice(correct)
        correct = correctMap[qfilter]
        return datum if datum in correct else choice(correct)
    # All photons are intercepted and they may be lost
    def apply_filter3(qfilter, datum):
        correctMap = {
            "x": DIAGONAL,
            "+": RECTILINEAR,
        }
        eveFilter = choice(FILTERS)
        correct = correctMap[eveFilter]
        datum = datum if datum in correct else choice(correct)
        if datum not in correct and drop_photon_chance():
            return None
        correct = correctMap[qfilter]
        if datum not in correct and drop_photon_chance():
            return None
        return datum if datum in correct else choice(correct)

    
    apply_filter = {
        0: apply_filter0,
        1: apply_filter1,
        2: apply_filter2,
        3: apply_filter3,
    }[problemNumber - 1]
    class Bob:
        def quantum_channel(self, data, tell=None):
            """
            Simulate transmitting a key over the quantum channel
            bob.quantum_channel(data):
                data: a list of characters (↗, ↖, ↑, or →)
                tell: [optional] a list of booleans (with the same length as data) 
                    Where an index is True, Bob will send one of (↗, ↖, ↑, or →) instead of the filter he used
                    Bob will not store the 
            returns:
                A list of the filters bob used Eg. ["x", "+", "x", "+"]
                The list will have the same length as data unless photons are dropped
            """
            nonlocal key
            assert all(e in set(ALL) for e in data), "Elements in data must be one of '{}'".format(ALL)
            filters = choices(FILTERS, k=len(data))

            new_key = tuple((apply_filter(f, datum) for f, datum in zip(filters, data)))
            # Drop filters where photons were lost
            filters = [f if nk is not None else None for f, nk in zip(filters, new_key)]
            if tell is None:
                key += new_key
                return filters
            assert len(tell) == len(data), "Arguments must be the same length"
            # Dispose of the indices Bob told Alice
            key += tuple(map(itemgetter(0), filter(lambda x: not x[1], zip(new_key, tell))))
            return tuple(keybit if tellbit else filterbit for keybit, filterbit, tellbit in zip(new_key, filters, tell))
        def dispose(self, elements):
            """
            Take a list of booleans, eg. [True, False, True]
            And dispose of data in key where value is False
            bob.dispose(elements)
                elements: a list of bools
            Example:
            before dispose: key == ["↗", "↖"] 
            after dispose: with elements = [True, False]; key == ["↗"]
            """ 
            nonlocal key
            assert all(type(e) is bool for e in elements), "Elements in elements must be one of True or False"
            assert len(elements) == len(key), "The elements argument in 'dispose(elements)' must be the same length as the data bob has stored"
            key = tuple(map(itemgetter(0), filter(itemgetter(1), zip(key, elements))))
        
        def message(self, ciphertext):
            """
            Send Bob the encrypted message
            bob.message(ciphertext)
                ciphertext: a string returned from otp_decrypt
            Returns the message bob got after decrypting with his key
            Bob will only use the first len(ciphertext) * 5 characters of his key

            You can only call message once. You may not call any other methods from after calling 
            bob.message
            """
            neededKeyLength = len(ciphertext) * 5
            message = otp_decrypt(key[:neededKeyLength], ciphertext)
            print("Bob's message: {}".format(message))
            def done_error(*args, **kwargs):
                raise Exception("bob.message() has already been called")
            self.quantum_channel = done_error
            self.dispose = done_error
            self.message = done_error
            self.message = done_error
            return message
        
        def report_eve(self):
            """
            Call this method only when you're positive that your messages have been intercepted
            Your program can end after calling this method
            """
            print("Eve Reported!")
        
        def debug(self):
            """
            Returns the current value of Bob's key
            Do not rely on this function in your final code
            """
            return key


    return Bob()

def otp_key_indices(key):
    keybase2 = (DIAGONAL.index(k) if k in DIAGONAL else RECTILINEAR.index(k) for k in key)
    groupsOf5 = (islice(keybase2, 0, 5) for _ in range(len(key) // 5))
    keyIndices = (sum(d * (2**i) for i, d in enumerate(num)) for num in groupsOf5)
    return keyIndices

def otp_encrypt(key, message):
    """
    Encrypt a message using the one time pad cipher
    otp_encrypt(key, message)
        key: a string containing only ↗, ↖, ↑, or →. 5 times the length of message
        message: A string to encrypt contains only uppercase letters and space
    returns: encrypted ciphertext
    """
    CIPHER_ALPHABET = ascii_uppercase + " *&^%$"
    assert len(CIPHER_ALPHABET) == 32
    assert len(key) == len(message) * 5, "Key must be 5 times the length of message"
    assert all(k in set(ALL) for k in key), "Key may only contain ↗, ↖, ↑, or →"
    assert all(c.isupper() or c == " " for c in message), "Message can only contain uppercase letters and space"

    indices = otp_key_indices(key)
    return ''.join(CIPHER_ALPHABET[(index + CIPHER_ALPHABET.index(plain)) % 32] for index, plain in zip(indices, message))


def otp_decrypt(key, message):
    """
    Decrypt a message using the one time pad cipher
    otp_encrypt(key, ciphertext)
        key: a string containing only ↗, ↖, ↑, or →. 5 times the length of message
        ciphertext: A string to decrypt contains only uppercase letters and space
    returns: decrypted plaintext
    """
    CIPHER_ALPHABET = ascii_uppercase + " *&^%$"
    assert len(CIPHER_ALPHABET) == 32
    assert len(key) == len(message) * 5, "Key must be 5 times the length of message"
    assert all(k in set(ALL) for k in key), "Key may only contain ↗, ↖, ↑, or →"
    assert all(c in CIPHER_ALPHABET for c in message), "Invalid ciphertext"

    indices = otp_key_indices(key)
    return ''.join(CIPHER_ALPHABET[(CIPHER_ALPHABET.index(plain) - index + 32) % 32] for index, plain in zip(indices, message))
