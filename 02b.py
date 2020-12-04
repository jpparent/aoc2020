import re

f = open('02.txt')
rows = f.readlines()
f.close()

validCount = 0

for row in rows:
	result = re.search('(.+)-(.+) (.): (.+)', row)
	pos1 = int(result.group(1))
	pos2 = int(result.group(2))
	letter = str(result.group(3))
	pwd = str(result.group(4))

	if (pwd[pos1-1] == letter) != (pwd[pos2-1] == letter) :
		validCount += 1

print(str(validCount))

