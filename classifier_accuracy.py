import csv
from sentiment_analysis import classifier
from matplotlib import pyplot as plt
import random
import codecs


def both_sets(reader):
	#cross_validation_size = 0.5 * total_size
	#probability = cross_validation_size/total_size
	test_set = []
	training_data = []
	total_count = 0
	for row in reader:
		if random.random() < 0.5:
			test_set.append(row[1])
		training_data.append(row)
		total_count += 1
		

	return test_set, training_data, total_count

#def check_accuracy(fileName):

with codecs.open('training_set_better.csv', encoding='utf-8', errors='replace') as f:
	reader = csv.reader(f)


	percentage_list = []

	for i in range(0, 500):
		test_set, cross_validation_set, total_count = both_sets(reader)

		count_right = 0

		classify = classifier()

		for i in range(0, len(test_set)):
			if (test_set[i][0] == classify(cross_validation_set[i])):
				count_right += 1

		percent_right = count_right * 100
		percentage_list.append(percent_right)

	plt.hist(percentage_list)
	plt.show()

