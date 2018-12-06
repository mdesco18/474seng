"""
data_splitter.py
"""


import random
import os
import sys


def main():

	file = sys.argv[1]
	infile = os.path.abspath(file)
	
	with open(infile) as f:
		lines = f.readlines()
		
	hunnidk = [lines[i:i+2500000] for i in range(0,len(lines),2500000)]
	i = 0
	for group in hunnidk:
		i += 1
		outfile = 'playerdata/weka_samples/2point5milPoker'+str(i)+'.arff'
		outfile = open(outfile, 'w')
		outfile.write("@relation poker\n@attribute cards_dealt numeric\n@attribute player_position numeric\n@attribute profitability numeric\n@attribute card1 {2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A}\n@attribute card2 {2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A}\n@attribute suited {yes, no}\n@attribute win {yes, no}\n@data\n")
		
		for hand in group:
			outfile.write(hand)
			
	outfile.close()
	
	
if __name__ == '__main__':
	main()
