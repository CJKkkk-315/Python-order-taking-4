def p3():
    # 定义递归函数
    def f(n):
        # 0！ = 1
        if n == 0:
            return 1
        else:
            # 递归调用
            return f(n-1) * n
    # 输出结果
    print(f(5))