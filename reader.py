import csv
import re
from nltk.stem import WordNetLemmatizer


def getRelDeps(dep, noun, index):
	reldep = ''
	reldepleft = re.findall(r'(\S*\(%s-%d, \S*-[0-9]*\))' % (noun, index), dep)
	reldepright = re.findall(r'(\S*\(\S*-[0-9]*, %s-%d\))' % (noun, index), dep)
	for r in reldepleft:
		reldep += r + ' '
	for r in reldepright:
		reldep += r + ' '
	return reldep	

def getSentFrag(sent, index):
	arr = sent.split()
	if (index-6) < 0:
		startindex = 0
	else:
		startindex = index-6
	if (index+5) > len(arr):
		endindex = len(arr)
	else:
		endindex = index+5
	sentfragarr = arr[startindex:endindex]
	sentfrag = ' '.join(sentfragarr)
	return sentfrag

def getIndex(noun, tagged):
	count = 0
	#print tagged.split()
	for word in tagged.split():
		#print word
		count += 1
		if word.split('/')[0].lower() == 'dancing':
			return count
		else:
			pass
	return -1

with open('dancingIn.csv','rb') as f:
	reader = csv.reader(f)
	ofile = open('danceout.csv', 'wb')
	writer = csv.writer(ofile)
	deps = {}
	frags = {}

	
	header = True
	for row in reader:
		if header:
			header = False
		else:
			relDeps = getRelDeps(row[2],'dancing',getIndex('dancing',row[1]))
			#print getIndex('singing',row[1])
			frag = getSentFrag(row[0],getIndex('dancing',row[1]))
			#if 'singing/' not in row[1]:
			for dep in relDeps.split(' '):
				if '(' in dep:
					#print 'winner'
					deptype = dep.split('(')[0]
					if deptype in deps:
						deps[deptype] += 1
					else:
						deps[deptype] = 1
					if deptype in frags:
						frags[deptype].append(frag) 
					else:
						frags[deptype] =[frag]
										#print deptype
				

	for deptype in deps:
		row = [deptype,deps[deptype]]
		for frag in frags[deptype]:
			row.append(frag)
		writer.writerow(row)
		
