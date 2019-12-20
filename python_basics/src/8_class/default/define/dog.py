from test_method import hi


class Dog:
    # 如果不继承，省略()
    # class Dog():

    # Python 2.7
    # class Dog(object):

    # 与类相关联的方法调用都会自动传入实参 self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法.self会自传递，不需要传递它
    # 方法 __init__()不显式包含return语句，Python 自动返回一个实例
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 给属性设置默认值
        self.type_name = 'normal'

    def sit(self):
        print(self.name + " is sitting.")

    def roll_over(self):
        print(self.name + " had rolled over")

    def get_name(self):
        return self.name

    def get_type_name(self):
        return self.type_name

    def set_type_name(self, type_name):
        self.type_name = type_name

    def update_age(self, age):
        if self.age < age:
            self.age = age
        else:
            print("You can not roll back an age")

        self.age += age

    # 控制用户修改属性值:
    # 以禁止增量为负值，从而防止有人利用它来回拨值。
    # 能够访问程序的人都可以通过直接访问属性来将里程表修改为任何值。
    def increment_age(self, increment_age):
        self.age += increment_age

#  TODO:
# my_dog = Dog('Dog-a', 1)
# my_dog.sit()  # Dog-a is sitting.
# print("Dog's name is " + my_dog.name)  # Dog's name is Dog-a


hi("123")
