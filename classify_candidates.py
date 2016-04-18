#classify candidates
import csv
from sentiment_analysis import classifier

# test, try to classify trump and how the classifier is behaving
trump_posts = []
with open('Trump.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 0:
        	trump_posts.append(row[0])

classify = classifier()
positive_count = 0
negative_count = 0
for i in trump_posts:
	a = classify(i);
	if( a == '1'):
		positive_count += 1
	else:
		negative_count += 1
		
print("Trump:")
print("positive: " + str(positive_count))
print("negative: " + str(negative_count))
