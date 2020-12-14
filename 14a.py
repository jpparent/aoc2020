f = open('14.txt')
rows = [r.strip().split(' = ') for r in f.readlines()]
f.close()

mem = dict()
mask = 0

def bmask(bval,mask):
	bval = str(bval)[2:] # keep only bits
	while len(bval) < 36:
		bval = '0' + bval # prepend the leading 0s
	bval = list(bval) # change to a list for easy char replacing
	for i,b in enumerate(mask):
		if b == '0':
			bval[i] = '0'
		elif b == '1':
			bval[i] = '1'
	bval = ''.join(bval) # put back as a string
	return int(bval,2) # return as int, from the string read as a bin value
	
for ins,val in rows:
	if ins[0:3] == 'mas':
		mask = val
	else:
		address = ins[4:-1]
		maskedVal = bmask(bin(int(val)),mask)
		mem[address] = maskedVal
	
print(sum(mem.values()))
