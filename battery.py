class Battery():

    def __init__(self, battery_size = 175):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} kWh battery")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
