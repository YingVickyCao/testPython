class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = self.make + ',' + self.model + "," + str(self.year)
        return long_name.title()

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def desc_type(self):
        print("Car")
