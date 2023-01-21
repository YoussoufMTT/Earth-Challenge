import sys

if len(sys.argv) == 4 :
	
	a = sys.argv[1]
	b = sys.argv[2]
	c = sys.argv[3]

	if (a <= b and a >= c) or (a >= b and a <= c):
		
		print("La valeur médiane est :", a)
		
	elif (b <= a and b >= c) or (b >= a and b <= c):
		
		print("La valeur médiane est :", b)
		
	elif (c <= b and c >= a) or (c >= b and c <= a):
	
		print("La valeur médiane est :", c)
	
else :
	
	print("Erreur ! Entrez trois nombres.")	