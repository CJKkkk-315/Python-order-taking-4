class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


class Student(Person):
    def __init__(self,name,age,sex,python,c):
        Person.__init__(self,name,age,sex)
        self.python = python
        self.c = c
        self.m = ''
    def show(self):
        f = lambda x,y:(x+y)/2
        score = f(self.c,self.python)
        print(f'最终成绩为：{score} 专业为：{self.m}')

    def major(self,m):
        self.m = m

s = Student('张三',18,'男',100,90)
s.major('计算机')
s.show()
