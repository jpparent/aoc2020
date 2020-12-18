import re

f = open('16.txt')
rows = [r.strip() for r in f.readlines()]
f.close()

rules = dict()
myTicket = []
tickets = []
invalidFields = []

myTicketIndex = -1
for i in range(0,len(rows)):
	if '-' in rows[i]:
		res = re.search('([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', rows[i])
		if res:
			rules[res.group(1)] = [[int(res.group(2)),int(res.group(3))],[int(res.group(4)),int(res.group(5))]]
	elif rows[i] == "your ticket:":
		myTicketIndex = i + 1
	elif i == myTicketIndex:
		myTicket = rows[i].split(',')
	elif not rows[i]:
		continue
	elif ',' in rows[i]:
		tickets.append([int(c) for c in rows[i].split(',')])

for ticket in tickets:
	for val in ticket:
		valid = False
		for rule,bounds in rules.items():
			if val >= bounds[0][0] and val <= bounds[0][1] or val >= bounds[1][0] and val <= bounds[1][1]:
				valid = True
		if not valid:
			invalidFields.append(val)

print(sum(invalidFields))