input = [1,0,15,2,10,13]

def nthNumber(number):
	mem = dict()
	for j,n in enumerate(input):
		mem[n] = j

	last = input[-1]

	for i in range(len(input), number):
		new = 0
		if last in mem and mem[last] < i - 1: #was not first time said
			new = (i-1) - mem[last]
		mem[last] = i - 1
		last = new
	return last

def part1():
	print(nthNumber(2020))

def part2():
	print(nthNumber(30000000))

part1()
part2()