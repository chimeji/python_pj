#from crypt import crypt
from passlib.hash import sha256_crypt as sha256
import threading
import time

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

################
# PARAMETERS   #
################

#Bases
majuscule = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
majLen = len(majuscule)

minuscule = 'abcdefghijklmnopqrstuvwxyz'
minLen = len(minuscule)

symbole = '!'
symLen = len(symbole)

chiffre = '0123456789'
chiLen = len(chiffre)

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
print("Number of combinaison ", nbComb)

ten_loop_code(searchWord, mySalt, tabBase)





