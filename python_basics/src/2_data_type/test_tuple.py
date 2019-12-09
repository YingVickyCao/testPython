def define_tuple():
    nums = (10, 20)
    print(nums)
    return


def access_tuple():
    nums = (10, 20)
    print(nums)
    print(nums[0])  # 10
    print(nums[1])  # 20
    print(nums[-1])  # 20
    # print(nums[-10])  # ERROR: Traceback (most recent call last): IndexError: tuple index out of range
    # print(nums[10])  # ERROR: Traceback (most recent call last): IndexError: tuple index out of range
    return


def modify_tuple_item():
    nums = (10, 20)
    print(nums)

    # nums[1] = 21  # ERROR: Traceback (most recent call last): TypeError: 'tuple' object does not support item assignment
    # print(nums)
    return


def modify_tuple():
    nums = (10, 20)
    print(nums)  # (10, 20)

    nums = (100, 200)
    print(nums)  # (100, 200)
    return


def traversing_tuple():
    nums = (10, 20)
    # 10
    # 20
    for item in nums:
        print(item)
    return


def test():
    # define_tuple()
    # access_tuple()
    modify_tuple_item()
    modify_tuple()
    # traversing_tuple()
    return


test()
