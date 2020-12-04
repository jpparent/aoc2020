import re
import math

f = open('03.txt')
rows = f.readlines()
f.close()

treeCounts = [0,0,0,0,0]

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for s in range(0,len(slopes)):
	
	x = 0
	y = 0

	# use a while loop to be able to change the index dynamically
	while y < len(rows): 
		
		if rows[y][x] == '#':
			treeCounts[s] += 1
		x += slopes[s][0] 
		
		# loop around the input's horizontally
		if x >= len(rows[y])-1:
			x -= len(rows[y])-1
		
		# go down the slope
		y += slopes[s][1]

print(str(math.prod(treeCounts)))