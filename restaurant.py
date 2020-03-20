class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name + " is the biggest " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is opening.")

    def number_served_reading(self):
        print("Have " + str(self.number_served) + " people eaten in here.")

    def set_number_served(self, reset_eaten_number):
        if reset_eaten_number >= 36:
            self.number_served = reset_eaten_number

        else:
            print("Your information not accurate !")

    def increment_number_served(self, increment_numbers):
        self.number_served += increment_numbers

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['草莓冰激凌', '坚果冰淇淋', '西瓜冰淇淋', '龙舌兰冰激凌']

    def read_icecream(self):
        for flavor in self.flavors:
            print(flavor)