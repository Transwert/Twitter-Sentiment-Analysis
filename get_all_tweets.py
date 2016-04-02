import tweepy
import csv


auth = tweepy.OAuthHandler( key, secret)
auth.set_access_token( access, a_secret)
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access, a_secret)
api = tweepy.API(auth)

#returns a list containing at most 2000 tweets from a particular person's timeline
def get_all_tweets(screen_name):
	tweets = []

	to_add = get_once(screen_name)

	for i in range(2):
		tweets.extend(to_add)
		if len(to_add) > 0:
			break
		to_add = get_once(screen_name)
	return tweets

def get_once(screen_name):
	text = [i.text for i in api.user_timeline(screen_name, count = 200)]
	return text

# converts the list from get_all_tweets to a csv
def list_to_csv(lst):
	out = open("tweets.csv", 'w')
	writer = csv.writer(out, dialect='excel')
	writer.writerow(lst)


