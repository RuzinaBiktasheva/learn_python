# Упражнения 9.1 и 9.4:
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def discribe_restaurant(self):
        print(f"Наш ресторан называется {self.restaurant_name} и имеет тип кухни - {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"Наш ресторан открыт! Рады гостям!")

    def set_number_served(self):
        print(f"Количество посетителей: {self.number_served}.")

    def increment_number_served(self, number):
        self.number_served += number
        print(f"Количество посетителей изменилось и стало: {self.number_served}.")