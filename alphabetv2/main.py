import loopCodeFunctions as lcf
import multiprocessing
import time

if __name__ == '__main__':
	################
	# PARAMETERS   #
	################
	#Timeout
	timeout = 100
 

	#Bases
	majuscule = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	minuscule = 'abcdefghijklmnopqrstuvwxyz'
	symbole = '!,;:$'
	chiffre = '0123456789'
	all = majuscule + minuscule + symbole + chiffre

	################
	# MAIN PROGRAM #
	################

	#Encryption parameters
	bases = [majuscule, minuscule, minuscule, minuscule, symbole, chiffre, chiffre, chiffre]
	bases = [majuscule, minuscule, minuscule, symbole, chiffre, chiffre, chiffre, chiffre]
	bases = [all,all,all,all,all,all,all,all]
	salt = 'zj'
	findWord='zjE4k2Ky3/gug'

	#Show estimation
	nbComb = 1
	for base in bases:
		nbComb = nbComb * len(base)
	print("Number of combination " +  str(nbComb))
	print("Timeout : " +  str(timeout))


	#Start multiLoopCode
	loopCodeNb = 20 
	loopCountTab = [multiprocessing.Value('i',0) for i in range(0,loopCodeNb)] 

	stopEvent = multiprocessing.Event()
	processTab = []
	lcf.multiLoopCode(findWord, salt, bases, loopCountTab, processTab, stopEvent)
	
	
	#Wait 10 sec
	time.sleep(timeout)
	
	#Stop multiLoopCode
	#stopEvent.set()


	#Wait until all process finish
	for p in processTab:
		p.join()

	#Print estimation
	total = 0 
	for nbLoop in loopCountTab:
		total = total + nbLoop.value
	print("Number of combination " +  str(nbComb))
	print("Timeout : " +  str(timeout))
	print("Number of loops in " + str(timeout) + " secs : " + str(total))
	estimatedSec = nbComb // (total//timeout)
	estimatedMin = estimatedSec//60
	estimatedHour = estimatedMin//60
	print("Estimated Min : " + str(estimatedMin))
	print("Estimated Hour : " + str(estimatedHour))





