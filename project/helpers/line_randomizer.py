"""
line_randomizer.py
"""

import random
import os
import sys

def main():

	file = sys.argv[1]
	file = os.path.abspath(file)
	
	with open(file) as f:
		lines = f.readlines()
	random.shuffle(lines)
	
	with open("outfile.txt", "w") as f:
		f.writelines(lines)
		
	
if __name__ == '__main__':
	main()
