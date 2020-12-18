import re

f = open('18.txt')
# strip to remove \n, split to remove spaces, put back into string to split on non-numerical and remove '' entries (?)
rows = [[x for x in re.split(r'(\D)',"".join(r.strip().split())) if x] for r in f.readlines()]
f.close()

#rows = [["2","*","3","+","(","4","*","5",")"]]
rows = [["2","*","3","+","20"]]

def simplify(expression):
	if len(expression) == 1:
		return int(expression[0])
	#find first operator
	parensCounter = 0
	needToRemoveParens = False
	additionFound = False
	iopen = -1
	iclose = -1
	for i,c in enumerate(reversed(expression)):
		
		### parens ###
		if c == ')':
			parensCounter += 1
			iclose = len(expression) - i
		if c == '(':
			parensCounter -= 1
			iopen = len(expression) - i
			needToRemoveParens = True
			if parensCounter == 0:
				return simplify(expression[iopen+1:iclose])

		### addition priority
		if additionFound and parensCounter == 0 and (c in ('*','+') or i == len(expression)-1):
			print(expression)
			print(c)
			if c == '+':
				rh = expression[-i:]
				lh = expression[:-i - 1] 
				return simplify(lh) + simplify(rh)
			if c == '*':				
				rh = expression[-i:]
				lh = expression[:-i - 1] 
				return simplify(lh) * simplify(rh)
			else:
				return simplify(expression[-i:])

		if parensCounter == 0 and c in ('*','+'):
			rh = expression[-i:] # we're in reverse
			#if needToRemoveParens:
			#	rh = rh[1:-1]
			op = c
			if op == '+':
				additionFound = True
				#return simplify(expression[:-1 - i]) + simplify(rh)
			if op == '*':
				return simplify(expression[:-1 - i]) * simplify(rh)
			
		# left-most '('
		if i == len(expression) -1:
			if c == '(':
				rh = expression[-i:-1]
				return simplify(rh)
	print('not processed ' + str(expression))
total = 0
for expression in rows:
	total += int(simplify(expression))
	
print(total)