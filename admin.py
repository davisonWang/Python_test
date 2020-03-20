from user import User

class Privileges():
    def __init__(self):            # def __init__(self, privileges):去掉形参 privileges
        # self.privileges = privileges
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print("Administrator privileges : " + privilege.upper())


class Admin(User):
    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        # self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = Privileges()
