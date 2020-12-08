f = open('08.txt')
rows = f.readlines()
f.close()

accumulator = 0
exIns = set()

i = 0
while True:
	ins = rows[i].strip()
	if ins + str(i) in exIns:
		break
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

	if i >= len(rows):
		i -= len(rows)


print(accumulator)