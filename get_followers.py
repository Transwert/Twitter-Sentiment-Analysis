import tweepy
import csv
import operator
import time


#override tweepy.StreamListener to add logic to on_status


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



