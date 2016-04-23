import csv
import nltk
import process_tweet
import codecs

def read_csv(fileName):
	rows = []
	with codecs.open(fileName, encoding = 'utf-8', errors = 'replace') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        if len(row) > 0:
	           rows.append(row[0])
	return rows

#trump_data = read_csv('training_set.csv')

training_set, blabla = process_tweet.bulkFeatureExtraction('training_set.csv')

NBClassifier = nltk.NaiveBayesClassifier.train(training_set) #train the classifier on the training set
testTweet = 'Congrats @ravikiranj, i heard you wrote a new tech post on sentiment analysis'
processedTestTweet = process_tweet.processTweet(testTweet)
#print (NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet))))



