def access_list_item():
    phone_device_types = ["IOS", "Android"]
    print(phone_device_types)  # ['IOS', 'Android']

    print(phone_device_types[0])
    print(phone_device_types[0].title())

    # -1 = last item. 倒数第一个
    print(phone_device_types[-1])  # Android

    # -2 = 倒数第二个
    print(phone_device_types[-2])

    # print(phone_device_types[-3])                 # ERROR: Traceback (most recent call last): IndexError: list index out of range

    shopping_name = []
    # print("access []: [0]=" + shopping_name[0])   # ERROR:Traceback (most recent call last):IndexError: list index out of range

    # print("access []: [-1]=" + shopping_name[-1]) # ERROR:Traceback (most recent call last):IndexError: list index out of range
    return


def modify_item():
    nums = [10, 20, 30]
    print(nums)  # [10, 20, 30]

    # modify item
    nums[0] = 1
    print(nums)  # [1, 20, 30]
    return


def add_item():
    nums = [10, 20, 30, 40]

    # add item
    print(nums)  # [10, 20, 30, 40]

    # insert item before index
    nums.insert(1, 50)
    print(nums)  # [10, 50, 20, 30, 40]

    nums.insert(10, 10)
    print(nums)  # [10, 50, 20, 30, 40, 10]
    return


def remove_item():
    nums = [1, 2, 3, 4, 5, 6]
    print(nums)  # [1, 2, 3, 4, 5, 6]

    # remove item

    # remove item - by index
    del nums[0]
    print(nums)  # [2, 3, 4, 5, 6]

    empty_list = []
    # del empty_list[2]     # ERROR: Traceback (most recent call last): IndexError: list assignment index out of range

    # remove item - by pop
    pop_num = nums.pop()
    print(nums)  # [2, 3, 4, 5]
    print(pop_num)  # 6

    pop_num2 = nums.pop(1)
    print(nums)  # [2, 4, 5]
    print(pop_num2)  # 3

    # empty_list.pop()      # ERROR: Traceback (most recent call last):IndexError: pop from empty list
    # empty_list.pop(2)     # ERROR: Traceback (most recent call last):IndexError: pop from empty list

    list2 = [1]
    # list2.pop(2)          # ERROR: Traceback (most recent call last): IndexError: pop index out of range

    # remove item - by value
    strings = ['A', 'B', "B", 'C', 'D']
    strings.remove('C')
    print(strings)  # ['A', 'B', 'B', 'D']
    # strings.remove('d')  # ERROR: Traceback (most recent call last): ValueError: list.remove(x): x not in list
    # print(strings)
    strings.remove('B')  # remove() Only delete the first pointed value. If want to delete all same values,  remove them by looping.
    print(strings)  # ['A', 'B', 'D']
    return


def test():
    # access_list_item()
    # modify_item()
    # add_item()
    remove_item()
    return


test()
