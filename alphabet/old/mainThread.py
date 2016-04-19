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
myLoop2 = LoopCode(4, 7, searchWord, mySalt, tabBase) 
myLoop.start()
myLoop2.start()

#Sleep for 10 secs
time.sleep(5)
myLoop.stop()
myLoop2.stop()

print(myLoop.getCurrent())
print(myLoop2.getCurrent())

print("Number of loops : " + str(myLoop2.getLoopCount() + myLoop.getLoopCount()))

#ten_loop_code(searchWord, mySalt, tabBase)





