import sys

exposé = int(sys.argv[1])
exposant = int(sys.argv[2])

if exposant < 0 :

	print("Erreur : exposant négatif.")

else :

	res = exposé ** exposant
	print("Résultat :", res)