from car import Car
from battery import Battery

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(75)

    def fill_gas_tank(self):
        print(f"This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesls', 'model s', 2019)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()