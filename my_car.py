"""从模块car导入Car"""
# from car import Car
#
# my_new_car = Car('BMW', 'X7', 2020)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.odometer_reading = 23
# my_new_car.reading_odometer()

#-----------------------------------------------------------------------------------------------------------------------

# from car import Car, ElectricCar
#
# """
# 从一个模块中导入多个 类 时，用 逗号 分隔了各个类。导入必要的类后，就可根据需要
# 创建每个类的任意数量的实例。
# """
#
# my_beetle = Car('volkswagen', 'beetle', 2020)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = ElectricCar('tesla', 'roadster', 2021)
# print(my_tesla.get_descriptive_name())

#=======================================================================================================================

# import car
#
# my_beetle = car.Car('volkswagen', 'beetle', 2020)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = car.ElectricCar('tesla', 'roadster', 2021)
# print(my_tesla.get_descriptive_name())

#_______________________________________________________________________________________________________________________

from car import Car
from my_electric import ElectricCar

my_car = Car('volkswagen', 'beetle', 2020)
print(my_car.get_descriptive_name())

my_electric = ElectricCar('tesla', 'roadster', 2021)
print(my_electric.get_descriptive_name())
my_electric.battery.describe_battery()
my_electric.battery.get_range()













