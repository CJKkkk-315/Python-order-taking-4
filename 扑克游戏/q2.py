def mapp(cards):
    decode_cards = []
    for j in cards:
        i = list(j)
        if i[0]== 'D':
            i[0] = 1
        elif i[0]== 'C':
            i[0] = 2
        elif i[0] == 'H':
            i[0] = 3
        elif i[0] == 'S':
            i[0] = 4
        if i[1] == 'T':
            i[1] = 10
        if i[1] == 'J':
            i[1] = 11
        if i[1] == 'Q':
            i[1] = 12
        if i[1] == 'K':
            i[1] = 13
        if i[1] == 'A':
            i[1] = 14
        decode_cards.append([int(i[1]),int(i[0])])
    return decode_cards


def unmap(cards):
    cards.sort(reverse=True)
    uncard = []
    for i in cards:
        i = i[::-1]
        if i[0]== 1:
            i[0] = 'D'
        elif i[0]== 2:
            i[0] = 'C'
        elif i[0] == 3:
            i[0] = 'H'
        elif i[0] == 4:
            i[0] = 'S'
        if i[1] == 10:
            i[1] = 'T'
        if i[1] == 11:
            i[1] = 'J'
        if i[1] == 12:
            i[1] = 'Q'
        if i[1] == 13:
            i[1] = 'K'
        if i[1] == 14:
            i[1] = 'A'
        uncard.append(''.join(list(map(str,i))))
    return uncard


def single(my_cards,att):
    for i in my_cards:
        if i[0] >= att[0] and i[1] >= att[1]:
            return [i]
    return False

def pair(my_cards,att):
    d = [[] for _ in range(15)]
    for i in my_cards:
        d[i[0]].append(i)
    for i in range(15):
        if len(d[i]) < 2:
            continue
        if i < att[0][0]:
            continue
        elif i == att[0][0]:
            if sorted(d[i])[0] > sorted(att)[1]:
                return d[i]
        elif i > att[0][0]:
            return sorted(d[i])[:2]
    return False

def three(my_cards,att):
    d = [[] for _ in range(15)]
    for i in my_cards:
        d[i[0]].append(i)
    for i in range(15):
        if len(d[i]) < 3:
            continue
        if i < att[0][0]:
            continue
        elif i > att[0][0]:
            return sorted(d[i])[:3]
    return False

def four(my_cards,att):
    d = [[] for _ in range(15)]
    for i in my_cards:
        d[i[0]].append(i)
    for i in range(15):
        if len(d[i]) < 4:
            continue
        if i < att[0][0]:
            continue
        elif i > att[0][0]:
            return sorted(d[i])[:4]
    return False
def fullhouse(my_cards,att):
    aw_my_cards = my_cards[::]
    ad = set()
    for i in att:
        ad.add(i[0])
    ad = list(ad)
    att1 = []
    att2 = []
    for j in att:
        if j[0] == ad[0]:
            att1.append(j)
        else:
            att2.append(j)
    if len(att1) == 3:
        att3 = att1 + att2
    else:
        att3 = att2 + att1
    res1 = three(aw_my_cards,att3[:3])
    if res1:
        for i in res1:
            aw_my_cards.remove(i)
        res2 = pair(aw_my_cards,att3[3:5])
        if res2:
            return res1 + res2
        else:
            return False
    else:
        return False
lost_flag = 0
res_print  = []
n,m = input().split(',')
n = int(n)
m = int(m)
my_cards = mapp(input().split(','))
my_cards.sort()
att_list = []
for i in range(n):
    att = mapp(input().split(','))
    att_list.append(att)
for i in range(n):
    if not my_cards:
        break
    att = att_list[i]
    if len(att) == 1:
        res = single(my_cards,att[0])
        if res:
            for j in res:
                my_cards.remove(j)
            res_print.append(unmap(res))
        else:
            res_print.append('Pass')
            m -= 1
    elif len(att) == 2:
        res = pair(my_cards, att)
        if res:
            for j in res:
                my_cards.remove(j)
            res_print.append(unmap(res))
        else:
            res_print.append('Pass')
            m -= 1
    elif len(att) == 3:
        res = three(my_cards, att)
        if res:
            for j in res:
                my_cards.remove(j)
            res_print.append(unmap(res))
        else:
            res_print.append('Pass')
            m -= 1
    elif len(att) == 4:
        res = four(my_cards, att)
        if res:
            for j in res:
                my_cards.remove(j)
            res_print.append(unmap(res))
        else:
            res_print.append('Pass')
            m -= 1
    elif len(att) == 5:
        res = fullhouse(my_cards, att)
        if res:
            for j in res:
                my_cards.remove(j)
            res_print.append(unmap(res[:3])+unmap(res[3:5]))
        else:
            res_print.append('Pass')
            m -= 1
    if m == 0:
        for p in res_print:
            print(p)
        print('Twisted Fate lost all his HP and lost.')
        lost_flag = 1
        break

if not lost_flag:
    for p in res_print:
        print(p)
    print(f'Twisted Fate won with {m}HP left.')

