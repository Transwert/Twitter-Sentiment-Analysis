import tweepy
import csv
import operator
import time
import get_all_tweets as gett
import get_followers as getf


auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token( access, a_secret)
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access, a_secret)
api = tweepy.API(auth)

# a function that takes in a series of media outlets and creates csv with the links to the articles
# they have posted on their twitter account
def get_site(media):
	for screen_name in media:
		# get the urls for articles from the New York Times and store them in a csv
		urls = gett.map_outlet_to_url([screen_name])[screen_name]
		urls = [s.decode('utf-8') for s in urls]
		#creates a csv file with all the links that were found in the nytimes feed
		gett.list_to_csv(urls, screen_name) 
#get_site(['nytimes', 'CNNPolitics'])

# function that returns a list with all the twitter posts of the followers of the account specified 
# by screen_name
# status: Works
def get_follower_statuses(screen_name):
	follower_tweets = []
	followers = getf.get_followers(screen_name)
	for person in followers:
		if person.protected != True:
			follower_tweets.extend(gett.get_all_tweets(person.screen_name))
	gett.list_to_csv(follower_tweets, screen_name) 

#create csv files with tweets from followers of Doanld Trump, Bernie Sanders, 
# Hillary Clinton, Ted Cruz and John Kasich

get_follower_statuses('realDonaldTrump')
get_follower_statuses('SenSanders')
get_follower_statuses('HillaryClinton')
get_follower_statuses('tedcruz')
get_follower_statuses('JohnKasich')



