import user
from unit import Unit


class UserTeacher(user.User):
    def __init__(self, user_id=0, user_name='', user_password='password', user_role='TA', user_status='enabled',
                 teach_units=[]):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        # A list of units code taught by the teacher
        self.teach_units = teach_units

    def __str__(self):
        return super().__str__() + ", {}".format(self.teach_units)

    def teacher_menu(self):
        while True:
            print("\n1 List all teaching units information")
            print("2 Add a unit")
            print("3 Delete a unit")
            print("4 List all students’ information and scores of one unit")
            print("5 Show the avg/max/min score of one unit")
            print("6 Log out")
            ipt = input("Please enter your selection: ")
            if ipt == "1":
                self.list_teach_units()
            elif ipt == "2":
                unit_code = input("Please enter the unit code: ")
                if self.check_unit_code_exist(unit_code):
                    obj = Unit(unit_code=unit_code)
                else:
                    unit_name = input("Please enter the unit name: ")
                    unit_capacity = int(input("Please enter the unit capacity: "))
                    obj = Unit(unit_code=unit_code, unit_name=unit_name, unit_capacity=unit_capacity)
                self.add_teach_unit(obj)
            elif ipt == "3":
                unit_code = input("Please enter the unit code: ")
                self.delete_teach_unit(unit_code)
            elif ipt == "4":
                unit_code = input("Please enter the unit code: ")
                self.list_enrol_students(unit_code)
            elif ipt == "5":
                unit_code = input("Please enter the unit code: ")
                self.show_unit_avg_max_min_score(unit_code)
            elif ipt == "6":
                print()
                break
            else:
                pass

    def list_teach_units(self):
        """
        Display the information of all units that are taught by the current teacher.
        """
        cnt = 0
        for obj in self.get_units():
            if obj.unit_code in self.teach_units:
                print(obj)
                cnt += 1
        if cnt == 0:
            print("No units taught by the teacher are found in the system")

    def add_teach_unit(self, unit_obj):
        """
        Add a new unit information to the data/unit.txt and
        add the unit_code in the current teacher's 'teach_units' list
        :param unit_obj: An instance of the Unit class
        """
        lst_obj = self.get_units()
        for obj in lst_obj:
            if obj.unit_code == unit_obj.unit_code:
                print("Unit code already exists")
                break
        else:
            lst_obj.append(unit_obj)
        self.save_units(lst_obj)

        lst_obj = self.get_users()
        for idx, obj in enumerate(lst_obj):
            if obj.user_name == self.user_name:
                if unit_obj.unit_code not in obj.teach_units:
                    lst_obj[idx].teach_units.append(unit_obj.unit_code)
                    self.teach_units.append(unit_obj.unit_code)
                    print("Successfully added")
                    break
        else:
            print("The teaching list already contains the unit code")
        self.save_users(lst_obj)

    def delete_teach_unit(self, unit_code):
        """
        Delete a unit from the current teacher's 'teach_units' list.
        If this unit has been enrolled by students, remove all associated enrollment records as well.
        """
        lst_obj = self.get_users()
        for obj in lst_obj:
            if obj.user_name == self.user_name:
                if unit_code in obj.teach_units:
                    obj.teach_units.remove(unit_code)
                    self.teach_units.remove(unit_code)
                    print("Successfully deleted")
                else:
                    print("Delete failed")
        self.save_users(lst_obj)

        from user_student import UserStudent
        lst_obj = self.get_users()
        for obj in lst_obj:
            if type(obj) == UserStudent:
                for idx in range(len(obj.enrolled_units)):
                    if obj.enrolled_units[idx][0] == unit_code:
                        del obj.enrolled_units[idx]
                        break
        self.save_users(lst_obj)

    def list_enrol_students(self, unit_code):
        """
        Display the information of all students currently enrolled in the unit.
        """
        cnt = 0
        from user_student import UserStudent
        for obj in self.get_users():
            if type(obj) == UserStudent:
                if unit_code in [x[0] for x in obj.enrolled_units]:
                    print(obj)
                    cnt += 1
        if cnt == 0:
            print("No students are found enrolled in the unit within the system")

    def show_unit_avg_max_min_score(self, unit_code):
        """
        Display the unit’s average, maximum and minimum score.
        """
        lst = []
        from user_student import UserStudent
        for obj in self.get_users():
            if type(obj) == UserStudent:
                for t in obj.enrolled_units:
                    if t[0] == unit_code:
                        lst.append(t[1])
        if lst:
            print("Average score: {:.2f}".format(sum(lst) / len(lst)))
            print("Maximum score: {:.2f}".format(max(lst)))
            print("Minimum score: {:.2f}".format(min(lst)))
        else:
            print("No student enrol this unit")
