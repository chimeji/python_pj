#from crypt import crypt
import loopCodeFunctions as lcf
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
	test = 'ABcde'

	################
	# MAIN PROGRAM #
	################

	#Encryption parameters
	bases = [majuscule, minuscule, minuscule, minuscule, symbole, chiffre, chiffre, chiffre]
	#bases = [test, test, test, test, test, test, test, test]
	salt = 'KS'
	findWord='KSIdqhF5l6N2s'

	#Show estimation
	nbComb = 1
	for base in bases:
		nbComb = nbComb * len(base)
	print("Number of combination " +  str(nbComb))
	print("Timeout : " +  str(timeout))


	#Start multiLoopCode
	loopCodeNb = 10
	loopCountTab = [multiprocessing.Value('i',0) for i in range(0,loopCodeNb)] 

	stopEvent = multiprocessing.Event()
	lcf.multiLoopCode(findWord, salt, bases, loopCountTab, stopEvent)
	
	#Wait 10 sec
	time.sleep(timeout)
	
	#Stop multiLoopCode
	stopEvent.set()

	#Print estimation
	total = 0 
	for nbLoop in loopCountTab:
		total = total + nbLoop.value
	print("Number of loops in " + str(timeout) + " secs : " + str(total))
	estimatedSec = nbComb // (total//timeout)
	estimatedMin = estimatedSec//60
	estimatedHour = estimatedMin//60
	print("Estimated Min : " + str(estimatedMin))
	print("Estimated Hour : " + str(estimatedHour))





