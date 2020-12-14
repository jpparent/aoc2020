import copy

f = open('14.txt')
rows = [r.strip().split(' = ') for r in f.readlines()]
f.close()

mem = dict()
mask = 0

def recfloating(laddress, laddresses):
	if laddress.count('X') == 0:
		return
	for i,c in enumerate(laddress):
		if c == 'X':
			# append new addresses with the X changed
			laddress[i] = '0'
			laddresses.append(laddress)
			newladdress = copy.deepcopy(laddress)
			newladdress[i] = '1'
			laddresses.append(newladdress)
			# recursively decode the floating for these new addresses
			recfloating(laddress, laddresses)
			recfloating(newladdress, laddresses)
			break

def decode(baddress,mask):
	baddress = str(baddress)[2:] # keep only bits
	while len(baddress) < 36:
		baddress = '0' + baddress # prepend the leading 0s
	baddress = list(baddress) # change to a list for easy char replacing
	for i,b in enumerate(mask):
		if b == 'X':
			baddress[i] = 'X'
		elif b == '1':
			baddress[i] = '1'
	lis = []
	recfloating(baddress,lis)
	return lis
	
for ins,val in rows:
	if ins[0:3] == 'mas':
		mask = val
	else:
		address = ins[4:-1]
		addresses =  decode(bin(int(address)), mask)
		for la in addresses:
			sa = ''.join(la)
			ia = int(sa,2)
			mem[ia] = int(val)

print(sum(mem.values()))