# Cryptomath Module from 
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# My equation for finding A Is adapted from affine.py "decrypt"
import cryptomath

#---call this function for the [A,B] list ---
def crack_lcg(m, r1, r2, r3):
    
    x = r3 - r2
    y = r2 - r1

    #Finding A
    modInverse = cryptomath.findModInverse(y, m)
    if modInverse != None:
    	A = x * modInverse % m
    	#Finding B, isolated b from the equation of (R1 * A + B) % m = R2
    	B = r2 - r1 * A % m

    # If there is no valid modular inversion
    else:
    	#Either there are multiple solutions or no solutions, either way we return [0,0]
    	A = 0
    	B = 0

    return [A, B]


#----This section below is for testing purposes --- 
def main():

	firstTest = crack_lcg(16, 2, 11, 8)
	print('First Test',firstTest)

	secondTest = crack_lcg(2**32, 953210035, 3724055312, 1961185873)
	if secondTest[0] == 22695477:
		if secondTest[1] == 1:
			print('Second Test', secondTest, ' Both a and B match')
		else:
			print('Second Test', secondTest, 'Only A matches the answer')
	else:
		print('Second Test', secondTest, 'No Match')

	thirdTest = crack_lcg(21, 12, 0, 6)
	print('Third Test', thirdTest, ' For values resulting in multiple correct keys')

	fourthTest = crack_lcg(15, 11, 13, 14)
	print('Fourth Test', fourthTest, ' For values resulting in B = 0, A != 0')

if __name__ == "__main__":
    main()
