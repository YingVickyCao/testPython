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


def traversing_list():
    score = [90, 94, 98]
    for item in score:
        print(item)
    return


def traversing_list():
    score = [90, 94, 98]
    for item in score:
        print(item)
    return


def create_value_list():
    create_value_list4_use_range()
    return


def create_value_list4_use_range():
    # range(): start from first param, stop until second param. [)
    for value in range(1, 5):
        print(value)

    # list(range(1, 5))：convert result to a list
    nums = list(range(1, 5))  # [1, 2, 3, 4]
    print(nums)

    # create list with step: [)
    even_number = list(range(2, 11, 2))
    print(even_number)  # [2, 4, 6, 8, 10]

    even_number2 = list(range(2, 12, 2))
    print(even_number2)  # [2, 4, 6, 8, 10]
    return


# 统计计算
def statistical_computing():
    digits = [1, 10, 3]
    min_digit = min(digits)
    print(min_digit)  # 1

    max_digit = max(digits)
    print(max_digit)  # 10

    sum_of_digits = sum(digits)
    print(sum_of_digits)  # 14
    return


# 列表解析
def list_comprehension():
    squares = []
    for value in range(1, 5):
        # square = value ** 2
        # squares.append(square)
        squares.append(value ** 2)
    print(squares)  # [1, 4, 9, 16]

    # 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。
    # 首先指定一个描述性的列表名，squares2;然后，指定一个左方括号， 并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达式为value**2，它计 算平方值。接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。
    # 在这个示例中，for循环为for value in range(1,11)，它将值1~10提供给表达式value**2。
    # Why use it ? 使用代码生成列表太繁琐。创建列表解析，以简化生成列表。
    squares2 = [value ** 2 for value in range(1, 5)]
    print(squares2)  # [1, 4, 9, 16]
    return


# 切片
def segment():
    players = ["1", '2', "3", "4", "5", '6']
    # [startIndex : endIndex]
    print(players[0:2])  # ['1', '2']
    print(players[1:4])  # ['2', '3', '4']
    print(players[1:10])  # ['2', '3', '4', '5', '6']

    # When no start index, [0:
    print(players[:2])  # ['1', '2']

    # When no end index, :lastIndex]
    print(players[1:])  # ['2', '3', '4', '5', '6']

    # 负数索引： [倒数第n个:last index]
    print(players[-3:])  # ['4', '5', '6']
    print(players[-10:])  # ['1', '2', '3', '4', '5', '6']

    # traversing segment
    # 1
    # 2
    for item in players[:2]:
        print(item)

    # Copy list
    # Copy whole list
    # =[:]:value copy
    # 使用列表副本
    my_shopping_foods = ["pizza", 'cake', 'coffee']
    friend_shopping_foods = my_shopping_foods[:]
    print(my_shopping_foods)  # ['pizza', 'cake', 'coffee']
    print(friend_shopping_foods)  # ['pizza', 'cake', 'coffee']

    my_shopping_foods.append('water')
    friend_shopping_foods.append('ice cream')
    print(my_shopping_foods)  # ['pizza', 'cake', 'coffee', 'water']
    print(friend_shopping_foods)  # ['pizza', 'cake', 'coffee', 'ice cream']

    # = : set ref
    # 设置引用
    my_languages = ['C', "C++", 'Java', "JS"]
    friend_languages = my_languages
    print(my_languages)
    print(friend_languages)

    my_languages.append('Python')
    friend_languages.append("Excel")
    print(my_languages)  # ['C', 'C++', 'Java', 'JS', 'Python', 'Excel']
    print(friend_languages)  # ['C', 'C++', 'Java', 'JS', 'Python', 'Excel']
    # Copy segment
    return


def test():
    # access_list_item()
    # modify_item()
    # add_item()
    # remove_item()
    # sort_list()
    # reverse_list()
    # length_of_list()
    # traversing_list()
    # create_value_list()
    # statistical_computing()
    # list_comprehension()
    segment()
    return


test()
