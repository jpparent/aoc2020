import re

f = open('04.txt')
rows = f.readlines()
f.close()

validCount = 0
byr = iyr = eyr = hgt = hcl = ecl = pid = cid = False

i = 0
while i < len(rows):
	
	row = str(rows[i])
	i +=1 # next line

	if len(row) < 2: #end of passport entry or end of file

		if byr and iyr and eyr and hgt and hcl and ecl and pid:
			validCount += 1

		byr = iyr = eyr = hgt = hcl = ecl = pid = cid = False
		
		continue
		
	if not byr:
		byrRes = re.search('byr:(\d{4})', row)
		byrVal = int(byrRes.group(1)) if byrRes else -1
		if byrVal >= 1920 and byrVal <= 2002:
			byr = True

	if not iyr:
		iyrRes = re.search('iyr:(\d{4})', row)
		iyrVal = int(iyrRes.group(1)) if iyrRes else -1
		if iyrVal >= 2010 and iyrVal <= 2020:
			iyr = True

	if not eyr:
		eyrRes = re.search('eyr:(\d{4})', row)
		eyrVal = int(eyrRes.group(1)) if eyrRes else -1
		if eyrVal >= 2020 and eyrVal <= 2030:
			eyr = True

	if not hgt:
		hgtRes = re.search('hgt:(\d+)(.{2})', row)
		if hgtRes:
			hgtVal = int(hgtRes.group(1))
			hgtUnit = hgtRes.group(2)
			if hgtUnit == 'cm':
				if hgtVal >= 150 and hgtVal <= 193:
					hgt = True
			elif hgtUnit == 'in':
				if hgtVal >= 59 and hgtVal <= 76:
					hgt = True

	if not hcl:
		hclRes = re.search('hcl:#([a-fA-F0-9]{6})', row)
		if hclRes:
			hcl = True

	if not ecl:
		eclRes = re.search('ecl:(amb|blu|brn|gry|grn|hzl|oth)', row)
		if eclRes:
			ecl = True

	if not pid:
		pidRes = re.search('pid:(\d{9})', row)
		if pidRes:
			pid = True


print(str(validCount))