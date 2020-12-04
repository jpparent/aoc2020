f = open('04.txt')
rows = f.readlines()
f.close()

validCount = 0
byr = iyr = eyr = hgt = hcl = ecl = pid = cid = -1

i = 0
while i < len(rows):
	
	row = str(rows[i])
	i +=1 # next line

	if len(row) < 2: #end of passport entry or end of file

		if byr >= 0 and iyr >= 0 and eyr >= 0 and hgt >= 0 and hcl >= 0 and ecl >= 0 and pid >= 0 :
			validCount += 1

		byr = iyr = eyr = hgt = hcl = ecl = pid = cid = -1

		continue

	byr = row.find('byr') if byr == -1 else byr
	iyr = row.find('iyr') if iyr == -1 else iyr
	eyr = row.find('eyr') if eyr == -1 else eyr
	hgt = row.find('hgt') if hgt == -1 else hgt
	hcl = row.find('hcl') if hcl == -1 else hcl
	ecl = row.find('ecl') if ecl == -1 else ecl
	pid = row.find('pid') if pid == -1 else pid
	cid = row.find('cid') if cid == -1 else cid # optional


print(str(validCount))