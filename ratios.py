import csv

def getOneWay(ifile, targetIndex):
	csvifile = open(ifile, 'rU')
	reader = csv.reader(csvifile)
	target = 0
	total = 0
	header = True
	for row in reader:
		total += 1
		if header:
			header = False
		else:
			if(row[targetIndex] != '[]' and row[targetIndex] != ''):
				target += 1
	return target / float(total)

def getTwoWay(ifile, numIndex, demIndex):
	csvifile = open(ifile, 'rU')
	reader = csv.reader(csvifile)
	numCount = 0
	demCount = 0
	header = True
	for row in reader:
		if header:
			header = False
		else:
			if(row[demIndex] != '[]' and row[demIndex] != ''):
				demCount += 1
				if(row[numIndex] != '[]' and row[numIndex] != ''):
					numCount += 1
	return numCount / float(demCount)



print getTwoWay('springingOut.csv', 15, 22)
print getOneWay('testingOut.csv', 22)

	

