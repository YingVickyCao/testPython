def condition_testing():
    # 比较数字和字符串
    name = 'mn'
    print(name == 'mn')  # True
    print(name == 'mN')  # False
    print(name == 'm')  # False
    print(name >= 'Y')  # True TODO:

    age = 18
    print(age == 18)  # True
    print(age == 3)  # False

    # 检查多个条件：and, or
    num_1 = 2
    num_2 = 8
    print(num_1 > 5 and num_2 > 5)  # False
    print(num_1 > 5 or num_2 > 5)  # True

    # 检查特定值是否包含在列表中？in。 大小写、空格敏感
    food = ['A', 'b', "c"]
    print("A" in food)  # True
    print("a" in food)  # False
    print("A " in food)  # False
    print("b" in food)  # True

    # 检查特定值是否不包含在列表中？not in。 大小写、空格敏感
    print("A" not in food)  # False
    print("a" not in food)  # True
    print("A " not in food)  # True
    print("b" not in food)  # False
    return


def use_if():
    # simple_if()
    # if_else()
    # if_elif_else()
    # use_multiple_elif()
    # omit_else()
    test_multiple_condition()
    use_if_handle_list()
    return


def simple_if():
    age = 20
    if age > 18:  # 条件测试
        print("You are old enough to vote!")
        print("Have you have registered to vote yet? ")
    print("\n")
    return


def if_else():
    num = 2
    if num > 10:  # 条件测试
        print("Big than 10")
        print(">10")
    else:
        print("Not big than 10")
        print("<10")
    print("\n")
    return


def if_elif_else():
    # amusement park, check to Ticket Price
    # Bad
    age = 12
    if age < 4:
        print("Admission cost is $0")
    elif age < 18:
        print("Admission cost is $5")
    else:
        print("Admission cost is $10")

    # Good: 效率更高，易修改
    if age < 4:
        price = 0
    elif age < 18:
        # print()
        price = 5
    else:
        price = 10
    print("Admission cost is $" + str(price))  # ERROR: Traceback (most recent call last): UnboundLocalError: local variable 'price' referenced before assignment
    return


def use_multiple_elif():
    age = 12
    if age < 4:
        price = 0
    elif age < 18:
        price = 5
    elif age < 65:
        price = 10
    else:
        price = 5
    print("Admission cost is $" + str(price))
    return


def omit_else():
    # else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。
    # Good: 使用一个elif代码块来 代替else代码块
    age = 12
    if age < 4:
        price = 0
    elif age < 18:
        price = 5
    elif age < 65:
        price = 10
    elif age >= 65:
        price = 5
    print("Admission cost is $" + str(price))
    return


def test_multiple_condition():
    # 一点点drink：加糖，加柠檬，加冰，加牛奶
    yi_dian_dian_drink_elements = ["sugar", 'ice', 'milk', 'orange']

    drink_requested_toppings = ['water']
    if 'sugar' in yi_dian_dian_drink_elements:
        drink_requested_toppings.append('sugar')

    if 'ice' in yi_dian_dian_drink_elements:
        drink_requested_toppings.append('ice')

    if 'milk' in yi_dian_dian_drink_elements:
        drink_requested_toppings.append('milk')

    if 'orange' in yi_dian_dian_drink_elements:
        drink_requested_toppings.append('orange')

    print(drink_requested_toppings)
    return


def use_if_handle_list():
    # Car1
    # CAR2
    # Car3
    # Check special item in list
    cars = ["car1", "car2", "car3"]
    for car in cars:
        if car == 'car2':
            print(car.upper())
        else:
            print(car.title())

    # Check if list is empty
    print("\n")
    nums = []
    if nums:
        print(nums)
    else:
        print("Nums is empty")

    # Use many list
    print("\n")
    # 一点点drink：加糖，加柠檬，加冰，加牛奶
    available_toppings = ["sugar", 'ice', 'milk', 'orange']
    requested_toppings = ["sugar", 'A', 'milk']
    accepted_toppings = ['water']
    for requested_topping_item in requested_toppings:
        if requested_topping_item in available_toppings:
            accepted_toppings.append(requested_topping_item)
            print("Add " + requested_topping_item)
        else:
            print("Sorry, we don't have " + requested_topping_item)
    print(accepted_toppings)
    return


def test():
    # condition_testing()
    use_if()
    return


test()
