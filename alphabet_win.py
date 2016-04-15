#from crypt import crypt
from passlib.hash import sha256_crypt as sha256
import time

#Bases
majuscule = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
majLen = len(majuscule)

minuscule = 'abcdefghijklmnopqrstuvwxyz'
minLen = len(minuscule)

symbole = '!'
symLen = len(symbole)

chiffre = '0123456789'
chiLen = len(chiffre)

#Password
passlen = 8
mySalt = 'KS'
searchWord='KSIdqhF5l6N2s'

############
# loopCode #
############
def loop_code(start, stop, findWord, salt, bases):
	loopCount = 0
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
									password = sha256.encrypt(word, salt=mySalt, rounds=5000, implicit_rounds=True)
									print (str(loopCount) + " word : " + word + " password : " + password)
									loopCount = loopCount + 1


def ten_loop_code(findWord, salt, bases):
	#Nombre d'iteration par boucle: nombre de base / 10
	iteration = len(bases[0])//10
	print("Nombre d'iteration par boucle : " + iteration)
	for i in range (1,10):
		start = 
	loop_code(start, stop, findWord, salt, bases)
	return 1

################
# MAIN PROGRAM #
################
tabBase = [majuscule, minuscule, minuscule, minuscule, symbole, chiffre, chiffre, chiffre]

ten_loop_code(0, 5, searchWord, mySalt, tabBase)
#Cryptage
#passWord = sha256.encrypt(wordI, salt=mySalt, rounds=5000, implicit_rounds=True)

