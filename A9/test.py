import a9p3
import a9p1
import a9p2
import a9p5
ciphertext = "VE AYO Y FGVUQE INXK KYC VP YMGVX"

# mapping1 = {'V': 'E', 'Y': 'T', 'E': 'A', 'G': 'O', 'X': 'I', 'K': 'N', 'A': 'R', 'O': 'S', 'F': 'F', 'U': 'U', 'Q': 'M', 'I': 'W', 'N': 'L', 'C': 'H', 'P': 'D', 'M': 'C'}
# mapping2 = {'V': 'R', 'Y': 'T', 'E': 'E', 'G': 'O', 'X': 'I', 'K': 'N', 'A': 'A', 'O': 'H', 'F': 'F', 'U': 'U', 'Q': 'M', 'I': 'W', 'N': 'L', 'C': 'S', 'P': 'D', 'M': 'C'}
mapping1 = {'V': 'E', 'Y': 'T', 'E': 'A', 'G': 'O', 'X': 'I', 'K': 'N', 'A': 'R', 'O': 'S', 'F': 'F', 'U': 'U', 'Q': 'M', 'I': 'W', 'N': 'L', 'C': 'H', 'P': 'D', 'M': 'C'}
mapping2 = {'U': 'C', 'I': 'M', 'N': 'U', 'K': 'O', 'V': 'E', 'O': 'R', 'Q': 'L', 'C': 'H', 'G': 'A', 'P': 'D', 'F': 'W', 'E': 'I', 'X': 'N', 'M': 'S', 'A': 'F', 'Y': 'T'}
plaintext = ''
with open('text_for_eng_freq.txt','r') as f:
	for line in f:
		plaintext+= line
plaintext = a9p1.cleanText(plaintext)

freq  = a9p1.ngramsFreqs(plaintext, 1)
score1 = a9p2.keyScore(mapping1, ciphertext, freq, 1)
score2 = a9p2.keyScore(mapping2, ciphertext, freq, 1)

print("Score from mine:",score1)
print("Score from example:", score2)


plaintext = 'IT WAS A BRIGHT COLD DAY IN APRIL'
a0 = 'EA STH T ROEDLA CUIN NTM EW TFOEI'
a1 = 'RE ATH T FORUME WLIN NTS RD TCORI'
a2 = 'OD ITM T WEOAND CLUS STR OF THEOU'
a3 = 'NF ITO T MENCLF UWAS STR ND THENA'
a4 = 'ON ATM T WEODLN CURI ITS OF THEOR'
a5 = 'AT HEL E ROADWT CUIM MEN AS EFOAI'
a6 = 'CN AEU E RMCDON THIS SEL CW EFMCI'
a7 = 'EA STH T ROEDLA CUIN NTM EW TFOEI'
a8 = 'EA STH T ROEDLA CUIN NTM EW TFOEI'


print(a9p5.getDecipherAcc(a0,plaintext))
print(a9p5.getDecipherAcc(a1,plaintext))
print(a9p5.getDecipherAcc(a2,plaintext))
print(a9p5.getDecipherAcc(a3,plaintext))
print(a9p5.getDecipherAcc(a4,plaintext))
print(a9p5.getDecipherAcc(a5,plaintext))
print(a9p5.getDecipherAcc(a6,plaintext))
print(a9p5.getDecipherAcc(a7,plaintext))
print(a9p5.getDecipherAcc(a8,plaintext))