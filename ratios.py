import csv

def getOneWay(reader, targetIndex, notwants):
	target = 0
	total = 0
	header = True
	for row in reader:
		if header:
			header = False
		else:
			total += 1
			passPls = False 
			for index in notwants:
				if(row[index] != '[]'):
					passPls = True
			if(passPls):
				continue
			if(row[targetIndex] != '[]' and row[targetIndex] != ''):
				target += 1
	return target / float(total)

def getNeg(reader, notwants):
	target = 0
	total = 0
	header = True
	for row in reader:
		if header:
			header = False
		else:
			total += 1
			passPls = False
			for index in notwants:
				if(row[index] != '[]'):
					passPls = True
			if(passPls):
				continue
			target += 1
	print target
	print total
	return target / float(total)

def getPos(reader, dowants):
	target = 0
	total = 0
	header = True
	for row in reader:
		if header:
			header = False
		else:
			total += 1
			passPls = False
			for index in dowants:
				if(row[index] == '[]'):
					passPls = True
			if(passPls):
				continue
			target += 1
	return target / float(total)
def getTwoWay(reader, numIndex, demIndex, notwants):
	numCount = 0
	demCount = 0
	header = True
	for row in reader:
		if header:
			header = False
		else:
			passPls = False
			for index in notwants:
				if(row[index] != '[]'):
					passPls = True
			if(passPls):
				continue
			if(row[demIndex] != '[]' and row[demIndex] != ''):
				demCount += 1
				if(row[numIndex] != '[]' and row[numIndex] != ''):
					print row[numIndex]
					numCount += 1
	return numCount / float(demCount)

def getTwoWayNeg(reader, numIndex, notwants):
	numCount = 0
	demCount = 0
	header = True
	for row in reader:
		if header:
			header = False
		else:
			passPls = False
			for index in notwants:
				if(row[index] != '[]' or row[index] != ''):
					passPls = True
			if(passPls):
				continue
			demCount += 1
			if(row[numIndex] != '[]' and row[numIndex] != ''):
				numCount += 1
	return numCount / float(demCount)


'''
def getTwoWayPos(reader, numIndex, demIndex, dowants):
	numCount = 0
	demCount = 0
	header = True
	for row in reader:
		if header:
			header = False
		else:
			passPls = 
			for index in dowants:
				if(row[index])
'''
colIndices = []
rowIndices = [24,]
vpNegs = [15,22,27]
def tableMaker(ifile,ofile):
	csvifile = open(ifile, 'rU')
	reader = list(csv.reader(csvifile))
	csvofile = open(ofile, 'w')
	writer = csv.writer(csvofile)
	writer.writerow(['VP-ing','DET-ing','DET-of-ing','Poss-ing','Poss-dobj-ing','Poss-of-ing','Total'])
	writer.writerow([str(getNeg(reader,vpNegs)),str(getOneWay(reader,22,[15])),str(getPos(reader,[15,22])),str(getOneWay(reader,27,[13,15])),str(getPos(reader, [27,13])),str(getPos(reader, [27,15])),'0' ])



tableMaker('spendingOut.csv', 'spendingTable.csv')
#print getOneWay('testingOut.csv', 27)

	

