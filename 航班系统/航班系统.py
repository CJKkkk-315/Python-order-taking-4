import random


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class IteratorLinkList:
    def __init__(self, head):
        self.head = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is not None:
            return_value = self.head.value
            self.head = self.head.next
            return return_value
        else:
            raise StopIteration


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.length = 0

    def __iter__(self):
        return IteratorLinkList(self.head)

    def __len__(self):
        return self.length

    def append(self, new_data):

        new_node = Node(new_data, None)

        if self.length == 0:
            self.head = new_node
            self.length = 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node
            self.length += 1

    def remove(self, items):
        pre = None
        current = self.head

        if current.value == items:
            self.head = current.next
            return
        while current.next is not None:
            if current.data == items:
                pre.next = current.next
                return
            else:
                pre = current
                current = current.next


# 定义航班类
class Flight:
    # 初始化,需要终点站，航班号，飞机号，乘客定额，剩余票量参数
    def __init__(self, end_set, fid, pid, day, user_number, ticket_number):
        self.__end_set = end_set
        self.__fid = fid
        self.__pid = pid
        self.__day = day
        self.__user_number = user_number
        self.__ticket_number = ticket_number

    # 字符串结构化输出，方便将航班信息展示在界面上
    def __str__(self):
        return f'航班号:{self.__fid} 飞机号:{self.__pid} 终点站:{self.__end_set} 飞行周日:星期{self.__day} ' \
               f'乘员定额:{self.__user_number} 余票量:{self.__ticket_number}'

    # 检查传入的终点站是否与航班终点站一致
    def check_end_set(self, end_set):
        if end_set == self.__end_set:
            return True
        else:
            return False

    # 检查传入的航班号是否与该航班号一致
    def check_fid(self,fid):
        if fid == self.__fid:
            return True
        else:
            return False

    # 检查是否还有余票
    def check_ticket_number(self):
        if self.__ticket_number:
            return True
        else:
            return False

    # 减少余票
    def reduce_ticket(self):
        self.__ticket_number -= 1

    # 增加余票
    def up_ticket(self):
        self.__ticket_number += 1


# 定义用户类
class User:
    # 初始化,需要姓名，订票号，航班号，舱位等级
    def __init__(self, name, tid, fid, level):
        self.name = name
        self.tid = tid
        self.fid = fid
        self.level = level


# 定义候补类
class Alternate:
    # 初始化,需要姓名，航班号，舱位等级
    def __init__(self, name, fid, level):
        self.name = name
        self.fid = fid
        self.level = level


# 初始化航班列表
flight_l = [
    Flight('北京', 1, 1, 1, 2, 2),
    Flight('上海', 2, 2, 2, 5, 5),
    Flight('广州', 3, 3, 3, 5, 5),
    Flight('深圳', 4, 4, 4, 5, 5),
    Flight('北京', 5, 5, 5, 5, 5)
]
flight_list = LinkedList()
for i in flight_l:
    flight_list.append(i)
# 初始化用户列表
user_list = LinkedList()
# 初始化候补列表
alternate_list = LinkedList()


# 根据给定的fid，在列表中查到对应的航班实例对象
def select_flight_by_fid(fid):
    # 循环遍历
    for flight in flight_list:
        # 若航班号一致，则返回对应对象
        if flight.check_fid(fid):
            return flight
    # 没有找到则返回None
    return None


# 根据航班终点站查询所有对应的航班
def search_flight():
    end_set = input('请输入航班的终点站名:')
    res_list = []
    # 循环遍历所有航班
    for flight in flight_list:
        # 若终点站一致，则加入到最终列表中
        if flight.check_end_set(end_set):
            res_list.append(flight)
    # 打印出所有结果航班
    print('查询结果如下:')
    for flight in res_list:
        print(flight)


# 购票函数
def buy_ticket():
    # 用户输入姓名和航班号
    name = input('请输入你的姓名:')
    fid = int(input('请输入要订购航班的航班号:'))
    # 根据航班号获取航班对象
    target_flight = select_flight_by_fid(fid)
    # 检测是否正确
    if not target_flight:
        print('航班号错误！')
        return 0
    # 提示用户输入舱位等级
    while True:
        level = input('请输入要订购航班的舱位等级:')
        if level not in ['1', '2', '3']:
            print('舱位等级错误！请重新输入')
        else:
            break
    # 输出航班信息
    print('你要订购的航班为:')
    print(target_flight)
    # 检查是否还有余票
    if target_flight.check_ticket_number():
        # 随机生成订票号
        tid = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        print('订购成功！你的订票号为:', tid)
        # 将用户订单加入用户列表
        user_list.append(User(name, tid, fid, level))
        # 对饮航班余票减少
        target_flight.reduce_ticket()
    else:
        # 若无余票，则进入候补
        c = input('该航班已无余票！是否进入候补？(y/n):')
        if c == 'n':
            pass
        elif c == 'y':
            alternate_list.append(Alternate(name, fid, level))
            print('候补成功！')


# 检测是否有候补可以转正
def check_alternate(fid):
    # 遍历候补列表
    for alternate in alternate_list:
        # 若该航班存在候补
        if alternate.fid == fid:
            # 随机生成订票号
            tid = ''.join([str(random.randint(0, 9)) for _ in range(5)])
            # 添加到用户订单列表
            user_list.append(User(alternate.name, tid, alternate.fid, alternate.level))
            # 找到对应航班对象
            target_flight = select_flight_by_fid(fid)
            # 余票减一
            target_flight.reduce_ticket()
            # 从候补列表中删除
            alternate_list.remove(alternate)


# 退票函数
def refund_ticket():
    name = input('请输入你的姓名:')
    tid = input('请输入要退订的订票号:')
    flag = 1
    # 根据姓名和订票号寻找对应订单
    for user in user_list:
        if name == user.name and tid == user.tid:
            # 从订单列表中删除
            user_list.remove(user)
            print('退订成功！')
            flag = 0
            # 退订后，检查对应航班是否有候补
            target_flight = select_flight_by_fid(user.fid)
            target_flight.up_ticket()
            check_alternate(user.fid)
            break
    # 没有找到则输出信息
    if flag:
        print('没有该订单！')


# 菜单
m = """
航空订票系统

1.查询航线
2.订票业务
3.退票业务
4.退出

"""
# 读取用户输入，执行对应函数
while True:
    print(m)
    c = input('请输入选择：')
    if c == '1':
        search_flight()
    elif c == '2':
        buy_ticket()
    elif c == '3':
        refund_ticket()
    elif c == '4':
        exit(0)
    else:
        print('输入有误，请重新输入')

