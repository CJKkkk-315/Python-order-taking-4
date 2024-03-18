"""
MATH20621 - Mini test 2
Student name: add your name
Student id:   add your id number
Student mail: your.name@student.manchester.ac.uk
"""

# Feel free to add other functions you find useful.

# Problem 1
def nested(p1, p2):
    """
    add a docstring
    """
    try:
        p1_list = []
        for i in p1.split(', '):
            p1_list.append(float(i))
        p2_list = []
        for i in p2.split(', '):
            p2_list.append(float(i))
    except:
        raise TypeError
    for i in p1_list:
        for j in p2_list:
            if i == j:
                return None
    p2_list.sort()
    p2_flag = [0 for _ in range(len(p2_list))]
    for i in p1_list:
        for j in range(len(p2_list)-1):
            if p2_list[j] < i < p2_list[j+1]:
                p2_flag[j] += 1
    for i in p2_flag:
        if i > 1:
            return False
    return True

# Problem 2
def len_count(s):
    """
    add a docstring
    """
    s = s.lower().replace(',','').replace('.','').split(' ')
    d = {}
    for i in s:
        d[len(i)] = d.get(len(i),0) + 1
    d = [(i,j) for i,j in d.items()]
    d.sort(key=lambda x:[x[1],x[0]],reverse=True)
    return d

# Problem 3
def transpose(L):
    """
    add a docstring
    """
    l = [len(i) for i in L]
    s = set()
    for i in l:
        s.add(i)
    if len(s) != 1:
        raise IndexError
    for i in L:
        for j in i:
            if not isinstance(j,int):
                raise ValueError
    LT = [[] for _ in range(len(L[0]))]
    for i in range(len(L[0])):
        for j in range(len(L)):
            LT[i].append(L[j][i])
    return LT

# main() function for all the testing
def main():
    # do your testing here, for example
    print("should return True:", nested("-13.11, 7.5", "17.19, 23.31, 1.41"))
main() # call main() function to run all tests