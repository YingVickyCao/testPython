import json

file_name = 'nums.json'


#  将数字存储在json中
def save():
    nums = [1, 2, 3, 4]
    with open(file_name, 'w') as file_obj:
        json.dump(nums, file_obj)
    return


# 将数字读取到内存中
def read():
    with open(file_name) as file_object:
        nums = json.load(file_object)
    print(nums)
    return


def test():
    save()
    read()
    return


test()
