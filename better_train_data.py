# this is a script that takes in two training sets, one for positive and one for negative data 
# It converts the two in a single csv file with 2 columns, one with 0s and 1s and another one with 
# the actual post
import json
import csv

# retuns a list of dictionaries each of which is a tweet given a filename
def get_data_dict(filename):
    with open(filename, 'r') as infile:
        tweets = []
        for line in infile:
            json_dict = json.loads(line)
            tweets.append(json_dict)
    return tweets

positive_tweets = get_data_dict('Training_Data/training_negative_tweets.json')
negative_tweets = get_data_dict('Training_Data/training_positive_tweets.json')

positive_text = []
for tweet in positive_tweets:
    positive_text.append(tweet['text'])

negative_text = []
for tweet in negative_tweets:
    negative_text.append(tweet['text'])

binary_positive = [1 for i in range(len(positive_text))]
binary_negative = [0 for i in range(len(negative_text))]

final_lst = list(zip(binary_positive, positive_text))
final_lst.extend(zip(binary_negative, negative_text))

with open('Training_Data/training_set_better.csv', 'w') as output:
    csv_writer = csv.writer(output)
    for row in final_lst:
        csv_writer.writerow(row)




