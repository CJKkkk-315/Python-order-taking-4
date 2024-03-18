from user import User
from user_teacher import UserTeacher
from user_student import UserStudent
from unit import Unit
import random


class UserAdmin(User):

    def __init__(self, user_id=None, user_name='None', user_password='None', user_role='ST', user_status='enabled'):
        super().__init__(user_id, user_name, user_password, user_role, user_status)

    @staticmethod
    def admin_menu():
        print(
            """
            1○ Search user information
            2○ List all users’ information
            3○ List all units’ information
            4○ Enable/Disable user
            5○ Add/Delete user
            6○ Log out
            """
            )

    @staticmethod
    def search_name(user_name):
        all_user = UserAdmin.read_user()
        for user in all_user:
            if user.user_name == user_name:
                print(user)

    @staticmethod
    def list_all_user():
        all_user = UserAdmin.read_user()
        for user in all_user:
            print(user)

    @staticmethod
    def list_all_unit():
        all_unit = Unit.read_unit()
        for unit in all_unit:
            print(unit)

    @staticmethod
    def enable_disable_user(user_name):
        all_user = UserAdmin.read_user()
        for user in all_user:
            if user.user_name == user_name:
                if user.user_status == 'enabled':
                    user.user_status = 'disabled'
                else:
                    user.user_status = 'enabled'
        UserAdmin.write_user(all_user)

    @staticmethod
    def add_user(user):
        all_user = UserAdmin.read_user()
        all_user.append(user)
        UserAdmin.write_user(all_user)

    @staticmethod
    def delete_user(user_name):
        all_user = UserAdmin.read_user()
        for user in all_user:
            if user.user_name == user_name:
                all_user.remove(user)
                UserAdmin.write_user(all_user)
                print('Success!')
                return
        print('User not found!')

    @staticmethod
    def read_user():
        f = open('data/user.txt')
        all_user = []
        f_data = [i for i in f.read().split('\n') if i]
        for row in f_data:
            user = row.split(', ')
            if user[3] == 'AD':
                user_instance = UserAdmin(*user)
                all_user.append(user_instance)
            elif user[3] == 'ST':
                user = user[:5] + [eval(', '.join(user[5:]))]
                user_instance = UserStudent(*user)
                all_user.append(user_instance)
            else:
                user = user[:5] + [eval(', '.join(user[5:]))]
                user_instance = UserTeacher(*user)
                all_user.append(user_instance)
        f.close()
        return all_user

    @staticmethod
    def write_user(all_user):
        f = open('data/user.txt', 'w')
        for user in all_user:
            f.write(str(user) + '\n')
        f.close()
