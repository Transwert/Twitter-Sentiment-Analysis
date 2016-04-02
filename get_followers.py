import tweepy
import csv
import operator
import time


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


def get_followers(screen_name):
	followers = []
	for i in range(25):
		followers.extend(api.followers(screen_name))
	return followers

def get_followers_id(screen_name):
	followers_id = []
	for i in range(25):
		lst = [i.id for i in api.followers(screen_name)]
		followers_id.extend(lst)
	return followers_id

def split_text(tweet):
	sentence = tweet.split()
	return sentence 

def find_url(tweet):
	t = split_text(tweet)
	for word in t:
		if word[0:7] == "https://":
			url = word
	return url
print(find_url('https://t.co/0o1jI5yDZd jhdhsf sjhshdj sdhsjdjhsdd jshdhsd sdhjsdh'))

