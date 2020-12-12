import copy
f = open('12.txt')
instructions = [[r[:1],r[1:].strip()] for r in f.readlines()]
f.close()

x = y = 0
wx = 10
wy = 1
wdx = 10
wdy = 1

def rotateAround(x,y,ax,ay,dir):
	dx = x - ax
	dy = y - ay
	newX = newY = 0
	if dir == 'R':
		newDx = dy
		newDy = -dx
	elif dir == 'L':
		newDx = -dy
		newDy = dx
	x = ax + newDx
	y = ay + newDy
	return [x,y]

for ins in instructions:
	a = ins[0]
	v = int(ins[1])
	#print('ship: ' + str(x) + ',' + str(y) + '  wd: ' + str(wdx) + ',' + str(wdy) + '  wp: ' + str(wx) + ',' + str(wy))
	#print(ins)
	if a == 'N':
		wdy += v
		wy += v
	elif a == 'S':
		wdy -= v
		wy -= v
	elif a == 'E':
		wdx += v
		wx += v
	elif a == 'W':
		wdx -= v
		wx -= v
	elif a == 'F':
		x += v * wdx
		y += v * wdy
		wx = x + wdx
		wy = y + wdy
	else:
		times = v//90
		for t in range(0,times):
			res = rotateAround(wx,wy,x,y,a)
			wx = res[0]
			wy = res[1]
			wdx = wx - x
			wdy = wy - y

print(abs(x) + abs(y))