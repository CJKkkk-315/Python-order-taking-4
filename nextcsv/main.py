import csv
data = []
f = open('NameData.csv')
f_csv = csv.reader(f)
header = next(f_csv)
for i in f_csv:
    data.append(i)
f.close()
print(header)
for i in data:
    print(i)
