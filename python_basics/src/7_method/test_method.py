import pizza
from module_1 import function_2, function_3
from module_1 import function_4 as f4
import pizza as p
from module_1 import *


def define_method():
    # hi()  # ERROR: Traceback (most recent call last): TypeError: hi() missing 1 required positional argument: 'username'
    hi("Jerry")
    hi2("Jerry")


def hi():
    # docstring
    """ Just say hi """
    print("Hi")


def hi(username):
    print("Hi" + username)


def hi2(username):
    print("Hi" + username)


def pass_actual_param():
    # pass_actual_argument_4_position_argument()
    # pass_actual_argument_4_keyword_argument()
    # default_value()

    # pass_list()

    pass_any_num_actual_argument()


# 传递实参  - 位置实参：基于实参的顺序
def pass_actual_argument_4_position_argument():
    pet("dog", 'Jerry')
    pet('Jerry', "dog")  # 逻辑错误


def pet(pet_type, pet_name):
    print(pet_type + "'s name is " + pet_name)


def pass_actual_argument_4_keyword_argument():
    stu(name="Xiao Ming", score=15)
    stu(score=15, name="Xiao Ming")


def stu(name, score):
    print(name + "'s score is " + str(score))


def default_value():
    rect(5, 20)  # 5,20
    rect(100)  # 100,10
    menu_order_item(10, 'rice')  # rice's price is 10
    menu_order_item()  # Tomato's price is 5


def rect(length, width=10):
    print(str(length) + "," + str(width))


# RRROR: non-default parameter follows default parameter
# def shop_item(price=5, name):

def menu_order_item(price=5, name='Tomato'):
    print(name + "'s price is " + str(price))


def return_value():
    # Good: 使用默认参数，让实参变得可选
    print(get_formatted_name("Wu", 'xi'))  # Wu Xi
    print(get_formatted_name("rock", 'ghost', "mu"))  # Rock Mu Ghost
    # return value is dictionary
    print(build_name("Wu", 'xi'))  # {'fist_name': 'Wu', 'last_name': 'xi'}


def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        return first_name.title() + " " + middle_name.title() + " " + last_name.title()
    else:
        return first_name.title() + " " + last_name.title()


def build_name(first_name, last_name, middle_name=""):
    if middle_name:
        return {'fist_name': first_name, "middle_name": middle_name, "last_name": last_name}
    else:
        return {'fist_name': first_name, "last_name": last_name}


def pass_list():
    # Tom
    # Jerry
    user_names = ["Tom", "Jerry"]
    hi_users(user_names)

    # 在函数中修改列表
    method_modify_list()

    # 禁止函数修改列表
    forbid_method_modify_list()


def hi_users(names):
    for name in names:
        print(name)


def method_modify_list():
    print("\n")
    unprinted_designs = ['iphone case', 'robot design']
    completed_models = []
    print_models(unprinted_designs, completed_models)
    print("\n")
    show_completed_models(completed_models)  # ['robot design', 'iphone case']
    show_uncompleted_models(unprinted_designs)  # []


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current = unprinted_designs.pop()
        print(current)
        completed_models.append(current)


def show_completed_models(completed_models):
    # for item in completed_models:
    #     print(item)
    print(completed_models)


def show_uncompleted_models(unprinted_designs):
    print(unprinted_designs)


def forbid_method_modify_list():
    print("\n")
    unprinted_designs = ['iphone case', 'robot design']
    completed_models = []
    print_models(unprinted_designs[:], completed_models)
    print("\n")
    show_completed_models(completed_models)  # ['robot design', 'iphone case']
    show_uncompleted_models(unprinted_designs)  # ['iphone case', 'robot design']


def pass_any_num_actual_argument():
    # 任意数量实参
    make_pizza('A')  # ('A',)
    make_pizza('C', 'D', "E")  # ('C', 'D', 'E')

    # 结合使用位置实参和任意数量实参
    method_can_receive_different_type_argument()

    # 使用任意数量的关键字实参
    print("\n")
    profile = build_profile('Tom', age=1, animal_type='cat')
    print(profile)  # {'name': 'Tom', 'age': 1, 'animal_type': 'cat'}


def make_pizza(*toppings):
    print(toppings)
    for item in toppings:
        print("Add " + item)


def method_can_receive_different_type_argument():
    # size is Small,add toppings below:
    # Milk
    make_drink("Small", 'Milk')
    print("\n")

    # size is Medium,add toppings below:
    # Sugar
    # Orange
    make_drink("Medium", 'Sugar', 'Orange')


def make_drink(size, *toppings):
    print("size is " + size + ",add toppings below:");
    for item in toppings:
        print("" + item)


def build_profile(name, **user_info):
    profile = {}
    profile['name'] = name
    for key, value in user_info.items():
        profile[key] = value
    return profile


def import_module():
    # 导入整个模块
    pizza.make_pizza('A')  # ('A',)
    pizza.make_pizza('C', 'D', "E")  # ('C', 'D', 'E')

    # 导入特定的函数
    print("\n")
    function_2()  # function_2
    function_3()  # function_3

    # 使用as 给函数指定别名
    print("\n")
    f4()  # function_4

    # 使用as给模块指定别名
    print("\n")
    p.make_pizza('A')  # ('A',)
    p.make_pizza('C', 'D', "E")  # ('C', 'D', 'E')

    # 导入模块中的所有函数
    print("\n")
    function_1()  # function_1


def test():
    # define_method()
    # return_value()
    # pass_actual_param()
    import_module()


test()
