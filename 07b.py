import re

f = open('07.txt')
rows = f.readlines()
f.close()

def countHeldBags(color):
	for row in rows:
		typeSearch = re.search('^' + color + ' bags', row)
		if typeSearch:
			result = re.findall('(\d+) ([\w ]+) bags?[.,]{1}', row)
			if not result:
				return 0
			else:
				total = 0
				for res in result:
					c = int(res[0])
					b = res[1]
					total += (c + (c * countHeldBags(b)))
				return total

print(countHeldBags('shiny gold'))