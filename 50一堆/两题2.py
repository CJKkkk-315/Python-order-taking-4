d = {}
while True:
    user_input = input()
    if not user_input:
        break
    a, b, c = user_input.split()
    b = int(b)
    c = int(c)
    if a not in d:
        d[a] = [0 for _ in range(12)]
    d[a][b-1] += c

for i in range(12):
    max_city = ''
    max_value = -1
    for k,v in d.items():
        if v[i] > max_value:
            max_city = k
            max_value = v[i]

    print(max_city,max_value)

max_city = ''
max_value = -1
for k,v in d.items():
    if sum(v) > max_value:
        max_city = k
        max_value = sum(v)
print(max_city,max_value)