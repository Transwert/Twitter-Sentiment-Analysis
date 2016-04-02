from langdetect import detect

def filter_english(lists):
	return [tweet for tweet in lists if detect(tweet) == 'en']