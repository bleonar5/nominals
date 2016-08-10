
def getSubj(tagged, noun, index):
	split = tagged.split(' ')
	nsubj = []
	i = 0
	for word in split:
		if noun in word:
			if 'NN' in split[i - 1]:
				nsubj = split[i-1]
		i += 1 
	return nsubj