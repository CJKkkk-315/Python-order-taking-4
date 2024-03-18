n = int(input())
s = []
ss = []
for i in range(n):
    name,score = input().split()
    score = int(score)
    ss.append(score)
    if score in ss:
        score -= 0.0001*ss.count(score)
    s.append([score,name])
s.sort()
for i in s[::-1]:
    print('{:>15}{:>5}'.format(i[1],round(i[0])))