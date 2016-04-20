#from crypt import crypt
import loopCodeFunctions
import multiprocessing
import time

if __name__ == '__main__':
	################
	# PARAMETERS   #
	################
	#Timeout
	timeout = 10

	#Bases
	majuscule = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	minuscule = 'abcdefghijklmnopqrstuvwxyz'
	symbole = '!'
	chiffre = '0123456789'

	################
	# MAIN PROGRAM #
	################

	#Encryption parameters
	tabBase = [majuscule, minuscule, minuscule, minuscule, symbole, chiffre, chiffre, chiffre]
	mySalt = 'KS'
	searchWord='KSIdqhF5l6N2s'

	#Show estimation
	nbComb = 1
	for base in tabBase:
		nbComb = nbComb * len(base)
	print("Number of combination " +  str(nbComb))
	print("Timeout : " +  str(timeout))


	nbLoops = [multiprocessing.Value('i',0) for i in range(1,40)] 
	processList = []
	stopEvent = multiprocessing.Event()

	for nbLoop in nbLoops:
		p = multiprocessing.Process(target=loopCodeFunctions.loopCode, args=(0, 3, searchWord, mySalt, tabBase, nbLoop, stopEvent))
		p.start()
		processList.append(p)
		

	time.sleep(timeout)
	
	stopEvent.set()

	total = 0
	for nbLoop in nbLoops:
		total = total + nbLoop.value
	print("Number of loops in " + str(timeout) + " secs : " + str(total))
	estimatedSec = nbComb // (total//timeout)
	estimatedMin = estimatedSec//60
	estimatedHour = estimatedMin//60
	print("Estimated Min : " + str(estimatedMin))
	print("Estimated Hour : " + str(estimatedHour))






