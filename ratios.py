import csv
'''
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

def vpingGrabber(list):
	return [row for row in list if row[13] == '[]' and row[15] == '[]' and row[22] == '[]' and row[27] == '[]']

def accingGrabber(list):
	return [row for row in list if row[15] == '[]' and row[22] == '[]' and row[27] == '[]']

def detingGrabber(list):
	return [row for row in list if row[22] != '[]']

def ofingGrabber(list):
	return [row for row in list if row[15] != '[]' and row[22] == '[]' and row[27] == '[]']

def detofingGrabber(list):
	return [row for row in list if row[22] != '[]' and row[15] != '[]']

def possofingGrabber(list):
	return [row for row in list if row[15] != '[]' and row[27] != '[]']

def possingGrabber(list):
	return [row for row in list if row[27] != '[]' and row[15] == '[]']


'''
def getRatio(numList,denList):
	numCount = 0
	denCount = 0
	header = True
	for row in rowsList:
		if header:
			header = False
		else:
'''


colIndices = []
rowIndices = [24,]
vpNegs = [15,22,27]
rowsList= []
def tableMaker(ifile,ofile):
	csvifile = open(ifile, 'rU')
	reader = list(csv.reader(csvifile))[1:]
	csvofile = open(ofile, 'w')
	writer = csv.writer(csvofile)
	'''
	header = True
	i = j = 0
	for row in reader:
		if(header):
			header = False
		else:
			for col in row[8:]:
				if (col != '[]' and col != ''):
					rowsList[i][j] = True
				else:
					rowsList[i][j] = False
				j += 1
			j = 0
	i += 1
	'''
	#print(reader)
	for row in vpingGrabber(reader):
		print row[6]
	writer.writerow(['VP-ing','DET-ing','DET-of-ing','Poss-ing','Poss-dobj-ing','Poss-of-ing','Total'])
	#writer.writerow([str(getNeg(reader,vpNegs)),str(getOneWay(reader,22,[15])),str(getPos(reader,[15,22])),str(getOneWay(reader,27,[13,15])),str(getPos(reader, [27,13])),str(getPos(reader, [27,15])),'0' ])



tableMaker('testingOut.csv', 'testingTable.csv')
#print getOneWay('testingOut.csv', 27)

	

