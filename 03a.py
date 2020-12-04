import re

f = open('03.txt')
rows = f.readlines()
f.close()

treeCount = 0

x = 0
for y in range(0,len(rows)):
	if rows[y][x] == '#':
		treeCount += 1
	x += 3 # slope is right 3, down 1
	# loop around the input's horizontally
	if x >= len(rows[y])-1:
		x -= len(rows[y])-1

print(str(treeCount))

