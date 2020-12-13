f = open('13.txt')
rows = f.readlines()
f.close()

ids = [int(x) if x != 'x' else 0 for x in rows[1].split(',')]

t = 0
i = 0
earliestT = None

while True:
	print(t,end='\r')
	if i == len(ids):
		break # matched all
	elif ids[i] == 0:
		i += 1
		t += 1
		continue
	elif t % ids[i] == 0:
		earliestT = t if not earliestT else earliestT
		i += 1
		t += 1
		continue
	else:
		if i == 0: 
			t += 1
		else:
			i = 0 # restart check
		earliestT = None

print()
print(earliestT)