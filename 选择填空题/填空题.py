import re
with open('填空题答案.txt',encoding='utf8') as f:
    data = [i.split('\t') for i in f.read().split('\n')]
with open('某同学考试卷.txt',encoding='utf8') as f:
    answer = [i.split('\t') for i in f.read().split('\n')]
data = [i for i in data[1:-1] if i]
qa = {}
for i in data:
    qa[i[0]] = i[1]
res = 0
for i in answer:
    print(i[0],end='')
    p1 = re.compile(r'[(](.*)[)]',re.S)
    q = '、'.join(re.sub("\(.*\)","()",i[0]).split('、')[1:])
    a = re.findall(p1,i[0])
    if qa[q] == a[0]:
        print('(√)')
        print('正确答案:',qa[q])
        res += 4
    else:
        print('(x)')
        print('正确答案:', qa[q])
print('最终得分为：',res)