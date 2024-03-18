def p2():
    res = 0
    # 循环100内所有数
    for i in range(100):
        # 判断是否为偶数
        if i%2 == 0:
            # 累加到结果中
            res += i
    print(res)