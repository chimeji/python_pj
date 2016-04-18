#from crypt import crypt
from passlib.hash import sha256_crypt as sha256
import threading

############
# LoopCode #
############
class LoopCode(threading.Thread):
	def __init__(self, start, stop, findWord, salt, bases):
		threading.Thread.__init__(self)
		self._start = start
		self._stop = stop
		self._findWord = findWord
		self._salt = salt
		self._bases = bases 
	
	def run(self):
		loopCount = 0
		for i in range(self._start, self._stop):
			car1 = self._bases[0][i]
			for car2 in self._bases[1]:
				for car3 in self._bases[2]:
					for car4 in self._bases[3]:
						for car5 in self._bases[4]:
							for car6 in self._bases[5]:
								for car7 in self._bases[6]:
									for car8 in self._bases[7]:
										word = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8
										encrypted = sha256.encrypt(word, salt=self._salt, rounds=5000, implicit_rounds=True)
										print (str(loopCount) + " word : " + word + " encrypted : " + encrypted)
										loopCount = loopCount + 1


