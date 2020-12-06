from collections import Counter

f = open('06.txt')
rows = f.readlines()
f.close()

totalAnswers = 0

counters = []
groupSize = 0

for i in range(0,len(rows)+1):

	#end of group
	if i == len(rows) or not rows[i].strip():
		totalCount = Counter()
		for counter in counters:
			totalCount += counter
		for char, count in totalCount.items():
			if count == groupSize:
				totalAnswers += 1
		counters.clear()
		groupSize = 0
		continue
	else:
		groupSize += 1
		counters.append(Counter(rows[i].strip()))


print(str(totalAnswers))
