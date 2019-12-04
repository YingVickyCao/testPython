def test():
    test_number()
    return


# number
def test_number():
    test_integer()
    test_float()
    test_number_to_string()
    return


def test_integer():
    print(20 + 2)
    print(20 * 2)
    print(20 + 2)
    print(20 / 2)  # 10.0

    print(2 + 3 * 4)
    print((2 + 3) * 4)
    return


def test_float():
    # float
    print(0.1 + 0.1)  # 0.2
    float_num_1 = 0.1
    float_num_2 = 0.1
    float_num_total = float_num_1 + float_num_2
    print(float_num_1 + float_num_2)  # 0.2
    print(float_num_total)  # 0.2
    print(0.2 + 1)
    print(0.1 + 0.12)
    return


# number -> string
def test_number_to_string():
    age = 10
    # ERROR:Traceback : TypeError: can only concatenate str (not "int") to str
    # msg = "Happy" + age + "rd Birthday!"
    msg = "Happy " + str(age) + "rd Birthday!"
    print(msg)
    msg = "Happy " + repr(age) + "rd Birthday!"
    print(msg)
    # integer : Python 2 vs Python 3
    print(3 / 2)  # Python 3: 1.5. Python 2: 1
    print(3.0 / 2)  # 1.5
    print(3 / 2.0)  # 1.5
    print(3.0 / 2.0)  # 1.5
    return


test()
