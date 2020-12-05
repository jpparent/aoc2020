import math

f = open('05.txt')
rows = f.readlines()
f.close()

highestID = 0

for row in rows:
	r = [0,127]
	c = [0,7]

	for letter in row:
		if letter == 'F':
			r[1] = math.floor((r[1]-r[0])*0.5)+r[0]
		if letter == 'B':
			r[0] = math.ceil((r[1]-r[0])*0.5)+r[0]
		if letter == 'L':
			c[1] = math.floor((c[1]-c[0])*0.5)+c[0]
		if letter == 'R':
			c[0] = math.ceil((c[1]-c[0])*0.5)+c[0]

	seatID = r[0] * 8 + c[0]
	if seatID > highestID:
		highestID = seatID

print(str(highestID))