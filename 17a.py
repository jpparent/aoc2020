import copy

f = open('17t.txt')
rows = [r.strip() for r in f.readlines()]
f.close()

class Cube(object):
	def __repr__(self):
		return "x={0},y={1},z={2},active={3}".format(self.x,self.y,self.z,self.active)
	def __str__(self):
		return "x={0},y={1},z={2},active={3}".format(self.x,self.y,self.z,self.active)
	def __init__(self, x, y, z, active):
		super(Cube, self).__init__()
		self.x = x
		self.y = y
		self.z = z
		self.active = active
		if (active):
			self.activate()
	def countActiveNeighbors(self):
		count = 0
		for (x,y,z) in self.getAllNeighborCoords():
			c = getCube(x,y,z)
			if c and c.active:
				count += 1
		return count

	def getAllNeighborCoords(self):
		coords = []
		for i in range(self.x-1, self.x+2):
			for j in range(self.y-1, self.y+2):
				for k in range(self.z-1, self.z+2):
					if (i,j,k) != (self.x,self.y,self.z):
						coords.append([i,j,k])
		return coords
	def tick(self):
		n = self.countActiveNeighbors()
		if self.active and n == 2 or n == 3:
			pass
		elif not self.active and n == 3:
			self.active = True
	def activate(self):
		# "wake" the neighboors
		for n in self.getAllNeighborCoords():
			if not exists(n[0],n[1],n[2]):
				space.append(Cube(n[0],n[1],n[2], False))

def exists(x,y,z):
	return bool([c for c in space if (c.x,c.y,c.z) == (x,y,z)])
def getCube(x,y,z):
	if exists(x,y,z):
		return [c for c in space if (c.x,c.y,c.z) == (x,y,z)][0]

space = []
for i in range(0,len(rows)):
	for j in range(0, len(rows[i])):
		if rows[i][j] == '#':
			c = Cube(j,i,0,True)
			space.append(c)

for i in range(0,6):
	spacecopy = copy.deepcopy(space)
	for c in spacecopy:
		c.tick()
	 


print(len([c for c in space if c.active]))
