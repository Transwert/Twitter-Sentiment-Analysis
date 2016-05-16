from listener import SListener
import time, tweepy, sys

## authentication
key="HfX9vtQ37LoGgcAnOigeqcqRs"
secret="VHT2CXZrIRvJQCVVKY8VaXFFr20NmQgWfAVeVeKij7Du4pfrIs"

access="703801335980773377-7tiks85kqBaeqd7jc0yxZzfBBEEGM2P"
a_secret="uwsceG85ug1jCeKeCi1Vab7q5zon1fRaB778qO8z5E5pk"

auth = tweepy.OAuthHandler( key, secret)
auth.set_access_token( access, a_secret)
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access, a_secret)
api = tweepy.API(auth)

def main():
    track = ['Sanders', 'sanders']
 
    listen = SListener(api, 'myprefix')
    stream = tweepy.Stream(auth, listen)

    print ("Streaming started...")

    try: 
        stream.filter(track = track)
    except:
        print ("error!")
        stream.disconnect()

if __name__ == '__main__':
    main()