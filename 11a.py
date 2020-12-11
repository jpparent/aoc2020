import copy
f = open('11.txt')
layout = [[c for c in r.strip()] for r in f.readlines()]
f.close()

empty = 'L'
floor = '.'
occupied = '#'

adjacentCoordsIncrement = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

lenX = len(layout[0])
lenY = len(layout)

def PrintLayout():
	for row in layout:
		print("".join(row))
	print('\n')

def CountAdjacent(x,y,layout):
	count = 0
	for inc in adjacentCoordsIncrement:
		if y + inc[0] < 0 or y + inc[0] > lenY - 1:
			continue
		if x + inc[1] < 0 or x + inc[1] > lenX - 1:
			continue
		if layout[y + inc[0]][x + inc[1]] == occupied:
			count += 1
	return count

def ApplyRules():
	global layout
	changesCount = 0
	# read from a copy to simulate all rules applying simultaneously
	layoutCopy = copy.deepcopy(layout)

	for y in range(0, lenY):
		for x in range(0, lenX):
			if layoutCopy[y][x] == floor:
				continue
			if layoutCopy[y][x] == empty and CountAdjacent(x,y,layoutCopy) == 0:
				layout[y][x] = occupied
				changesCount += 1
			if layoutCopy[y][x] == occupied and CountAdjacent(x,y,layoutCopy) >= 4:
				layout[y][x] = empty
				changesCount +=1		
	return changesCount

#PrintLayout()
while ApplyRules() != 0:
	pass
#	PrintLayout()

def CountTotalOccupied():
	c = 0
	for row in layout:
		c += row.count(occupied)
	return c

print(CountTotalOccupied())