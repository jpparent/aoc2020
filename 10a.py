f = open('10.txt')
rows = [int(r) for r in f.readlines()]
f.close()

rows.sort()
diffs = []
last = 0
for adapt in rows:
	diffs.append(adapt - last)
	last = adapt
diffs.append(3) # device's adapter is always 3 higher

print(diffs.count(1) * diffs.count(3))