b = eval(input())
l = eval(input())
for i in l:
    b = b[:i][::-1] + b[i:]
print(b)
flag = 0
for i in range(1,len(b)):
    if b[i] <= b[i-1]:
        flag = 1
        break
if flag:
    print('No')
else:
    print('Yes')
