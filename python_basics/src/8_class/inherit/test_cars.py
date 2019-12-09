from car import Car
from electric_car import ElectricCar


def test():
    car = Car("DaZhong", "module_1", 2016)
    print(car.get_descriptive_name())  # Dazhong,Module_1,2016

    electric_car = ElectricCar("DaZhong", "module_1", 2016)
    print(electric_car.get_descriptive_name())  # Dazhong,Module_1,2016

    electric_car.desc_battery()  # 70-kwh battery

    car.desc_type()  # Car
    electric_car.desc_type()  # Electric Car

    electric_car.battery.desc_battery()  # 70-kwh battery


test()
