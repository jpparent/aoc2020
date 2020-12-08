f = open('08.txt')
rows = f.readlines()
f.close()

insLenght = len(rows)

def testProgram(instructions):
	global insLenght

	accumulator = 0
	exIns = set()
	i = 0

	while i != insLenght:
		ins = instructions[i].strip()
		if ins + str(i) in exIns:
			return [False, accumulator]
		# store the full instruction + its index
		exIns.add(ins + str(i))

		op = ins[:3]
		arg = ins[4:]

		if op == 'nop':
			pass
		if op == 'acc':
			val = int(arg[1:])
			val *= 1 if arg[0] == '+' else -1
			accumulator += val
		if op == 'jmp':
			val = int(arg[1:])
			val *= 1 if arg[0] == '+' else -1
			i += val
		else:
			i += 1

	return [True, accumulator]

for i in range(0,insLenght):
	ins = rows[i].strip()
	if ins[:3] == 'jmp':
		testInstructions = list(rows)
		testInstructions[i] = 'nop' + ins[3:]
		res = testProgram(testInstructions)
		if res[0]:
			print(res[1])
	if ins[:3] == 'nop':
		testInstructions = list(rows)
		testInstructions[i] = 'jmp' + ins[3:]
		res = testProgram(testInstructions)
		if res[0]:
			print(res[1])

