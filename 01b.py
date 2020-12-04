f = open('01.txt')
rows = f.readlines()
f.close()

for i in range(0, len(rows)-1):
	for j in range(i, len(rows)-1):
		for k in range(j, len(rows)-1):
			
			a = eval(rows[i])
			b = eval(rows[j])
			c = eval(rows[k])
					
			if a + b + c == 2020:
				print(str(a*b*c))
				exit()
