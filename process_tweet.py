import re
from langdetect import detect
import csv

class processTweet(object):


    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        self.fileName = 


    #def filterEnglish(lists): #filters out words that are not in English
    #	return [tweet for tweet in lists if detect(tweet) == 'en']

    def processTweet(tweet):
    	#Convert to lower case
        tweet = tweet.lower()
        tweet.decode('utf-8')
        #Convert www.* or https?://* to URL
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
        #Convert @username to AT_USER
        tweet = re.sub('@[^\s]+','AT_USER',tweet)
        #Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)
        #Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        #trim
        tweet = tweet.strip('\'"')
        return tweet


    def handleRepeatedLetters(s):
        #look for 2 or more repetitions of character and replace with 1 repetition of the character itself
        pattern = re.compile(r"(.)\1{2,}", re.DOTALL)
        return pattern.sub(r"\1\1", s)

    def stopWords(file):
        stopWords = []
        stopWords.append('AT_USER')
        stopWords.append('URL')
        fp = open(file, 'r')
        for line in fp.readline():
            word = line.strip()
            stopWords.append(word)
        fp.close()
        return stopWords

    def getFeatureVector(tweet):
        featureVector = []
        #split tweet into words
        words = tweet.split()
        for w in words:
            #replace more than two with two occurrences
            w = handleRepeatedLetters(w)
            #strip punctuation
            w = w.strip('\'"?,.')
            #check if the word stats with an alphabet
            val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            #ignore if it is a stop word
            if(w in stopWords or val is None):
                continue
            else:
                featureVector.append(w.lower())
        return featureVector


    def extract_features(tweet):
        tweet_words = set(tweet)
        features = {}
        for word in featureList:
            features['contains(e%s)' % word] = (word in tweet_words)
        return features

    def bulkFeatureExtraction(file):
        #file = file.decode('utf-8')

        stopwordsList = []

        with open(file, 'r') as f:
            reader = csv.reader(f)
            #your_list = list(reader)
            for row in reader:
                tweet = row[1]
                sentiment = row[0]
                processedTweet = processTweet(tweet)
                featureVector = getFeatureVector(processedTweet, stopWordsList)
                featureList.extend(featureVector)
                tweets.append((featureVector, sentiment))


        #inpTweets = csv.reader(open(file, 'r'))
        stopWordsList = stopWords('stopwords.txt')
        featureList = []
        tweets = []

        #inpTweets = list(inpTweets)
        #[tweet.decode('utf-8') for tweet in inpTweets]

        
    	# Remove featureList duplicates
        featureList = list(set(featureList))

    	# Extract feature vector for all tweets in one shote
        training_set = nltk.classify.util.apply_features(extract_features, tweets)
        print(training_set)

    def addTweetsToDict(fileName):

        tweets_dictionary = {} #HashMap<String, Integer> 

        with open(file, 'r') as f:
            reader = csv.reader(f)
            
            for row in reader:
                tweet = row[1]
                sentiment = row[0]
                tweets_dictionary[tweet] = sentiment

        return tweets_dictionary



'''def plot():
	labels = 'Positive', 'Negative'
	sizes = [.34, .66]
	colors = ['yellowgreen', 'mediumpurple', 'lightskyblue', 'lightcoral'] 
	explode = (0, 0.1)    # proportion with which to offset each wedge

	plt.pie(sizes,              # data
	        explode=explode,    # offset parameters 
	        labels=labels,      # slice labels
	        colors=colors,      # array of colours
	        autopct='%1.1f%%',  # print the values inside the wedges
	        shadow=True, enable shadow
	        startangle=70       # starting angle
	        )
	plt.axis('equal')
	plt.savefig('trump.png')'''
