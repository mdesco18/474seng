README.md NaiveBayes.py

Author: Marc-Andre Descoteaux
Student: V00847029 mdesco18@uvic.ca
Project: SENG474 a1

This program is designed as an implementation for the data mining practice of Naive Bayes Text Classification using the Multinomial or Bernouilli model.

	usage: NaiveBayes.py [-h] [-m] [-b] [-id TRAINDATA] [-il TRAINLABEL]
                     [-td TESTDATA] [-tl TESTLABEL] [-D] [-o [OUTFILE]]

	Take in files

	optional arguments:
	  -h, --help            show this help message and exit
	  -m, --multi           use the multinomial model
	  -b, --bernie          use the bernoulli model
	  -id TRAINDATA, --traindata TRAINDATA
							the train data
	  -il TRAINLABEL, --trainlabel TRAINLABEL
							the test labels
	  -td TESTDATA, --testdata TESTDATA
							the test data
	  -tl TESTLABEL, --testlabel TESTLABEL
							the test labels
	  -D, --debug           the debugging argument
	  -o [OUTFILE], --outfile [OUTFILE]
							the outfile
							
	Implements NaiveBayesAccuracy.py
	
	usage: NaiveBayesAccuracy.py [-h] [-r RESULTS] [-t TESTLABEL] [-D]
                             [-o [OUTFILE]]

	Take in files

	optional arguments:
	  -h, --help            show this help message and exit
	  -r RESULTS, --results RESULTS
							the results from NaiveBayes
	  -t TESTLABEL, --testlabel TESTLABEL
							the test labels
	  -D, --debug           the debugging argument
	  -o [OUTFILE], --outfile [OUTFILE]
							the outfile

