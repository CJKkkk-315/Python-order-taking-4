s = [i.replace('\n',' ').replace('.',' ').replace(',',' ') for i in open('crossin.txt').readlines()]
d = {}
for i in range(len(s)):
    endl = {}
    t = s[i].split()
    for j in range(len(t)):
        if t[j].replace('-','a').isalpha() and t[j][0] != '-' and t[j] not in ['a','an','the','and']:
            if t[j] in d:
                if t[j] in endl:
                    d[t[j]].append([i+1,s[i].find(t[j],endl[t[j]])+1])
                else:
                    d[t[j]].append([i + 1, s[i].find(t[j]) + 1])
            else:
                d[t[j]] = [[i+1,s[i].find(t[j])+1]]
            endl[t[j]] = d[t[j]][-1][1]+len(t[j])
d = [[i]+j for i,j in d.items()]
d.sort()
with open('crossout.txt','w') as f:
    for i in d:
        f.write(i[0]+':')
        tt = ','.join([f'({j[0]},{j[1]})' for j in sorted(i[1:])])
        f.write(tt+'\n')
