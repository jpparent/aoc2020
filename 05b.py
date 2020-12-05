import math

f = open('05.txt')
rows = f.readlines()
f.close()

seatIDs = []

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
	seatIDs.append(seatID)

for i in range(0, len(seatIDs)):
	for j in range(i, len(seatIDs)):
		if abs(seatIDs[i] - seatIDs[j]) == 2:
			inBetween = (seatIDs[i] + seatIDs[j]) * 0.5
			if inBetween not in seatIDs:
				print(str(inBetween))

