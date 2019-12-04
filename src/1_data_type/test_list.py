def access_list_item():
    phone_device_types = ["IOS", "Android"]
    print(phone_device_types)  # ['IOS', 'Android']

    print(phone_device_types[0])
    print(phone_device_types[0].title())

    # -1 = last item. 倒数第一个
    print(phone_device_types[-1])  # Android

    # -2 = 倒数第二个
    print(phone_device_types[-2])

    #
    # ERROR: Traceback (most recent call last): IndexError: list index out of range
    # print(phone_device_types[-3])

    shopping_name = []
    # ERROR:Traceback (most recent call last):IndexError: list index out of range
    # print("access []: [0]=" + shopping_name[0])

    # ERROR:Traceback (most recent call last):IndexError: list index out of range
    # print("access []: [-1]=" + shopping_name[-1])
    return


def modify_add_remove_item():
    nums = [10, 20, 30]
    print(nums)  # [10, 20, 30]

    # modify item
    nums[0] = 1
    print(nums)  # [1, 20, 30]

    # add item
    nums.append(40)
    print(nums)  # [1, 20, 30, 40]

    # insert item before index
    nums.insert(1, 50)
    print(nums)  # [1, 50, 20, 30, 40]

    nums.insert(10, 10)
    print(nums)  # [1, 50, 20, 30, 40, 10]

    # remove item
    return


def test():
    # access_list_item()
    modify_add_remove_item()
    return


test()
