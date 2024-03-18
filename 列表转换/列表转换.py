input_list = [['1001','Kevin','2018Q1',202],['1002','Tony','2018Q1',367],['1003','Mary','2018Q1',402],['1004','Kevin','2018Q2',320],['1005','Tony','2018Q2',147],['1006','Mary','2018Q2',302],
['1007','Tony','2018Q3',234],['1008','Lucy','2018Q3',217],['1009','Kevin','2018Q3',159],['1010','Tony','2018Q4',213],['1011','Mary','2018Q4',289],['1012','Lucy','2018Q4',110]]

y = 2001
output_list = {}
for row in input_list:
    i = int(row[2][-1])
    k = row[1]
    try:
        output_list[k][i-1] = row[3]
    except:
        output_list[k] = [0,0,0,0]
        output_list[k][i-1] = row[3]
res = []
for i in output_list:
    res.append([y,i] + output_list[i][:])
    y += 1
with open('res.csv','w',newline='') as f:
    f.write('Codenew,Name,Cost2018Q1,Cost2018Q2,Cost2018Q3,Cost2018Q4\n')
    for i in res:
        f.write(','.join(list(map(str,i)))+'\n')
