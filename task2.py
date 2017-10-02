
import csv
with open('Crime.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row)
