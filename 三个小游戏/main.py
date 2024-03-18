# 引入需要的函数
from p1 import p1
from p2 import p2
from p3 import p3
# 屏幕输出文本
print("欢迎来到小游戏课堂:")
print("请输入数字选择不同的小游戏∶")
print("1∶输出100以内所有偶数")
print("2∶输出100以内所有偶数合")
print("3∶求5的阶乘")
# 读取用户输入
c = int(input())

# 调用不同函数

def main(c1):
    if c1 == 1:
        p1()
    elif c1 == 2:
        p2()
    elif c1 == 3:
        p3()


main(c)
