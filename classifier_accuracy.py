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
	test_count = 0
	for row in reader:
		if random.random() < 0.2:
			if random.random() < 0.5:
				test_set.append(row)
				test_count += 1
			training_data.append(row)
			total_count += 1
		
	#print(total_count)
	return test_set, training_data, total_count, test_count

with codecs.open('training_set_better.csv', encoding='utf-8', errors='replace') as f:
	reader = csv.reader(f)


	percentage_list = []

	classify = classifier()


	for i in range(0, 500):
		test_set, training_data, total_count, test_count = both_sets(reader)

		count_right = 0

		print(total_count)
		if (test_count != 0):
			
			for i in range(0, test_count):
				if (test_set[i][0] == classify(test_set[i][1])):

					count_right += 1

			percent_right = (count_right/test_count) * 100
			percentage_list.append(percent_right)

	print(percentage_list)
	plt.hist(percentage_list, bins = 20)
	plt.show()

