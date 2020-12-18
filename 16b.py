import re

f = open('16.txt')
rows = [r.strip() for r in f.readlines()]
f.close()

rules = dict()
myTicket = []
tickets = []

def parse():
	global myTicket
	myTicketIndex = -1
	for i in range(0,len(rows)):
		if '-' in rows[i]:
			res = re.search('([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', rows[i])
			if res:
				rules[res.group(1)] = [[int(res.group(2)),int(res.group(3))],[int(res.group(4)),int(res.group(5))]]
		elif rows[i] == "your ticket:":
			myTicketIndex = i + 1
		elif i == myTicketIndex:
			myTicket = [int(c) for c in rows[i].split(',')]
		elif not rows[i]:
			continue
		elif ',' in rows[i]:
			tickets.append([int(c) for c in rows[i].split(',')])


def validate(ticket):
	for val in ticket:
		isValueValid = False
		for rule,bounds in rules.items():
			if val >= bounds[0][0] and val <= bounds[0][1] or val >= bounds[1][0] and val <= bounds[1][1]:
				isValueValid = True
		if not isValueValid:
			return False
	return True

parse()
tickets = [ticket for ticket in tickets if validate(ticket)] # remove invalid tickets

fittingfields = [dict()] * len(myTicket)
# loop each i value of all tickets to find the field it represents
for i in range(0, len(myTicket)):
	for t in tickets:
		for field,bounds in rules.items():
			if t[i] >= bounds[0][0] and t[i] <= bounds[0][1] or t[i] >= bounds[1][0] and t[i] <= bounds[1][1]:
				# add one to the fitting field counter
				if field not in fittingfields[i]:
					fittingfields[i][field] = 1
				else:
					fittingfields[i][field] += 1
			else:
				# substract one to the fitting field counter
				if field not in fittingfields[i]:
					fittingfields[i][field] = -1
				else:
					fittingfields[i][field] -= 1

orderedfields = sorted(fittingfields[0].items(), key=lambda item: item[1], reverse=True)

total = 1
for k in range(0, len(myTicket)):
	print(orderedfields[k][0].split()[0])
	if (orderedfields[k][0].split()[0] == "departure"):
		total *= myTicket[k]

print(total)