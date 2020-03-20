class Employee():

    def __init__(self, first_name, last_name, ):
        self.first_name = first_name
        self.last_name = last_name
        self.yearly_salary = 0

    def show_full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        print(full_name)

    def give_raise(self, raise_number=5000):
        self.yearly_salary += raise_number
        print(self.yearly_salary)

    def give_custom_raise(self, raise_custom_number=''):
        self.yearly_salary += raise_custom_number
        print(self.yearly_salary)


# my_money = Employee('Donald', 'Trump')
# my_money.show_full_name()
# my_money.give_raise()
# my_money.give_custom_raise(7000)