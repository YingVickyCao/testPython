def check_while_exit_condition():
    num1 = 1
    while num1 <= 5:
        # 1
        # 2
        # 3
        # 4
        # 5
        print(num1)
        num1 = num1 + 1

    print("\n")
    num2 = 10
    while num2 <= 5:
        print(num2)
        num2 = num2 + 1
    return


def let_user_choose_when_exit():
    print("Welcome. \nEnter 'quit' to end the program.")

    prompt = "Please input : "
    msg = ""
    while msg != 'quit':
        msg = input(prompt)
        if msg != 'quit':
            print(msg)
    return


def let_user_choose_when_exit_4_user_flag():
    print("Welcome. \nEnter 'quit' to end the program.")

    # Good
    active = True
    prompt = "Please input : "
    while active:
        msg = input(prompt)
        if msg == 'quit':
            active = False
        else:
            print(msg)
    return


def break_to_exit_loop():
    print("Welcome. \nEnter 'quit' to end the program.")
    prompt = "Please input num : "

    while True:
        num = input(prompt)
        if num == 'quit':
            break
        else:
            print(num)
    return


def continue_in_loop():
    i = 1
    while i < 5:
        current_num = i
        i = i + 1
        if current_num % 2 == 0:
            continue

        print(current_num)
    return


def test():
    # check_while_exit_condition()
    # let_user_choose_when_exit()
    # let_user_choose_when_exit_4_user_flag()
    # break_to_exit_loop()
    continue_in_loop()
    return


test()
