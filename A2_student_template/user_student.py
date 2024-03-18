import random
import user

class UserStudent(user.User):
    def __init__(self, user_id=0, user_name='', user_password='password', user_role='ST', user_status='enabled', enrolled_units=[]):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        # list of tuples (unit_code, score)). The score default is -1.
        self.enrolled_units = enrolled_units

    def __str__(self):
        return super().__str__() + ", {}".format(self.enrolled_units)

    def student_menu(self):
        while True:
            print("\n1 List all available units information")
            print("2 List all enrolled units")
            print("3 Enrol a unit")
            print("4 Drop a unit")
            print("5 Check the score of a unit")
            print("6 Generate score")
            print("7 Log out")
            ipt = input("Please enter your selection: ")
            if ipt == "1":
                self.list_available_units()
            elif ipt == "2":
                self.list_enrolled_units()
            elif ipt == "3":
                unit_code = input("Please enter the unit code: ")
                self.enrol_unit(unit_code)
            elif ipt == "4":
                unit_code = input("Please enter the unit code: ")
                self.drop_unit(unit_code)
            elif ipt == "5":
                unit_code = input("Please enter the unit code(enter '' check all the scores):")
                self.check_score(unit_code)
            elif ipt == "6":
                unit_code = input("Please enter the unit code: ")
                self.generate_score(unit_code)
            elif ipt == "7":
                print()
                break
            else:
                pass

    def list_available_units(self):
        """
        Display all the units that can be enrolled by the current student.
        """
        cnt = 0
        lst_obj = self.get_units()
        for obj in lst_obj:
            if obj.unit_code not in [x[0] for x in self.enrolled_units]:
                print(obj)
                cnt += 1
        if cnt == 0:
            print("No unit found")

    def list_enrolled_units(self):
        """
        Display all the units that the student enrolled.
        """
        cnt = 0
        lst_obj = self.get_units()
        for obj in lst_obj:
            if obj.unit_code in [x[0] for x in self.enrolled_units]:
                print(obj)
                cnt += 1
        if cnt == 0:
            print("No unit found")

    def enrol_unit(self, unit_code):
        """
        Enrol the current student into a unit.
        One student can enrol a maximum of 3 units and each unit has its own capacity.
        After enrollment, initialise the score as -1.
        """
        if len(self.enrolled_units) > 2:
            print("Enrol failed, One student can enrol a maximum of 3 units")
        elif not self.check_unit_code_exist(unit_code):
            print("Enrol failed, the unit code is not exists")
        elif unit_code in [x[0] for x in self.enrolled_units]:
            print("Enrol failed, You have enrolled the unit")
        else:
            cnt = 0
            for obj in self.get_users():
                if type(obj) == UserStudent and unit_code in [x[0] for x in obj.enrolled_units]:
                    cnt += 1
            cap = 0
            for obj in self.get_units():
                if obj.unit_code == unit_code:
                    cap = obj.unit_capacity
                    break
            if cnt < cap:
                lst_obj = self.get_users()
                for obj in lst_obj:
                    if obj.user_name == self.user_name:
                        obj.enrolled_units.append((unit_code, -1))
                        self.enrolled_units.append((unit_code, -1))
                        break
                self.save_users(lst_obj)
                print("Successfully enrolled")
            else:
                print("Enrol failed, The unit has reached its maximum capacity")

    def drop_unit(self, unit_code):
        """
        Remove the unit from the list of units in which the student is currently enrolled
        """
        if unit_code not in [x[0] for x in self.enrolled_units]:
            print("Drop failed, You did not enroll the unit")
        else:
            lst_obj = self.get_users()
            for obj in lst_obj:
                if obj.user_name == self.user_name:
                    for idx in range(len(obj.enrolled_units)):
                        if obj.enrolled_units[idx][0] == unit_code:
                            del obj.enrolled_units[idx]
                            del self.enrolled_units[idx]
                            break
            self.save_users(lst_obj)
            print("Successfully droped")

    def check_score(self, unit_code):
        """
        Display the unit score.
        """
        if unit_code:
            if unit_code not in [x[0] for x in self.enrolled_units]:
                print("You haven't enrolled the unit")
            else:
                for t in self.enrolled_units:
                    if t[0] == unit_code:
                        print("Score: {}".format(t[1]))
        else:
            for t in self.enrolled_units:
                print("Unit:{} Score:{}".format(t[0], t[1]))

    def generate_score(self, unit_code):
        if unit_code not in [x[0] for x in self.enrolled_units]:
            print("You haven't enrolled the unit")
        else:
            score = random.randint(0, 100)
            lst_obj = self.get_users()
            for obj in lst_obj:
                if obj.user_name == self.user_name:
                    for idx in range(len(obj.enrolled_units)):
                        if obj.enrolled_units[idx][0] == unit_code:
                            obj.enrolled_units[idx] = (unit_code, score)
                            self.enrolled_units[idx] = (unit_code, score)
                            print("The score for unit {} has been set to {}".format(unit_code, score))
                            break
            self.save_users(lst_obj)
