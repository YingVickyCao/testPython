class Battery:
    def __init__(self, battery_sizes=70):
        self.battery_size = battery_sizes

    def desc_battery(self):
        print(str(self.battery_size) + '-kwh battery')