import math
n = 1
while True:
    if n*math.log(n,2)/60000 > 60:
        print(n)
        break
    n += 1


n = 50000000
t = n**2/25000000 / 60 / 60 / 24 / 365
print(t)