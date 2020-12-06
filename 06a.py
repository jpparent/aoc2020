from collections import Counter

f = open('06.txt')
rows = f.readlines()
f.close()

totalAnswers = 0

counters = []

for i in range(0,len(rows)+1):

	#end of group
	if i == len(rows) or not rows[i].strip():
		totalCount = Counter()
		for counter in counters:
			totalCount += counter
		totalAnswers += len(list(totalCount))
		counters.clear()
		continue
	else:
		counters.append(Counter(rows[i].strip()))


print(str(totalAnswers))
