from tweepy import StreamListener
import json, time, sys, csv

class SListener(StreamListener):

    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.counter = 0
        self.tweets = open('Trump.csv', 'w')
        csv_writer = csv.writer(self.tweets)

    def on_data(self, data):
        if  'in_reply_to_status' in data:
            self.on_status(data)

        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print (warning['message'])
            return false

    def on_status(self, status):
        data = json.loads(status)
        if data['text'] != None and data['lang'] == 'en':
            csv_writer.writeRows(['blah'])
<<<<<<< HEAD
=======
            self.tweets.write(data['text'])
>>>>>>> 606b55c8e0e132c8069fee02f9e2af268ae43f3e
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