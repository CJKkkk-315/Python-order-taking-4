import random
from user import User
from user_admin import UserAdmin
from user_teacher import UserTeacher
from user_student import UserStudent
from unit import Unit


def generate_test_data():
    f = open('data/user.txt','w')
    f.close()
    f = open('data/unit.txt', 'w')
    f.close()
    UserAdmin.add_user(UserAdmin(None,'admin',UserAdmin.encrypt('password'),'AD','enabled'))
    u1 = UserTeacher(None, 'u1', UserAdmin.encrypt('u1'), 'TA', 'enabled')
    u2 = UserTeacher(None, 'u2', UserAdmin.encrypt('u2'), 'TA', 'enabled')
    u3 = UserTeacher(None, 'u3', UserAdmin.encrypt('u3'), 'TA', 'enabled')
    k1 = Unit(None, 1111111, 'k1')
    k2 = Unit(None, 2222222, 'k2')
    k3 = Unit(None, 3333333, 'k3')
    UserAdmin.add_user(u1)
    UserAdmin.add_user(u2)
    UserAdmin.add_user(u3)
    u1.add_teach_unit(k1)
    u2.add_teach_unit(k2)
    u3.add_teach_unit(k3)
    s1 = UserStudent(None,'s1',UserAdmin.encrypt('s1'),'ST','enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    s2 = UserStudent(None, 's2', UserAdmin.encrypt('s2'), 'ST', 'enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    s3 = UserStudent(None, 's3', UserAdmin.encrypt('s3'), 'ST', 'enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    s4 = UserStudent(None, 's4', UserAdmin.encrypt('s4'), 'ST', 'enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    s5 = UserStudent(None, 's5', UserAdmin.encrypt('s5'), 'ST', 'enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    s6 = UserStudent(None, 's6', UserAdmin.encrypt('s6'), 'ST', 'enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    s7 = UserStudent(None, 's7', UserAdmin.encrypt('s7'), 'ST', 'enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    s8 = UserStudent(None, 's8', UserAdmin.encrypt('s8'), 'ST', 'enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    s9 = UserStudent(None, 's9', UserAdmin.encrypt('s9'), 'ST', 'enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    s10 = UserStudent(None, 's10', UserAdmin.encrypt('s10'), 'ST', 'enabled',[(1111111,-1),(2222222,-1),(3333333,-1)])
    UserAdmin.add_user(s1)
    UserAdmin.add_user(s2)
    UserAdmin.add_user(s3)
    UserAdmin.add_user(s4)
    UserAdmin.add_user(s5)
    UserAdmin.add_user(s6)
    UserAdmin.add_user(s7)
    UserAdmin.add_user(s8)
    UserAdmin.add_user(s9)
    UserAdmin.add_user(s10)

def main_menu(now_user):
    all_user = UserAdmin.read_user()
    if now_user.user_role == 'AD':
        while True:
            now_user.admin_menu()
            c = input()
            if c == '1':
                user_name = input('username:')
                now_user.search_name(user_name)
            elif c == '2':
                now_user.list_all_user()
            elif c == '3':
                now_user.list_all_unit()
            elif c == '4':
                user_name = input('user name:')
                now_user.enable_disable_user(user_name)
            elif c == '5':
                aod = input('add or delete:')
                if aod == 'add':
                    user_name = input('user name:')
                    password = UserAdmin.encrypt(input('password:'))
                    role = input('role:')
                    if role == 'AD':
                        now_user.add_user(UserAdmin(user_name=user_name, user_password=password, user_role=role))
                    if role == 'ST':
                        now_user.add_user(UserStudent(user_name=user_name, user_password=password, user_role=role))
                    if role == 'TA':
                        now_user.add_user(UserTeacher(user_name=user_name, user_password=password, user_role=role))
                else:
                    user_name = input('user name:')
                    for user in all_user:
                        if user.user_name == user_name:
                            now_user.delete_user(user_name)
            elif c == '6':
                print('Log Out!')
                break
            else:
                print('Error input!')
    elif now_user.user_role == 'ST':
        while True:
            now_user.student_menu()
            c = input()
            if c == '1':
                now_user.list_available_units()
            elif c == '2':
                now_user.list_enrolled_units()
            elif c == '3':
                aod = input('enrol or drop:')
                if aod == 'enrol':
                    unit_code = input('unit code:')
                    now_user.enrol_unit(unit_code)
                else:
                    unit_code = input('unit code:')
                    now_user.drop_unit(unit_code)
            elif c == '4':
                unit_code = input('unit code:')
                now_user.check_score(unit_code)
            elif c == '5':
                unit_code = input('unit code:')
                now_user.generate_score(unit_code)
            elif c == '6':
                print('Log Out!')
                break
            else:
                print('Error input!')
    else:
        while True:
            all_unit = Unit.read_unit()
            now_user.teacher_menu()
            c = input()
            if c == '1':
                now_user.list_teach_units()
            elif c == '2':
                unit_code = input('unit code:')
                aod = input('add or delete:')
                if aod == 'add':
                    now_user.add_teach_unit(Unit(unit_code=unit_code))
                else:
                    for unit in all_unit:
                        if unit.unit_code == unit_code:
                            now_user.delete_teach_unit(unit_code)
            elif c == '3':
                unit_code = input('unit code:')
                now_user.list_enrol_students(unit_code)
            elif c == '4':
                unit_code = input('unit code:')
                now_user.show_unit_avg_max_min_score(unit_code)
            elif c == '5':
                print('Log Out!')
                break
            else:
                print('Error input!')
def main():
    while True:
        flag = 0
        now_user = None
        while True:
            print("""
            Welcome!
            
            1.Log in
            2.Exit
            """)
            c = input()
            if c == '1':
                user_name = input("Please enter user name: ")
                user_password = UserAdmin.encrypt(input("Please enter user password: "))
                all_user = UserAdmin.read_user()
                for user in all_user:
                    if user.user_name == user_name and user.user_password == user_password:

                        now_user = user
                        if now_user.user_status == 'disabled':
                            break
                        print('Success!')
                        flag = 1
                        break
                if flag:
                    break
                print('username/password error or disabled login!')
            elif c == '2':
                exit(0)
            else:
                print('Error input!')
        main_menu(now_user)

generate_test_data()
main()

