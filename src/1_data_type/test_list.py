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
    # print(shopping_name[0])   # ERROR:Traceback (most recent call last):IndexError: list index out of range
    # print(shopping_name[-1]) # ERROR:Traceback (most recent call last):IndexError: list index out of range
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


def sort_list():
    sort_list_by_permanent_order()
    sort_list_by_temporary_order()
    return


def sort_list_by_permanent_order():
    # Permanent order
    cars = ["bw", "ya", "abc", "ca"]
    cars.sort()  # 正序排列，永久排序
    print(cars)  # ['abc', 'bw', 'ca', 'ya']

    print("\n")
    languages = ['Java', 'C', "Python"]
    languages.sort(reverse=True)  # 倒序排列，永久排序
    print(languages)  # ['Python', 'Java', 'C']
    return


def sort_list_by_temporary_order():
    nums = [1, 10, 5, 8]
    num_temp = sorted(nums)  # 正序排列，临时排序
    print(num_temp)  # [1, 5, 8, 10]
    print(nums)  # [1, 10, 5, 8]

    print("\n")
    prices = [100, 5, 10]
    prices_temp = sorted(prices, reverse=True)  # 倒序排列，临时排序
    print(prices_temp)  # [100, 10, 5]
    print(prices)  # [100, 5, 10]
    return


def reverse_list():
    reverse_list_by_permanent_order()
    reverse_list_by_temporary_order()


def reverse_list_by_permanent_order():
    stu = ["A", "C", "B"]
    stu.reverse()  # 反转列表，not 倒序排列. 永久性修改，但通过再次调用恢复原来的排列顺序
    print(stu)  # ['B', 'C', 'A']
    stu.reverse()
    print(stu)  # ['A', 'C', 'B']
    return


def reverse_list_by_temporary_order():
    money = [5, 10, 8]
    money_temp = list(reversed(money))  # 反转列表，not 倒序排列. 临时反转
    # reversed(money) -> list_reverseiterator object at 0x1057fe450
    print(money_temp)  # [8, 10, 5]
    print(money)  # [5, 10, 8]
    return


def length_of_list():
    names = ["A", "C"]
    print(len(names))  # 2
    print(len([]))  # 0
    return


def test():
    access_list_item()
    # modify_item()
    # add_item()
    # remove_item()
    # sort_list()
    # reverse_list()
    # length_of_list()
    return


test()
