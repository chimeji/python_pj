count = 0

lentab1 = 5
lentab2 = 7
lentab3 = 4
bases = ['abdce', '1234567', '$;,:']

nbComb = 1
for base in bases:
	nbComb = nbComb * len(base)	


for nb in range(0,nbComb):
	i = nb//(len(bases[1])*len(bases[2]))
	j = (nb%(len(bases[1])*len(bases[2])))//len(bases[2])
	k = (nb%(len(bases[1])*len(bases[2])))%len(bases[2])

	print("{} [{} {} {}] = ".format(nb,i,j,k) + bases[0][i] + bases[1][j] + bases[2][k])

	
	
