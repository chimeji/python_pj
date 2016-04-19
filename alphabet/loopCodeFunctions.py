#from crypt import crypt
from passlib.hash import sha256_crypt as sha256

############
# LoopCode #
############
def loopCode(start, stop, findWord, salt, bases, loopCount, stopEvent):
	loopCount.value = 0
	for i in range(start, stop):
		car1 = bases[0][i]
		for car2 in bases[1]:
			for car3 in bases[2]:
				for car4 in bases[3]:
					for car5 in bases[4]:
						for car6 in bases[5]:
							for car7 in bases[6]:
								for car8 in bases[7]:
									word = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8
									encrypted = sha256.encrypt(word, salt=salt, rounds=5000, implicit_rounds=True)
									current =  str(loopCount.value) + " word : " + word + " encrypt : " + encrypted
									loopCount.value = loopCount.value + 1
									if encrypted == findWord:
										print("Found !!! : " + current)
										stopEvent.set()
									if stopEvent.is_set():
										print(current)
										return

	print("No found : " + current)

###############
# TenLoopCode #
###############
def ten_loop_code(findWord, salt, bases):

	#Nombre d'iteration par boucle: nombre de base / 10
	iterationNb = len(bases[0])//10
	print("Nombre d'iteration par boucle : " + str(iterationNb))

	#Boucle sur les serie de nombre
	start = 0
	stop = start + iterationNb
	while stop < len(bases[0]):
		print("start = " + bases[0][start] + " stop = " + bases[0][stop])
		#loop_code(start, stop, findWord, salt, bases)
		start = stop + 1
		stop = start + iterationNb

	#Last round
	if len(bases[0])%10 != 0:
		stop = len(bases[0])-1
		print("start = " + bases[0][start] + " stop = " + bases[0][stop])
		loop_code(start, stop, findWord, salt, bases)
	return 1


