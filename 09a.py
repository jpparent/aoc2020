f = open('09.txt')
rows = [int(r) for r in f.readlines()]
f.close()

preambleSize = 25

def IsValid(number, index):

	for i in range(index - preambleSize, index):
		for j in range(i, index):
			if rows[i] != rows[j] and rows[i] + rows[j] == number:
				return True
	return False

for i in range(preambleSize - 1,len(rows)):
	if not IsValid(rows[i], i):
		print(rows[i])
		break