from default.define.dog import Dog


def test():
    dog = Dog('B', 10)

    # TODO:
    # Dog-a is sitting.
    # Dog's name is Dog-a
    dog.sit()  # B is sitting.
    print("Dog's name is " + dog.name)  # Dog's name is B
    print("Dog's name is " + dog.get_name())  # Dog's name is B
    print("Dog's type is " + dog.get_type_name())  # Dog's type is normal


    # 修改属性的值
    dog.type_name = "Ha Shi Qi"
    print("Dog's type is " + dog.get_type_name())  # Dog's type is Ha Shi Qi

    # 通过方法修改属性的值
    dog.set_type_name("Zang Ao")
    print("Dog's type is " + dog.get_type_name())  # Dog's type is Zang Ao

    return


test()
