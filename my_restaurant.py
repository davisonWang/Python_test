from restaurant import Restaurant

my_restaurant = Restaurant('全聚德', 'traditional chinese dish')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served_reading()

my_restaurant.set_number_served(27)
my_restaurant.number_served_reading()

my_restaurant.set_number_served(37)
my_restaurant.number_served_reading()

my_restaurant.increment_number_served(6)
my_restaurant.number_served_reading()