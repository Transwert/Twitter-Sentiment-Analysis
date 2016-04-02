import tweepy
import csv
import operator
import time
import get_all_tweets


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

#returns a list of user objects that are following the account with the particular screen_name
def get_followers(screen_name):
	followers = []
	for i in range(1):
		followers.extend(api.followers(screen_name))
	return followers

#returns a list of user ids (integers) objects that are following the account with the particular screen_name
def get_followers_id(screen_name):
	followers_id = []
	for i in range(1):
		lst = [i.id for i in api.followers(screen_name)]
		followers_id.extend(lst)
	return followers_id

lst = get_followers('J_tsar')
print(len(lst))
s = set()
for i in lst:
	s.add(i)
print(len(lst))


