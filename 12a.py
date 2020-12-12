import copy
f = open('12.txt')
instructions = [[r[:1],r[1:].strip()] for r in f.readlines()]
f.close()

x = y = 0
n = [0,1]
e = [1,0]
s = [0,-1]
w = [-1,0]
dirs = [n,e,s,w]
face = 1 # index in the directions list

for ins in instructions:
	a = ins[0]
	v = int(ins[1])

	if a == 'N':
		y += v
	if a == 'S':
		y -= v
	if a == 'E':
		x += v
	if a == 'W':
		x -= v
	if a == 'L':
		dec = v//90
		face -= dec
		if face < 0:
			face += 4
	if a == 'R':
		inc = v//90
		face += inc
		if face >= 4:
			face -= 4
	if a == 'F':
		x += v * dirs[face][0]
		y += v * dirs[face][1]

print(abs(x) + abs(y))