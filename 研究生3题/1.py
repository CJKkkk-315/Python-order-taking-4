import random
ll = random.randint(500,3072)
start = 500
end = 3072
first = 0
back = 0
other = 0
idx = 1
while True:
    print(f'当前范围{start} - {end}')
    guess = int(input(f'{idx},请猜测流量：'))
    if guess == ll:
        if idx == 1:
            first = ll
        elif idx == 2:
            first = ll/2
            back = ll/2
        else:
            first = ll / 2
            other = ll/4/(idx-1)
            back = ll / 4
        break
    else:
        if guess > ll:
            end = guess
            print(f'{guess}高了')
        else:
            start = guess
            print(f'{guess}低了')
        idx += 1
for i in range(idx):
    if i == 0:
        print(f'第{i + 1}个人获得{int(first)}MB流量')
    elif i == idx-1:
        print(f'第{i + 1}个人获得{int(back)}MB流量')
    else:
        print(f'第{i + 1}个人获得{int(other)}MB流量')