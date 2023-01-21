import sys

k = 0
maxi = len(sys.argv) - 1

if len(sys.argv) > 3 :

	for i in range(1, maxi) :
		
		if (sys.argv[i] < sys.argv[i+1]) :
			
			k+=1	
		
	if k == len(sys.argv) - 2 :
		
		print("Trié !")
	
	else :
		
		print("Pas Trié !")
		
					
else :
	
	print("Erreur ! Entre au minimum 3 nombres.")