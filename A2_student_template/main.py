import random
from unit import Unit
from user import User
from user_admin import UserAdmin
from user_teacher import UserTeacher
from user_student import UserStudent


def main_menu():
    print('1 Login')
    print('2 Exit')


def generate_test_data():
    """
    generate test data for the program
    """
    with open('data/unit.txt', 'w') as file:
        file.write("")
    lst_obj = []
    for unit_name in ['Python', 'C++', 'Java']:
        obj = Unit(unit_code='FIT{}'.format(random.randint(1000, 9999)), unit_name=unit_name,
                   unit_capacity=random.randint(2, 5))
        lst_obj.append(obj)
        with open('data/unit.txt', 'a') as file:
            file.write(str(obj) + '\n')

    with open('data/user.txt', 'w') as file:
        obj = UserAdmin()
        file.write(str(obj) + '\n')

    for x in range(3):
        with open('data/user.txt', 'a') as file:
            obj = UserTeacher(user_name=f'teacher{x + 1}', teach_units=[lst_obj[x].unit_code])
            file.write(str(obj) + '\n')

    for x in range(10):
        with open('data/user.txt', 'a') as file:
            unit_code = random.choice([x.unit_code for x in lst_obj])
            obj = UserStudent(user_name=f'student{x + 1}', enrolled_units=[(unit_code, -1)])
            file.write(str(obj) + '\n')


def main():
    try:
        generate_test_data()
    except:
        print("An error occurred while writing to the file. Please check if you have sufficient write permissions")
    else:
        while True:
            main_menu()
            ipt = input("Please enter your selection: ")
            if ipt == "1":
                user_name = input("Please enter user name: ")
                user_password = input("Please enter user password: ")
                usr = User()
                res = usr.login(user_name, user_password)
                if res:
                    obj = usr.gen_user_obj(res)
                    if type(obj) == UserAdmin:
                        obj.admin_menu()
                    elif type(obj) == UserTeacher:
                        obj.teacher_menu()
                    elif type(obj) == UserStudent:
                        obj.student_menu()
                else:
                    print("\nIncorrect username or password\n")
            elif ipt == "2":
                break
            else:
                print("\nYour selection is not available\n")


if __name__ == "__main__":
    main()
