
import publicKeyCipher as pkc

import hackRSA




def main():

	# N, E	
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




	pass


if __name__ == '__main__':
	main()

