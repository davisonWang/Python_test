import unittest
from your_money import Employee

class TestEmployeeSalary(unittest.TestCase):

    def setUp(self):
        self.my_salary = Employee('Donald', 'Trump')
        self.yearly_salary = 0
        self.salary = [5000, 12000]

    def test_give_default_raise(self):
        self.my_salary.give_raise()
        self.assertEqual(self.my_salary.yearly_salary, self.salary[0])

    def test_custom_raise(self):
        self.my_salary.give_custom_raise(self.salary[0])
        self.assertEqual(self.my_salary.yearly_salary, 5000)

        self.my_salary.give_custom_raise(self.salary[1])
        self.assertEqual(self.my_salary.yearly_salary, 17000)


unittest.main()


