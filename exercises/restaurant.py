# Упражнение 9.1:
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def discribe_restaurant(self):
        print(f"Наш ресторан называется {self.restaurant_name} и имеет тип кухни - {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"Наш ресторан открыт! Рады гостям!")

my_restaurant = Restaurant('Токио', 'японская')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.discribe_restaurant()
my_restaurant.open_restaurant()