#from crypt import crypt
from passlib.hash import sha256_crypt as sha256
from loopCode import LoopCode
import threading
import time


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

myLoop = LoopCode(0, 3, searchWord, mySalt, tabBase) 
myLoop.start()

#ten_loop_code(searchWord, mySalt, tabBase)





