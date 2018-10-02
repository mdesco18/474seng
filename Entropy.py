"""
Entropy.py
Calculate entropy (information gain) for attributes to construct ID3 tree
Input attribute probabilities at command line
"""

import math
import sys

def entropy(attr):
	e = 0
	
	for a in attr:
		e -= a*(math.log2(a))
		
	return e
	
def main():

	
	attr = [float(x) for x in sys.argv[1:]]
	z = sum(attr)
	
	if z != 1:
		print("\nError: sum of attribute probability != 1")
		print("Sum: {}".format(z))
		s = "Margin of error: "
		if z > 1:
			x = str(z-1)
		else:
			x = str(1-z)
		s += x
		print(s+'\n')
			
		
	e = entropy(attr)
	print(e)


if __name__ == "__main__":

	main()