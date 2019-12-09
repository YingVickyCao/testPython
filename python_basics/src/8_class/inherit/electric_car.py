from car import Car
from battery import Battery


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Python 2.7
        # super(ElectricCar, self).__init__(make, model, year)

        # 将实例用作属性
        self.battery_size = 70
        # 将实例用作属性：提取类
        self.battery = Battery()

    def desc_battery(self):
        print(str(self.battery_size) + '-kwh battery')

    # 重写父类的方法
    def desc_type(self):
        print("Electric Car")
