import re

f = open('18.txt')
# strip to remove \n, split to remove spaces, put back into string to split on non-numerical and remove '' entries (?)
rows = [[x for x in re.split(r'(\D)',"".join(r.strip().split())) if x] for r in f.readlines()]
f.close()

def simplify(expression):
	if len(expression) == 1:
		return int(expression[0])
	#find first operator
	parensCounter = 0
	needToRemoveParens = False
	for i,c in enumerate(reversed(expression)):
		if c == ')':
			parensCounter += 1
		if c == '(':
			parensCounter -= 1
			needToRemoveParens = True
		if parensCounter == 0 and c in ('*','+'):
			rh = expression[-i:] # we're in reverse
			if needToRemoveParens:
				rh = rh[1:-1]
			op = c
			if op == '*':
				return simplify(expression[:-1 - i]) * simplify(rh)
			if op == '+':
				return simplify(expression[:-1 - i]) + simplify(rh)
			
		elif i == len(expression) -1:
			if c == '(':
				rh = expression[-i:-1]
				return simplify(rh)
	print(expression)
total = 0
for expression in rows:
	total += int(simplify(expression))
	
print(total)