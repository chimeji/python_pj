#from crypt import crypt
from passlib.hash import sha256_crypt as sha256
import time

searchWord='KSIdqhF5l6N2s'
alphabet = 'abcefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"&#{[-|_^@]=+.,:;?!$'
#alphabet = 'abcefghijklmnopqrstuvwxyz{[-|_^@]=+.:;?!'
passlen = 8
mySalt = 'KS'

alphalen = len(alphabet)
nbpass = alphalen**passlen 
estimatedTime = (nbpass/100000)*16
start_time = time.time()

print ('alphalen :  '+ str(alphalen))
print ('nbpass   : ' + str(nbpass))
print ('16 sec for 100000 gen')
print ('Estimated time : ' + str(estimatedTime) + ' sec')
m, s = divmod(estimatedTime, 60)
h, m = divmod(m, 60)
#for i in range(100000):

#Boucle infinie
i = 0
while True:
	#Generation chaine
	car8 = alphabet[(i%(alphalen**8))//alphalen**7]
	car7 = alphabet[(i%(alphalen**7))//alphalen**6]
	car6 = alphabet[(i%(alphalen**6))//alphalen**5]
	car5 = alphabet[(i%(alphalen**5))//alphalen**4]
	car4 = alphabet[(i%(alphalen**4))//alphalen**3]
	car3 = alphabet[(i%(alphalen**3))//alphalen**2]
	car2 = alphabet[(i%(alphalen**2))//alphalen**1]
	car1 = alphabet[(i%(alphalen**1))]
	wordI = car8 + car7 + car6 + car5 + car4 + car3 + car2 + car1 

	#Cryptage
	passWord = sha256.encrypt(wordI, salt=mySalt, rounds=5000, implicit_rounds=True)

	#Affichage si OK
	print ('Word : ' + wordI + ' Crypt : ' + passWord + ' i : ' + str(i))
	if passWord == searchWord:
		print ('Word : ' + wordI + ' Crypt : ' + passWord + ' i : ' + str(i))
		print ("Exec Time : %s" % (time.time() - start_time))
		break
	i = i + 1
