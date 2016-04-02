import tweepy
import csv
import operator

#override tweepy.StreamListener to add logic to on_status
key = 'UoOP5xpzbFqCLm3WKEq6VqhPY'
secret = 'RUPDwPP4cdYvCkfkuOZcX4OofCXcsZRcXxN6BUIoBkYTddVdCj'
access = '715768598367715329-6QKfskhjRLrC6zmoIHllvL7SXISd522'
a_secret = 'RouBCcG7hHI4eA0MoaRtiGfX2nvFKoNEvrrAoczhttTGc'

auth = tweepy.OAuthHandler( key, secret)
auth.set_access_token( access, a_secret)
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access, a_secret)
api = tweepy.API(auth)

def split_text(tweet):
	sentence = tweet.split()
	return sentence 

def get_trump():
	media = ['nytimes', 'CNN', 'cnnbrk', 'CNNPolitics', 'cnni']
	tweets = []
	for m in media:
		new_tweets = api.user_timeline(screen_name = m,count=200)
		for i in new_tweets:
			if "Trump" in i.text or "trump" in i.text:
				tweets.append(i)
	print(len(tweets))
	return tweets

trump_data = get_trump()

d = {}

for tweet in trump_data:
d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(d)









		