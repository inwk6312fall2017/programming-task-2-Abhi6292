import csv

f = open("Crime.csv", 'rb')
reader = csv.reader(f) #reader object which iterates over a csv file(f)
headers = reader.next() #assign the first row to the headers variable
column = {} #list of columns
for h in headers: #for each header
    column[h] = []
for row in reader: #for each row in the reader object
    for h, v in zip(headers, row): #combine header names with row values (v) in a series of tuples
       column[h].append(v) 




