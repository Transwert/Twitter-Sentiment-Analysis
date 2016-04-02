import tweepy
import json
from pprint import pprint

import json
import urllib

key = 'UoOP5xpzbFqCLm3WKEq6VqhPY'
secret = 'RUPDwPP4cdYvCkfkuOZcX4OofCXcsZRcXxN6BUIoBkYTddVdCj'
auth = tweepy.OAuthHandler( key, secret)
auth.set_access_token( '715768598367715329-6QKfskhjRLrC6zmoIHllvL7SXISd522', 'RouBCcG7hHI4eA0MoaRtiGfX2nvFKoNEvrrAoczhttTGc')

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

api = tweepy.API(auth)
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)


		