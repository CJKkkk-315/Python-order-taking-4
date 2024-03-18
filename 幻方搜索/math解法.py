import numpy as np  # 导入NumPy库


def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Only odd order magic squares are supported.")

    magic_square = np.zeros((n, n), dtype=int)  # 创建一个 n x n 的二维数组，初始值全为0

    i, j = 0, n // 2  # 开始的位置在第一行中间

    for num in range(1, n ** 2 + 1):
        magic_square[i, j] = num  # 将当前的数字放到当前的位置
        i_next, j_next = (i - 1) % n, (j + 1) % n  # 向右上方移动
        if magic_square[i_next, j_next]:  # 如果下一个位置已经被占用
            i += 1  # 向下移动
        else:
            i, j = i_next, j_next  # 否则更新位置

    return magic_square


n = 5  # 幻方的大小
magic_square = generate_magic_square(n)

# 打印出幻方
print("Magic Square for n =", n)
print("Sum of each row or column", n * (n ** 2 + 1) // 2, "\n")
print(magic_square)
