import re

f = open('02.txt')
rows = f.readlines()
f.close()

validCount = 0

for row in rows:
	result = re.search('(.+)-(.+) (.): (.+)', row)
	min = int(result.group(1))
	max = int(result.group(2))
	letter = str(result.group(3))
	pwd = str(result.group(4))

	letterCount = pwd.count(letter)
	if letterCount >= min and letterCount <=max :
		validCount += 1

print(str(validCount))

