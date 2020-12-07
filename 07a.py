import re

f = open('07.txt')
rows = f.readlines()
f.close()

totalBagNames = set()

def findHolder(color):
	global totalBagNames
	for row in rows:
		result = re.search('^(.+) bags \w+.* \d+ '+ color + ' \w+\W{1}.*', row)
		if result:
			totalBagNames.add(result.group(1))
			findHolder(result.group(1))

findHolder('shiny gold')
print(len(totalBagNames))