def print_user_input():
    # # input(): string
    # msg = input("Please input anything: ")
    # print("Input is " + msg)
    #
    # # Good
    # prompt = "If you tell us who you are, we can personalize the messages you see."
    # prompt += "\nWhat is your first name? "
    # name = input(prompt)
    # print(name)

    num = input("Please input num : ")
    print(num)  # 8
    # print(num > 12)  # ERROR: Traceback (most recent call last): TypeError: '>' not supported between instances of 'str' and 'int'
    temp_num = int(num)
    print(temp_num > 12)  # false
    return


def test():
    print_user_input()
    return


test()
