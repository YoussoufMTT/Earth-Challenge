import sys

num = sys.argv[1]
denum = sys.argv[2]

if num.lstrip('-').isnumeric() == False or denum.lstrip('-').isnumeric() == False : 
	
	print("Erreur ! Uniquement des nombres.")
	exit()
	
if int(num) < int(denum) or int(denum) == 0 :
	
	print("Erreur ! Numérateur inférieur au dénumérateur.")
	
else :
	
	rés = int(num) // int(denum)
	reste = int(num) % int(denum)
	
	print("Résultat de la division entière :", rés)
	print("Reste :", reste)