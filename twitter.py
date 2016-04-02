import tweepy
import csv


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

tweets = []
media_outlets = ['nytimes']

for _ in range(0,10):
	trump = []
	new_tweets = api.user_timeline(screen_name = 'FoxNews',count=200)

	trump.extend(new_tweets)

	for i in trump:
		if not "Trump" in i.text:
			trump.remove(i)

with open("fox_news_trump.csv", 'wb') as outcsv: 
	writer = csv.writer(outcsv)
	for val in trump:
		writer.writerow([1])






		