import csv
with open('Trump.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 0:
           print (row[0])
