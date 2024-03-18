class User:
    def __init__(self, user_id=0, user_name='', user_password='', user_role='ST', user_status='enabled'):
        if user_id:
            self.user_id = user_id
        else:
            self.user_id = self.generate_user_id()
        self.user_name = user_name
        if user_password.startswith('^^^') and user_password.endswith('$$$'):
            self.user_password = user_password
        else:
            self.user_password = self.encrypt(user_password)
        self.user_role = user_role
        self.user_status = user_status  # enabled disabled

    def __str__(self):
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}"

    def get_units(self):
        lst_obj = []
        with open('data/unit.txt', 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                if line:
                    obj = self.gen_unit_obj(line)
                    lst_obj.append(obj)
        return lst_obj

    def save_units(self, lst_obj):
        with open('data/unit.txt', 'w') as file:
            for obj in lst_obj:
                file.write(str(obj) + '\n')

    def gen_unit_obj(self, line):
        lst = line.split(', ')
        from unit import Unit
        return Unit(int(lst[0]), lst[1], lst[2], int(lst[3]))

    def get_users(self):
        lst_obj = []
        with open('data/user.txt', 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                if line:
                    obj = self.gen_user_obj(line)
                    lst_obj.append(obj)
        return lst_obj

    def save_users(self, lst_obj):
        with open('data/user.txt', 'w') as file:
            for obj in lst_obj:
                file.write(str(obj) + '\n')

    def gen_user_obj(self, line):
        if line.endswith(']'):
            idx = line.rfind('[')
            lst = line[:idx - 2].split(', ') + [eval(line[idx:])]
        else:
            lst = line.split(', ')
        if lst[3] == "AD":
            from user_admin import UserAdmin
            return UserAdmin(int(lst[0]), lst[1], lst[2], lst[3], lst[4])
        elif lst[3] == "TA":
            from user_teacher import UserTeacher
            return UserTeacher(int(lst[0]), lst[1], lst[2], lst[3], lst[4], lst[5])
        elif lst[3] == "ST":
            from user_student import UserStudent
            return UserStudent(int(lst[0]), lst[1], lst[2], lst[3], lst[4], lst[5])
        else:
            return None

    def generate_user_id(self):
        with open('data/user.txt', 'r') as file:
            lst = []
            for line in file:
                line = line.rstrip('\n')
                if line:
                    lst.append(int(line.split(', ')[0]))
            if lst:
                return max(lst) + 1
            else:
                return 10000

    def check_username_exist(self, user_name):
        with open('data/user.txt', 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                if line:
                    if line.split(', ')[1] == user_name:
                        return True
        return False

    def check_unit_code_exist(self, unit_code):
        with open('data/unit.txt', 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                if line:
                    if line.split(', ')[1] == unit_code:
                        return True
        return False

    def encrypt(self, user_password):
        str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@\^_`{|}~"
        result = ""
        for idx, c in enumerate(user_password):
            result += str_1[ord(c) % len(str_1)]
            result += str_2[idx % len(str_2)]
        result = "^^^" + result + "$$$"
        return result

    def login(self, user_name, user_password):
        """
        return a user information string (obtained from the “user.txt” file).
        If the user does not exist or their status is 'disabled', then return None.
        """
        with open('data/user.txt', 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                if line:
                    lst = line.split(', ')
                    if lst[1] == user_name and lst[2] == self.encrypt(user_password) and lst[4] == 'enabled':
                        return line
        return None


if __name__ == '__main__':
    usr = User()
    assert usr.encrypt('abcd1234') == "^^^J!K#L$M%X&Y(Z)1*$$$"
