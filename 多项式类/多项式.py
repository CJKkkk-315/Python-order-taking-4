"""
多项式中的n次项系数对应列表中索引为n的数值
例如：
P = 2 + 3x + 4x^2 + 6x^4
对应coefficients_列表为 [2, 3, 4, 0, 6]
"""


class Polynomial:
    # 初始化系数列表
    def __init__(self, coefficients_):
        self.coefficients_ = coefficients_

    # 阶数即为系数列表长度-1
    def get_order(self):
        return len(self.coefficients_) - 1

    # 先将新系数列表长度设置为两个多项式中较长的一项，然后循环两个多项式，加到新多项式中，然后实例化返回
    def add(self, p):
        n = max(len(self.coefficients_), len(p.coefficients_))
        new_coefficients_ = [0 for i in range(n)]
        for i in range(len(self.coefficients_)):
            new_coefficients_[i] += self.coefficients_[i]
        for i in range(len(p.coefficients_)):
            new_coefficients_[i] += p.coefficients_[i]
        return Polynomial(new_coefficients_)

    # 求一阶导，将每一项降低一阶并且乘以它本来的阶数
    def get_first_derivative(self):
        n = len(self.coefficients_)
        new_coefficients_ = [0 for i in range(n)]
        for i in range(1, len(self.coefficients_)):
            new_coefficients_[i - 1] = i * self.coefficients_[i]
        del new_coefficients_[-1]
        return Polynomial(new_coefficients_)

    # 求一阶积分，将每一项升高一阶并且÷以它本来的阶数
    def get_antiderivative(self, c):
        n = len(self.coefficients_)
        new_coefficients_ = [0 for i in range(n)]
        for i in range(len(self.coefficients_)):
            new_coefficients_[i] = 1 / (i + 1) * self.coefficients_[i]
        new_coefficients_.insert(0, c)
        return Polynomial(new_coefficients_)

    # 简单的拼接字符串输出即可
    def __str__(self):
        r = ''
        if self.coefficients_[0]:
            r += str(self.coefficients_[0])
        for i in range(1,len(self.coefficients_)):
            if i != len(self.coefficients_):
                if self.coefficients_[i] > 0 and r:
                    r += '+'
            if self.coefficients_[i]:
                if i == 1:
                    if self.coefficients_[i] == 1:
                        r += 'x'
                    elif self.coefficients_[i] == -1:
                        r += '-x'
                    else:
                        r += str(self.coefficients_[i]) + 'x'
                else:
                    if self.coefficients_[i] == 1:
                        r += 'x^' + str(i)
                    elif self.coefficients_[i] == -1:
                        r += '-x^' + str(i)
                    else:
                        r += str(self.coefficients_[i]) + 'x^' + str(i)
        r = 'P(x) = ' + r
        return r


if __name__ == '__main__':
    a = [2, 0, 4, -1, 0, 6]
    b = [-1, -3, 0, 4.5]
    Pa = Polynomial(a)
    Pb = Polynomial(b)
    print(Pa.get_order())
    print(Pa.add(Pb))
    Pa = Pa.get_first_derivative()
    print(Pa)
    Pa = Pa.get_antiderivative(2)
    print(Pa)