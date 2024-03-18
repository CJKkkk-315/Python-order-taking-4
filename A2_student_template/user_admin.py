from user import User


class UserAdmin(User):
    def __init__(self, user_id=0, user_name='admin', user_password='password', user_role='AD', user_status='enabled'):
        super().__init__(user_id, user_name, user_password, user_role, user_status)

    def __str__(self):
        return super().__str__()

    def admin_menu(self):
        while True:
            print("\n1 Search user information")
            print("2 List all users’ information")
            print("3 List all units’ information")
            print("4 Enable/Disable user")
            print("5 Add user")
            print("6 Delete user")
            print("7 Log out")
            ipt = input("Please enter your selection: ")
            if ipt == "1":
                user_name = input("Please enter the username to search for: ")
                self.search_user(user_name)
            elif ipt == "2":
                self.list_all_users()
            elif ipt == "3":
                self.list_all_units()
            elif ipt == "4":
                user_name = input("Please enter the target username: ")
                self.enable_disable_user(user_name)
            elif ipt == "5":
                try:
                    self.__add_user()
                except:
                    print("Add failed, input data format incorrect")
            elif ipt == "6":
                user_name = input("Please enter the target username: ")
                self.delete_user(user_name)
            elif ipt == "7":
                print()
                break
            else:
                pass

    def __add_user(self):
        user_name = input("Please enter the username: ")
        user_password = input("Please enter the password: ")
        user_role = input("Please enter user role('AD'-admin, 'TA'-teacher, 'ST'-student): ")
        if user_role == "AD":
            obj = UserAdmin(user_name=user_name, user_password=user_password, user_role=user_role)
            self.add_user(obj)
        elif user_role == "TA":
            l = eval(input("Please enter the teach units list: "))
            from user_teacher import UserTeacher
            obj = UserTeacher(user_name=user_name, user_password=user_password, user_role=user_role, teach_units=l)
            self.add_user(obj)
        elif user_role == "ST":
            l = eval(input("Please enter the enrolled units list: "))
            from user_student import UserStudent
            obj = UserStudent(user_name=user_name, user_password=user_password, user_role=user_role, enrolled_units=l)
            self.add_user(obj)
            print("Successfully added")

    def search_user(self, user_name):
        """
        Display the information of the user found by the search
        """
        lst = self.get_users()
        for obj in lst:
            if obj.user_name == user_name:
                print(str(obj))
                break
        else:
            print("The user cannot be found")

    def list_all_users(self):
        """
        Display the information of all users currently stored in the system
        """
        lst = self.get_users()
        if lst:
            for obj in lst:
                print(obj)
        else:
            print("The user cannot be found")

    def list_all_units(self):
        """
        Display the information of all units currently stored in the system.
        """
        lst = self.get_units()
        if lst:
            for obj in lst:
                print(obj)
        else:
            print("No unit data found")

    def enable_disable_user(self, user_name):
        if self.check_username_exist(user_name):
            lst = self.get_users()
            for obj in lst:
                if obj.user_name == user_name:
                    if obj.user_status == "enabled":
                        obj.user_status = "disabled"
                    else:
                        obj.user_status = "enabled"
                    print("The status of user {} has been set to {}".format(user_name, obj.user_status))
            self.save_users(lst)
        else:
            print("The user cannot be found")

    def add_user(self, user_obj):
        """
        Add a user to the system. All the users should be persisted to the user.txt file.
        :param user_obj: An instance of the UserTeacher or UserStudent class
        """
        lst_obj = self.get_users()
        lst_obj.append(user_obj)
        self.save_users(lst_obj)

    def delete_user(self, user_name):
        if self.check_username_exist(user_name):
            lst_obj = self.get_users()
            for idx in range(len(lst_obj)):
                if lst_obj[idx].user_name == user_name:
                    del lst_obj[idx]
                    self.save_users(lst_obj)
                    print("Successfully deleted")
                    break
        else:
            print("The user cannot be found")
