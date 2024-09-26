from car import Car

my_car = Car('audi', 'a4', 2019)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 100
my_car.update_odometer(156)
print(my_car.odometer_reading)

my_car.increment_odometer(50)
print(my_car.odometer_reading)