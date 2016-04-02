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
	for i in range(10):
		followers.extend(api.followers_ids(screen_name))
	return followers



