import sys



lg = len(sys.argv)

sentence = []

for j in range(1,lg) :

	l = list(sys.argv[j]) # On transforme chaque mot en liste

	for k in l :

		if k == l[0] :

			sentence.append(k + ' ')

		else :

				sentence.append(k)

n = len(sentence)

for i in range(0, n):

	if i == n-1 :

		print(sentence[n -1 - i], end ='\n')

	else :

		print(sentence[n -1 - i], end ='')