class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        return full_name.title()

    def greet_user(self):
        print(self.describe_user() + " nice to meet you !")

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

    def reading_login_attempts(self):
        print("Attempt login times: " + str(self.login_attempts))









