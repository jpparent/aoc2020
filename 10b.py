f = open('10.txt')
rows = [int(r) for r in f.readlines()]
f.close()

rows.sort()
rows.insert(0,0) # insert the 0 jolt outlet

paths = [0] * len(rows)

def f(n):
	# first adapter has only one possibility
	if n == 0:
		paths[n] = 1
		return

	count = 0
	for i in range(1,4):
		if n - i < 0:
			break

		if rows[n - i] + 3 >= rows[n]:
			count += paths[n - i]
	
	paths[n] = count

# count all possibilities to each adapter from bottom up
for k in range (0, len(rows)):
	f(k)
# how many possibilities to plug the last adapter
print (paths[len(paths)-1])