from user import User

from unit import Unit


class UserTeacher(User):

    def __init__(self, user_id=None, user_name='None', user_password='None', user_role='ST', user_status='enabled', teach_units=[]):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.teach_units = teach_units

    def __str__(self):
        return super().__str__() + ', ' + str(self.teach_units)

    @staticmethod
    def teacher_menu():
        print("""
        1○ List all teaching units information
        2○ Add/Delete a unit
        3○ List all students’ information and scores of one unit
        4○ Show the avg/max/min score of one unit
        5○ Log out
        """)

    def list_teach_units(self):
        from user_admin import UserAdmin
        all_unit = Unit.read_unit()
        if not self.teach_units:
            print('t no units taught by the teacher are found in the system')
        for unit in self.teach_units:
            for u in all_unit:
                if str(u.unit_code) == str(unit):
                    print(u)

    def add_teach_unit(self, unit):
        from user_admin import UserAdmin
        self.teach_units.append(unit.unit_code)
        all_unit = Unit.read_unit()
        all_unit.append(unit)
        Unit.write_unit(all_unit)
        all_user = UserAdmin.read_user()
        for user in all_user:
            if user.user_name == self.user_name:
                user.teach_units.append(unit.unit_code)
        UserAdmin.write_user(all_user)

    @staticmethod
    def delete_teach_unit(unit_code):
        all_unit = Unit.read_unit()
        for unit in all_unit:
            if str(unit.unit_code) == str(unit_code):
                all_unit.remove(unit)
                Unit.write_unit(all_unit)
                print('Success!')
                return
        print('Unit not found!')

    @staticmethod
    def list_enrol_students(unit_code):
        from user_admin import UserAdmin
        all_user = UserAdmin.read_user()
        for user in all_user:
            if user.user_role == 'ST':
                for enrolled in user.enrolled_units:
                    if str(unit_code) == str(enrolled[0]):
                        print(user)
                        break

    @staticmethod
    def show_unit_avg_max_min_score(unit_code):
        from user_admin import UserAdmin
        all_user = UserAdmin.read_user()
        max_score = -2
        min_score = 1000
        scores = []
        for user in all_user:
            if user.user_role == 'ST':
                for enrolled in user.enrolled_units:
                    if str(unit_code) == str(enrolled[0]):
                        max_score = max(max_score, enrolled[1])
                        min_score = min(min_score, enrolled[1])
                        scores.append(enrolled[1])
        print("max score:", max_score)
        print("min score:", min_score)
        print("avg score:", sum(scores)/len(scores))

