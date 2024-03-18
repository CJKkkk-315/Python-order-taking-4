from user import User
from unit import Unit
import random


class UserStudent(User):

    def __init__(self, user_id=None, user_name='None', user_password='None', user_role='ST', user_status='enabled', enrolled_units=[]):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.enrolled_units = enrolled_units

    def __str__(self):
        return super().__str__() + ', ' + str(self.enrolled_units)

    @staticmethod
    def student_menu():
        print("""
            1○ List all available units information
            2○ List all enrolled units, each students can enrol maximum 3 units
            3○ Enrol/Drop a unit
            4○ Check the score of a unit
            5○ Generate score
            6○ Log out
            """)

    def list_available_units(self):
        all_unit = Unit.read_unit()
        all_code = [str(i[0]) for i in self.enrolled_units]
        for unit in all_unit:
            if str(unit.unit_code) not in all_code:
                print(unit)

    def list_enrolled_units(self):
        all_unit = Unit.read_unit()
        all_code = [str(i[0]) for i in self.enrolled_units]
        for unit in all_unit:
            if str(unit.unit_code) in all_code:
                print(unit)

    def enrol_unit(self, unit_code):
        from user_admin import UserAdmin
        if len(self.enrolled_units) == 3:
            print('One student can enrol a maximum of 3 units!')
            return
        all_unit = Unit.read_unit()
        all_user = UserAdmin.read_user()
        for unit in all_unit:
            if str(unit.unit_code) == str(unit_code):
                if unit.unit_capacity:
                    unit.unit_capacity = int(unit.unit_capacity) - 1
                    self.enrolled_units.append((unit_code, -1))
                else:
                    print('No capacity!')
                    return
        for user in all_user:
            if str(user.user_id) == str(self.user_id) and user.user_role == 'ST':
                user.enrolled_units.append((unit_code, -1))
                break
        UserAdmin.write_user(all_user)
        Unit.write_unit(all_unit)
        print('Success!')

    def drop_unit(self, unit_code):
        from user_admin import UserAdmin
        all_user = UserAdmin.read_user()
        for unit in self.enrolled_units:
            if str(unit[0]) == str(unit_code):
                self.enrolled_units.remove(unit)
                break
        for user in all_user:
            if str(user.user_id) == str(self.user_id) and user.user_role == 'ST':
                for unit in user.enrolled_units:
                    if str(unit[0]) == str(unit_code):
                        user.enrolled_units.remove(unit)
                        break
        UserAdmin.write_user(all_user)
        print('Success!')

    def check_score(self, unit_code):
        for unit in self.enrolled_units:
            if str(unit[0]) == str(unit_code) or not unit_code:
                print(unit[0],unit[1])

    def generate_score(self, unit_code):
        from user_admin import UserAdmin
        for unit in self.enrolled_units:
            if str(unit[0]) == str(unit_code):
                new_score = random.randint(1,100)
                new_unit = (unit[0],new_score)
                self.enrolled_units.remove(unit)
                self.enrolled_units.append(new_unit)
                break
        all_user = UserAdmin.read_user()
        for user in all_user:
            if str(user.user_id) == str(self.user_id) and user.user_role == 'ST':
                for unit in user.enrolled_units:
                    if str(unit[0]) == str(unit_code):
                        new_unit = (unit[0], new_score)
                        user.enrolled_units.remove(unit)
                        user.enrolled_units.append(new_unit)
                        print(new_score)
                        UserAdmin.write_user(all_user)
                        print('Success!')
                        return





