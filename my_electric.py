# from car import ElectricCar
#
# my_tesla = ElectricCar('tesla', 'model s', 2020)
#
# print(my_tesla.get_descriptive_name())
#
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
#

from car import Car
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        if self.battery_size == 70:
            range= 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on full charge."
        print(message)

class ElectricCar(Car):
    """模拟电动车的独特之处"""

    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()



