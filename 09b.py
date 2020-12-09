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

invalidNumber = 0

for i in range(preambleSize - 1,len(rows)):
	if not IsValid(rows[i], i):
		invalidNumber = rows[i]
		break

contiguous = []
i = 0
while sum(contiguous) != invalidNumber and i < len(rows):
	contiguous.clear()
	for j in range(i, len(rows)):
		contiguous.append(rows[j])
		if sum(contiguous) >= invalidNumber:
			i += 1
			break

print(min(contiguous) + max(contiguous))