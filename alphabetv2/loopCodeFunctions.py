from crypt import crypt
import multiprocessing
#from passlib.hash import sha256_crypt as sha256

############
# LoopCode #
############
def loopCode(start, stop, findWord, salt, bases, baseNumbers, loopCount, stopEvent):
	nb = start
	print("LOOPCODE - START [{}, {}] ".format(start, stop))
	while nb < stop:
		d8 = nb//baseNumbers[7]
		d7 = nb%baseNumbers[7]//baseNumbers[6]
		d6 = nb%baseNumbers[7]%baseNumbers[6]//baseNumbers[5]
		d5 = nb%baseNumbers[7]%baseNumbers[6]%baseNumbers[5]//baseNumbers[4]
		d4 = nb%baseNumbers[7]%baseNumbers[6]%baseNumbers[5]%baseNumbers[4]//baseNumbers[3]
		d3 = nb%baseNumbers[7]%baseNumbers[6]%baseNumbers[5]%baseNumbers[4]%baseNumbers[3]//baseNumbers[2]
		d2 = nb%baseNumbers[7]%baseNumbers[6]%baseNumbers[5]%baseNumbers[4]%baseNumbers[3]%baseNumbers[2]//baseNumbers[1]
		d1 = nb%baseNumbers[7]%baseNumbers[6]%baseNumbers[5]%baseNumbers[4]%baseNumbers[3]%baseNumbers[2]%baseNumbers[1]//baseNumbers[0]
		word = bases[0][d8] + bases[1][d7] + bases[2][d6] + bases[3][d5] + bases[4][d4] + bases[5][d3] + bases[6][d2] + bases[7][d1]
		nb = nb + 1

		#Encrypt word
		#encrypted = sha256.encrypt(word, salt=salt, rounds=5000, implicit_rounds=True)
		encrypted = crypt(word, salt)
		current =  str(nb)  + " : " + word + "  ---->  " + encrypted
		#print(current)
	
		#print("{} [{} {} {} {} {} {} {} {}] = ".format(nb,d8,d7,d6,d5,d4,d3,d2,d1) + bases[0][d8] + bases[1][d7] + bases[2][d6] + bases[3][d5] + bases[4][d4] + bases[5][d3] + bases[6][d2] + bases[7][d1])

		#Test word
		if encrypted == findWord:
			print("LOOPCODE  - FOUND !!! : " + current)
			loopCount.value = nb - start + 1
			stopEvent.set()
			return

		#Kill loop
		if stopEvent.is_set():
			print("LOOPCODE  - KILLED : " + current)
			loopCount.value = nb - start + 1
			return
	
	#Loop finished without finding target
	print("LOOPCODE - FINISHED : " + current)
	loopCount.value = nb - start + 1
	return

#################
# MultiLoopCode #
#################
def multiLoopCode(findWord, salt, bases, loopCountTab, processTab, stopEvent):

	baseNumbers = [] 

	#Number of combination
	nbComb = 1
	for base in bases:
		nbComb = nbComb * len(base)	

	#Calcul de la baseNumber
	currentBaseNumber  = 1
	baseNumbers.append(currentBaseNumber)
	for i in range(len(bases)-1,-1,-1):
		currentBaseNumber = currentBaseNumber * len(bases[i])
		baseNumbers.append(currentBaseNumber)
	print(bases)
	print(baseNumbers)

	stop = nbComb

	iterationByLoop = nbComb // len(loopCountTab)
	
	start = 0	
	stop = 0 
	for i in range(len(loopCountTab) - 1):
		stop = stop + iterationByLoop
		p = multiprocessing.Process(target=loopCode, args=(start, stop, findWord, salt, bases, baseNumbers, loopCountTab[i], stopEvent))
		p.start()
		processTab.append(p)
		start = stop + 1


	#Last loop
	stop = nbComb
	p = multiprocessing.Process(target=loopCode, args=(start, stop, findWord, salt, bases, baseNumbers, loopCountTab[i], stopEvent))
	p.start()
	processTab.append(p)
	return


