import math
f = open('13.txt')
rows = f.readlines()
f.close()

ids = [int(x) if x != 'x' else 0 for x in rows[1].split(',')]

earliestT = 0
t = 0
for i in range(0,len(ids)):
	while True:
		if ids[i] == 0: # joker, skip over
			t += 1
			break
		elif t % ids[i] == 0: # match
			earliestT = t-i if earliestT == 0 else earliestT
			t += 1
			break
		else: # no match, skip ahead to next start of current pattern by Lowest Common Multiple of the ids so far (they're all prime so it's the total prod)
			inc = math.prod([ids[j] for j in range(0, i) if ids[j] != 0]) 
			t += inc
			earliestT = 0	

print(earliestT)