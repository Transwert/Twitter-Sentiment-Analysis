# script that takes in the trainning data from a Kaggle Competition in 2011 and puts it in the right
# format

import codecs
import csv

lst_sentiments = []
lst_posts = []
with codecs.open('training_raw.csv', encoding='utf-8', errors='replace') as f:
    reader = csv.reader(f)
    for row in reader:
    	lst_sentiments.append(row[0][0])
    	lst_posts.append(row[0][2:])
final_lst = zip(lst_sentiments, lst_posts)

with open('training_set.csv', 'w') as output:
	csv_writer = csv.writer(output)
	for row in final_lst:
		csv_writer.writerow(row)


        
