import sys

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

arg = sys.argv[1]

if len(arg) > 1 :
	print("Erreur ! Entrer un lettre")

index = alph.index(arg)

for i in range (index, len(alph)) :
	
	if alph[i] =='z' :
		
		print(alph[i], end ='\n')
		
	else :
	
		print(alph[i], end ='')