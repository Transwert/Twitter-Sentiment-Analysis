from tweepy import StreamListener
import json, time, sys

class SListener(StreamListener):

    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.counter = 0
        self.tweets = open('vas.csv', 'w')

    def on_data(self, data):
        if  'in_reply_to_status' in data:
            self.on_status(data)

        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print (warning['message'])
            return false

    def on_status(self, status):
        data = json.loads(status)
        print(data['lang'])
        if data['text'] != None and data['lang'] == 'en':
            self.tweets.write(data['text'])
        self.counter += 1
        if self.counter >= 20000:
            self.tweets.close()
        return


    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 