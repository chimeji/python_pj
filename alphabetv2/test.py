count = 0

lentab1 = 5
lentab2 = 7
lentab3 = 4
bases = ['abdce', '1234567', '$;,:', 'ABCDE']
baseNumber = []

nbComb = 1
for base in bases:
	nbComb = nbComb * len(base)	

def getDigitDebug(number, position, baseNumbers):
	digit = number
	print("digit={}".format(number))
	for i in range(len(baseNumbers)-1, position, -1):
		digit = digit%baseNumbers[i] 
		print("digit%{}={}".format((baseNumbers[i]),digit))
	digit = digit//baseNumbers[position]	
	print("digit//{}={}\n".format(baseNumbers[position],digit))
	return digit


def getDigit(number, position, baseNumbers):
	digit = number
	for i in range(len(baseNumbers)-1, position, -1):
		digit = digit%baseNumbers[i] 
	digit = digit//baseNumbers[position]	
	return digit


#Calcul de la baseNumber
currentBaseNumber  = 1
baseNumber.append(currentBaseNumber)
for i in range(len(bases)-1,-1,-1):
	currentBaseNumber = currentBaseNumber * len(bases[i])
	baseNumber.append(currentBaseNumber)


for nb in range(1,nbComb):
	i = nb//baseNumber[3]
	j = nb%baseNumber[3]//baseNumber[2]
	k = nb%baseNumber[3]%baseNumber[2]//baseNumber[1]
	l = nb%baseNumber[3]%baseNumber[2]%baseNumber[1]//baseNumber[0]
	 

	#print("{} [{} {} {} {}] = ".format(nb,i,j,k,l) + bases[0][i] + bases[1][j] + bases[2][k] + bases[3][l])

for nb in range(0,nbComb):
	i = getDigit(nb, 3, baseNumber)
	j = getDigit(nb, 2, baseNumber)
	k = getDigit(nb, 1, baseNumber)
	l = getDigit(nb, 0, baseNumber)

	print("{} [{} {} {} {}] = ".format(nb,i,j,k,l) + bases[0][i] + bases[1][j] + bases[2][k] + bases[3][l])

#Test digit
print()
nb = 690
i = getDigit(nb, 3, baseNumber)
j = getDigit(nb, 2, baseNumber)
k = getDigit(nb, 1, baseNumber)
l = getDigit(nb, 0, baseNumber)
print ("{} [{} {} {} {}]".format(nb, i,j,k,l))


	
	
print(baseNumber)
