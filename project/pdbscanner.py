"""
pdb scanner
"""

import sys
import os
import argparse

debug = False
attributesWin = {} #attributes of a winning hand
attributesLose = {} #attributes of losing hand
totalwinnings = {} #total winnings from hand
totalbets = {} #total bets on hand
profits = {} #total profitability of a hand

"""
Properly read in a file, splitting by line
"""
def fileLoader(file):

	data = file.read().split('\n')
	file.close()
	
	return data
"""
key 	     	timestamp of this hand (see HDB)
att 1     		number of player dealt cards
att 2	        position of player (starting at 1, in order of cards received)
bet    			total action of player during hand
winnings       	amount of pot won by player
card1		    pocket cards of player (if revealed at showdown)
card2
"""
def getAttributes(playerhands):

	global debug
	global attributesWin
	global attributesLose
	global totalwinnings
	global totalbets
	global profits

	for line in playerhands:
		playerdata = line.split()
		
		if(len(playerdata) == 0):
			break
		
		if (len(playerdata) > 11):
			key = playerdata[1]
			att1 = playerdata[2]
			att2 = playerdata[3]
			bet = int(playerdata[9])
			winnings = int(playerdata[10])
			
			card1 = list(playerdata[11])
			suit = card1[1]
			card1 = card1[0]
			card2 = list(playerdata[12])
			
			if suit == card2[1]:
				suit = 'suited'
			else:
				suit = 'not'
			card2 = card2[0]
			hand = (card1, card2, suit)
			if winnings > 0:
				attributesWin[key] = (att1, att2, hand)
			else:
				if key in attributesLose:
					x = attributesLose[key]
					x.append((att1, att2, hand))
				else:
					x = [(att1, att2, hand)]
				attributesLose[key] = x

			if hand in totalwinnings:
				x = totalwinnings[hand]
				winnings += x
			if hand in totalbets:
				y = totalbets[hand]
				bet += y
				
			
			totalbets[hand] = bet
			totalwinnings[hand] = winnings
			profits[hand] = float(winnings/bet)
				

def output(outfile):

	global debug
	

	outputwin(outfile)
	outputlose(outfile)
	
	outputbets(outfile)
	outputwinnings(outfile)
	outputprofits(outfile)
	
	
	outfile.close()
	
def outputwin(outfile):

	global attributesWin
	outfile.write("Attributes\n")
	outfile.write("Winners\n")
	for x, y in attributesWin.items():
		outfile.write("Timestamp: {0} - Dealt cards: {1} - Player Position: {2} - Hand: {3} {4} {5}\n".format(x, y[0], y[1], y[2][0], y[2][1], y[2][2]))
	
def outputlose(outfile):

	global attributesLose
	outfile.write("Losers\n")
	for x, y in attributesLose.items():
		for z in y:
			outfile.write("Timestamp: {0} - Dealt cards: {1} - Player Position: {2} - Hand: {3} {4} {5}\n".format(x, z[0], z[1], z[2][0], z[2][1], z[2][2]))
	
def outputbets(outfile):

	global totalbets

	for x, y in totalbets.items():
		outfile.write("Hand: {0} Total bets: {1}\n".format(x, y))

def outputwinnings(outfile):

	global totalwinnings

	for x, y in totalwinnings.items():
		outfile.write("Hand: {0} Total winnings: {1}\n".format(x, y))
	
def outputprofits(outfile):

	global profits
	
	for x, y in profits.items():
		outfile.write("Hand: {0} Profitability: {1}\n".format(x, y))
		
def outputrelationdata(outfile):

	global attributesLose
	global attributesWin
	global profits
	
	for x, y in attributesWin.items():
		hand = y[2]
		if hand[2] == 'suited':
			suited = 'yes'
		elif hand[2] == 'not':
			suited = 'no'
		profitability = profits[hand]
		outfile.write("{0},{1},{2},{3},{4},{5},{6}\n".format(y[0], y[1], profitability, hand[0], hand[1], suited, 'yes'))
	
	for x, y in attributesLose.items():
		for z in y:
			hand = z[2]
			if hand[2] == 'suited':
				suited = 'yes'
			elif hand[2] == 'not':
				suited = 'no'
			profitability = profits[hand]
			outfile.write("{0},{1},{2},{3},{4},{5},{6}\n".format(z[0], z[1], profitability, hand[0], hand[1], suited, 'no'))	
	

def main():

	global debug
	
	
	dir = 'C:/Users/marca/Documents/TextBooks/fall18/seng474/code474seng/project/poker'
	print("Reading files...")
	for room in os.listdir(dir):
		pdb = room+'/'
		room = dir+'/'+room
		for month in os.listdir(room):
			month = room+'/'+month
			pdb = month+'/pdb'
			print(month)
			for f in os.listdir(pdb):
				f = pdb+'/'+f

				print(f)
				if os.path.isdir(f):
					for h in os.listdir(f):
						h = f+'/'+h
						print(f)
						file = open(h, 'r')
						
				else:
					file = open(f, 'r')
					
				playerdata = fileLoader(file)
		
				getAttributes(playerdata)
		
			"""
			#outfile = 'C:/Users/marca/Documents/TextBooks/fall18/seng474/code474seng/project/playerdata/199504/199504data.txt'
			outwin =  month+'/winningHands.txt'
			outlose = month+'/losingHands.txt'
			outwin = open(outwin, 'w')
			outlose = open(outlose, 'w')
			outputwin(outwin)
			outwin.close()
			outputlose(outlose)
			outlose.close()
			
			#outfile = open(outfile, 'w')
			#output(outfile)
			"""
			
	outbets = 'C:/Users/marca/Documents/TextBooks/fall18/seng474/code474seng/project/playerdata/bets.txt'
	outwinnings = 'C:/Users/marca/Documents/TextBooks/fall18/seng474/code474seng/project/playerdata/winnings.txt'
	outprofit = 'C:/Users/marca/Documents/TextBooks/fall18/seng474/code474seng/project/playerdata/profits.txt'
	outweka = 'C:/Users/marca/Documents/TextBooks/fall18/seng474/code474seng/project/playerdata/class.txt'

			
	outbets = open(outbets, 'w')
	outwinnings = open(outwinnings, 'w')
	outprofit = open(outprofit, 'w')
	outweka = open(outweka, 'w')

	outputrelationdata(outweka)
	outweka.close()
	outputbets(outbets)
	outbets.close()
	outputwinnings(outwinnings)
	outwinnings.close()
	outputprofits(outprofit)
	outprofit.close()
	
	
if __name__ == '__main__':
	main()

	
	
	