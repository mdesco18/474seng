"""
NaiveBayes.py
Author: Marc-Andre Descoteaux
Student: V00847029 mdesco18@uvic.ca
Project: SENG474 a1
"""

import sys
import argparse
import math
import numpy as np
import collections

global debug

"""
Properly read in a file, splitting by line
"""
def fileLoader(file):

	data = file.read().split('\n')
	file.close()
	
	return data
"""
Create a mapping of classes to data
"""
def classSeperator(data, labels):

	map = {}
	
	for i in range(len(data)):
		if labels[i] not in map:
			map[labels[i]] = []
		map[labels[i]].append(data[i])
	return map
"""
Extract the documents from the dataset
"""
def extractData(docs):

	words = []
	for doc in docs:
		d = doc.split()
		words += d
	return words
	
def extractDataFromDoc(docs):

	return docs.split(" ")
"""
Use the training data with the multinomialModel
"""
def trainingM(classes, traindata):

	global debug 
	text = {}
	words = []
	N = 0
	docNum = {}
	prior = {}
	condprob = {}
	T = {}
	vocab = []
	unique = {}
	
	
	words = extractData(traindata)
	if debug:
		print(words)
	N = sum([len(classes[c]) for c in classes])
	
	for t in words:
		if t not in unique:
			unique[t] = 1
			condprob[t] = {}
		else:
			unique[t] += 1
		
	
	vocab = list(unique.keys())
	vocab.sort()
	if debug:
		print(vocab)
		print(unique)
	
	for c in classes:
		text[c] = extractData(classes[c])
		docNum[c] = len(classes[c])	
		""" Using sentences or words as the 'documents' is negligible probability difference
		docNum[c] = len(text[c])
		N = len(words)
		"""
		prior[c] = docNum[c] / N
		if debug: 
			print(len(classes[c]))
			print(len(text[c]))
			print(N)
			print(prior[c])
		T[c] = {}
		
		
		for t in text[c]:
			if t not in T[c]:
				T[c][t] = 1
			else:
				T[c][t] += 1
		if debug:
			print(T[c])
			print(len(T[c]))
	
	
	if debug:
		print(len(text[c]))
		print(len(words))
		print(len(vocab))
	for c in classes:
		for t in vocab:
			if t not in T[c]:
				T[c][t] = 0
			condprob[t][c] = (T[c][t] + 1) / (len(text[c]) + len(vocab))
	
	if debug:
		print(condprob)
		
	
	return vocab, prior, condprob
"""
Apply the multinomialModel on the testdata
"""
def applyM(classes, vocab, prior, condprob, docs):

	global debug
	
	score = {}
	array = []
	key = []
	words = extractDataFromDoc(docs)
	
	if debug:
		print(words)
	for c in classes:
		key.append(c)
		score[c] = np.log(prior[c])
		if debug:
			print(score[c])
		for t in words:
			if t in vocab:
				if debug:
					print(condprob[t][c])
				score[c] += np.log(condprob[t][c])
			
		if debug:
			print(score[c])
		array.append(score[c])
	
	if debug:
		print(array)
	cmap = np.argmax(array)
	return key[cmap]
	
	
	
	
"""
Compute NaiveBayes with the multinomialModel
"""
def multinomialModel(classes, traindata, testdata):

	result = ""
	words, prior, condprob = trainingM(classes, traindata)
	
	for doc in testdata:
		cla = applyM(classes, words, prior, condprob, doc)
		result += str(cla) + '\n'
		
		if debug:
			print(doc)
			print(cmap)
			
	return result
	
def main():

	global debug
	
	"""
	Using ArgumentParser to take in files from command line arguments
	"""
	parser = argparse.ArgumentParser(prog='NaiveBayes.py',description='Take in files')
	parser.add_argument('-m', '--multi', dest='multinomial', action='store_true', default= False, help='use the multinomial model')
	parser.add_argument('-b', '--bernie', dest='bernoulli', action='store_true', default= False, help='use the bernoulli model')
	parser.add_argument('-id', '--traindata', dest='traindata', nargs=1, type=argparse.FileType('r'), help='the train data')
	parser.add_argument('-il', '--trainlabel', dest='trainlabel', nargs=1, type=argparse.FileType('r'), help='the test labels')
	parser.add_argument('-td', '--testdata', dest='testdata', nargs=1, type=argparse.FileType('r'), help='the test data')
	parser.add_argument('-tl', '--testlabel', dest='testlabel', nargs=1, type=argparse.FileType('r'), help='the test labels')
	parser.add_argument('-D', '--debug', dest='debug', action='store_true', default= False, help='the debugging argument')
	parser.add_argument('-o', '--outfile', dest='outfile', nargs='?', type=argparse.FileType('w'),  default= sys.stdout, help='the outfile')
	args = parser.parse_args()
	#parser.print_help()

	"""
	Gather objects from sys.args namespace
	"""
	multinomial = args.multinomial
	bernoulli = args.bernoulli
	debug = args.debug
	outfile = args.outfile
	
	if debug:
		sys.stdout = outfile
	
	traindata = fileLoader(args.traindata[0])
	trainlabel = fileLoader(args.trainlabel[0])
	classes = classSeperator(traindata, trainlabel)
	testdata = fileLoader(args.testdata[0])
	if multinomial:
		result = multinomialModel(classes, traindata, testdata)
	elif bernoulli:
		result = bernoulliModel(classes, traindata, testdata)
	else:
		print("Improper Usage")
	
	outfile.write(result)
	outfile.close()

	
if __name__ == '__main__':
	main()
