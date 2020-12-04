f = open('01.txt')
rows = f.readlines()
f.close()

for i in range(0, len(rows)-1):
	for j in range(i, len(rows)-1):
		current = eval(rows[i])
		other = eval(rows[j])
				
		if current + other == 2020:
			print(str(current*other))
			break
