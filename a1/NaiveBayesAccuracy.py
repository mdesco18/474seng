"""
NaiveBayesAccuracy.py
Author: Marc-Andre Descoteaux
"""

import sys
import argparse

global debug

"""
Properly read in a file, splitting by line
"""
def fileLoader(file):

	data = file.read().split('\n')
	file.close()
	
	return data

"""
Count occurrences of class 0 in file
"""
def counter0(list):
	count = 0
	for l in list:
		if l == '0':
			count += 1
			
	return count
		
"""
Count occurrences of class 1 in file
""" 
def counter1(list):
	count = 0
	for l in list:
		if l == '1':
			count += 1
			
	return count
		
"""
Determine accuracy by class
"""
def classPercent(r0, t0, r1, t1):

	if r0 < t0:
		x = r0 / t0 * 100
	else:
		x = t0 / r0 * 100
	if r1 < t1:
		y = r1 / t1 * 100
	else: 
		y = t1 / r1 * 100
		
	print("Accuracy for class 0 is {0}%".format(x))
	print("Accuracy for class 1 is {0}%".format(y))

"""
interface for NaiveBayes
@return the accuracy percentage of the NaiveBayes implementation for all classes
"""
def fromNB(results, test):
	
	correct = 0
	for i in range(len(results)):
		if results[i] == test[i]:
			correct += 1
	percent = correct / len(results) * 100
	
	return percent
	
	
"""
Run from command line. Unit Test
"""
def main():

	global debug
	
	"""
	Using ArgumentParser to take in files from command line arguments
	"""
	parser = argparse.ArgumentParser(prog='NaiveBayesAccuracy.py',description='Take in files')
	parser.add_argument('-r', '--results', dest='results', nargs=1, type=argparse.FileType('r'), help='the results from NaiveBayes')
	parser.add_argument('-t', '--testlabel', dest='testlabel', nargs=1, type=argparse.FileType('r'), help='the test labels')
	parser.add_argument('-D', '--debug', dest='debug', action='store_true', default= False, help='the debugging argument')
	parser.add_argument('-o', '--outfile', dest='outfile', nargs='?', type=argparse.FileType('w'),  default= sys.stdout, help='the outfile')
	args = parser.parse_args()
	parser.print_help()
	
	results = fileLoader(args.results[0])
	test = fileLoader(args.testlabel[0])
	debug = args.debug
	outfile = args.outfile
	
	if debug:
		print(results)
		print(test)
	
	r0 = counter0(results)
	t0 = counter0(test)
	r1 = counter1(results)
	t1 = counter1(test)
	
	classPercent(r0, t0, r1, t1)

if __name__ == "__main__":

	main()