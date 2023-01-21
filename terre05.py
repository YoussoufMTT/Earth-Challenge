import sys

sys.argv.pop(0)

n = len(sys.argv)

arg = sys.argv[0]
 
if n >= 2 :

	print("Un seul à la fois..")
	
else:
	
	if arg.lstrip('-').isnumeric() == False :
	
		print("Un number, s'il vous please !")
		
	else :
		
		if int(arg) % 2 == 0 :
			
			print("Nombre pair !")
			
		else :
			
			print("Nombre impair !")