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
        self.iter_head = self.head
        self.length = 0

    def __iter__(self):
        self.iter_head = self.head
        return self

    def __next__(self):
        if self.iter_head is not None:
            return_value = self.iter_head.value
            self.iter_head = self.iter_head.next
            return return_value
        else:
            raise StopIteration

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

for i in flight_list:
    print(i)