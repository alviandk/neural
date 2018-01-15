import csv
with open('cluster3art.csv') as csvfile:
  reader=csv.reader(csvfile)
  l=[]
  for row in reader:
    l.append(int(row[0]))
  print(l)
