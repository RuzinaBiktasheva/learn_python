# Упражнение 9.4:
from restaurant import Restaurant

your_restaurant = Restaurant('Piter', 'восточная')
print(your_restaurant.number_served)

your_restaurant.number_served = 10
print(your_restaurant.number_served)

print(your_restaurant.set_number_served())

print(your_restaurant.increment_number_served(70))