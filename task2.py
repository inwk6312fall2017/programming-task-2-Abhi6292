
import csv
with open('Crime.csv') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
     print(row[1])
