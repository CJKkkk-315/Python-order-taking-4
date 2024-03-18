import csv
data = []
with open('VZFixedIncomeCleanSong.csv') as f:
    f_csv = csv.reader(f)
    header = next(f_csv)
    for row in f_csv:
        data.append(row)
new_header = [header[0],header[5],header[9],header[10],header[11]]
new_data = []
for row in data:
    new_data.append([row[0],row[5],row[9],row[10],row[11]])
with open('new_file','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(new_header)
    for i in new_data:
        f_csv.writerow(i)