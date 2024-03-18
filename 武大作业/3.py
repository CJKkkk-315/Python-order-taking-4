import re
s = ''.join([i.replace('\n',' ') for i in open('filein.c').readlines()])
ret_1 = re.findall('/\*(.*?)\*/', s)

ss = 0
for i in ret_1:
    ss += len(i)
print(str(int(ss/len(s)*100))+'%')
