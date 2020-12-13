f = open('13.txt')
rows = f.readlines()
f.close()

earliestDeparture = int(rows[0].strip())
busIDs = [int(x) for x in rows[1].split(',') if x != 'x']

earliestBusId = 0
t = earliestDeparture
while earliestBusId == 0:
	t += 1
	for id in busIDs:
		if t % id == 0:
			earliestBusId = id
			break

print(earliestBusId * (t - earliestDeparture))