import sys

n = len(sys.argv)


if n > 2 :
	
	print("Erreur : un seul argument.")
	
else :
	
	if isinstance(sys.argv[1], str) == True :
		
			print(len(sys.argv[1]))
		
	else :
		
		print("Erreur : Mauvais type.")