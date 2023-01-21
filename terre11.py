import sys

nombre = sys.argv[1]
if nombre.isnumeric() == False :
	
	print ("Erreur, Entrer un nombre positif.")

else :
			
	nombre = int(sys.argv[1])

	i = 1
	k = 0 

	while i <= nombre or k < 0 :
	
		if i != nombre and i != 1 and nombre % i == 0 :
		
			k+=1
			
		i+=1