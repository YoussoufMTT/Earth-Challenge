import sys
import math

nombre = sys.argv[1]

if len(sys.argv) > 2 :

	print("Erreur, un seul argument")

if nombre.isdecimal() == False :
	
	print ("Erreur, Entrer un nombre positif.")

else :

	print("La racine carrée de ",float(nombre) ," est ", math.sqrt(float(nombre)))
	