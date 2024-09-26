# Упражнение 9.6

from restaurant import Restaurant

class IseCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = ['ванильное', 'шоколадное', 'мятное']

    def get_flavor_type(self):
        print(f"В ресторане продают следующие виды мороженного:\n* {self.flavor[0]}\n* {self.flavor[1]}\n* {self.flavor[2]}")


ise_restaurant = IseCreamStand('Чудеса', 'ресторан мороженного')
ise_restaurant.discribe_restaurant()
ise_restaurant.get_flavor_type()