import tweepy
import csv

key = 'UoOP5xpzbFqCLm3WKEq6VqhPY'
secret = 'RUPDwPP4cdYvCkfkuOZcX4OofCXcsZRcXxN6BUIoBkYTddVdCj'
access = '715768598367715329-6QKfskhjRLrC6zmoIHllvL7SXISd522'
a_secret = 'RouBCcG7hHI4eA0MoaRtiGfX2nvFKoNEvrrAoczhttTGc'

auth = tweepy.OAuthHandler( key, secret)
auth.set_access_token( access, a_secret)
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access, a_secret)
api = tweepy.API(auth)

#returns a list containing at most 2000 tweets from a particular person's timeline
#return format: list of strings
# status: Working
def get_all_tweets(screen_name):
	tweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200) 

	tweets.extend(new_tweets)

	if len(tweets) > 0:
			last_tweet = tweets[-1].id - 1
	count = 0
	while len(new_tweets) > 0 and count < 10: 
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=last_tweet)
		tweets.extend(new_tweets)
		if len(tweets) > 0:
			last_tweet = tweets[-1].id - 1
		count += 1
	tweets = [tweet.text.encode("utf-8") for tweet in tweets]
	return tweets


# maps media outlet's screen_name to a list of urls
# info will be used to do sentiment analysis on the article of that link
# status: working
def map_outlet_to_url(lst):
	d = {}
	for media in lst:
		tweets = get_all_tweets(media) 
		tweets = split_text(tweets)
		urls = find_url(tweets)
		d[media] = urls
	return d

# returns a list of all the urls that appears in the list of tweets
def find_url(tweet):
	lst = []
	for word in tweet:
		if word[0:8] == b'https://':
			lst.append(word)
	return lst
# returns a split version of the text into one big array for ease of use
def split_text(tweets):
	words = []
	for i in tweets:
		for j in i.split():
			words.append(j)
	return words 

# converts the list of strings and puts them in a csv file
def list_to_csv(lst, name):
	out = open(name + "_tweets.csv", 'w')
	writer = csv.writer(out, dialect='excel')
	writer.writerow(lst)


