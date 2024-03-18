from unit import Unit
import random


class User:

    def __init__(self, user_id=None, user_name='None', user_password='None', user_role='ST', user_status='enabled'):
        if user_id is None:
            user_id = self.generate_user_id()
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_status = user_status

    def __str__(self):
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}"

    @staticmethod
    def generate_user_id():
        from user_admin import UserAdmin
        all_user = UserAdmin.read_user()
        user_id = str(random.randint(10000,99999))
        while user_id in [i.user_id for i in all_user]:
            user_id = str(random.randint(10000, 99999))
        return user_id

    @staticmethod
    def check_username_exist(user_name):
        from user_admin import UserAdmin
        all_user = UserAdmin.read_user()
        if user_name not in [i.user_name for i in all_user]:
            return False
        else:
            return True

    @staticmethod
    def encrypt(user_password):
        import time
        str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@\^_`{|}~"
        res = ""
        for i in user_password:
            res += str_1[ord(i) % len(str_1)]
            res += str_2[ord(i) % len(str_2)]
        return "^^^" + res + "$$$"

    @staticmethod
    def login(user_name, user_password):
        from user_admin import UserAdmin
        all_user = UserAdmin.read_user()
        for user in all_user:
            if user.user_name == user_name and user.user_password == user_password:
                if user.user_status == 'disabled':
                    return None
                else:
                    return str(User(*user[:6]))
        return None


