import tweepy
import csv
import operator
import time
import get_all_tweets as get


key = 'UoOP5xpzbFqCLm3WKEq6VqhPY'
secret = 'RUPDwPP4cdYvCkfkuOZcX4OofCXcsZRcXxN6BUIoBkYTddVdCj'
access = '715768598367715329-6QKfskhjRLrC6zmoIHllvL7SXISd522'
a_secret = 'RouBCcG7hHI4eA0MoaRtiGfX2nvFKoNEvrrAoczhttTGc'

auth = tweepy.OAuthHandler( key, secret)
auth.set_access_token( access, a_secret)
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access, a_secret)
api = tweepy.API(auth)

# get the urls for articles from the New York Times and store them in a csv
nytimes_urls = get.map_outlet_to_url(['nytimes'])['nytimes']
nytimes_urls = [s.decode('utf-8') for s in nytimes_urls]

get.list_to_csv(nytimes_urls, 'nytimes') #creates a csv file with all the links that were found in the nytimes feed





