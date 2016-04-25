from crypt import crypt
import multiprocessing
#from passlib.hash import sha256_crypt as sha256

############
# LoopCode #
############
def loopCode(start, stop, findWord, salt, bases, loopCount, stopEvent):
	loopCount.value = 0
	for i in range(start, stop):
		car1 = bases[0][i]
		print("LOOPCODE  - bases[0][" + str(i) + "] = " + str(bases[0][i]) + " started")
		for car2 in bases[1]:
			for car3 in bases[2]:
				for car4 in bases[3]:
					for car5 in bases[4]:
						for car6 in bases[5]:
							for car7 in bases[6]:
								for car8 in bases[7]:
									word = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8
									#encrypted = sha256.encrypt(word, salt=salt, rounds=5000, implicit_rounds=True)
									encrypted = crypt(word, salt)
									current =  str(loopCount.value) + " word : " + word + " encrypt : " + encrypted
									loopCount.value = loopCount.value + 1
									#print(current)
									if encrypted == findWord:
										print("LOOPCODE  - Found !!! : " + current)
										stopEvent.set()
										return
									if stopEvent.is_set():
										print("LOOPCODE  - Stopped : " + current)
										return

	print("LOOPCODE - Finished : " + current)

#################
# MultiLoopCode #
#################
def multiLoopCode(findWord, salt, bases, loopCountTab, stopEvent):

	#Nombre d'iteration par boucle: nombre de base / nombre de loopCode voulu
	loopCodeNb = len(loopCountTab)
	iterationNb = len(bases[0])//loopCodeNb
	print("MULTILOOP - Number of loopCode oject : " + str(loopCodeNb + 1))
	print("MULTILOOP - Iteration per loopCode : " + str(iterationNb + 1))

	
	#Boucle les serie de nombre
	loopI = 0 
	start = 0
	stop = start + iterationNb
	while stop < len(bases[0]):
		print("MULTILOOP - Iteration " + str(loopI) + " [" + bases[0][start] + "  " + bases[0][stop] + "] started")
		p = multiprocessing.Process(target=loopCode, args=(start, stop, findWord, salt, bases, loopCountTab[loopI], stopEvent))
		p.start()

		start = stop + 1
		stop = start + iterationNb
		loopI = loopI + 1

	#Last round
	if len(bases[0])%10 != 0:
		stop = len(bases[0])-1
		print("MULTILOOP - Iteration " + str(loopI) + " [" + bases[0][start] + "  " + bases[0][stop] + "] started")
		p = multiprocessing.Process(target=loopCode, args=(start, stop, findWord, salt, bases, loopCountTab[loopI], stopEvent))
		p.start()
	return


