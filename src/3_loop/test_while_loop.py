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


# Good: while > for
def move_items_between_list():
    confirmed_users = []
    unconfirmed_users = ['A', "B", 'C']
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        # C
        # B
        # A
        print(current_user)
        confirmed_users.append(current_user)

    print(confirmed_users)  # ['C', 'B', 'A']
    print(unconfirmed_users)  # []
    return


# Good: while > for
def remove_special_items_in_list():
    pets = ['dog', 'cat', 'dog', 'cat', 'rabbit', 'cat']
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)  # ['dog', 'dog', 'rabbit']
    return


def test():
    check_while_exit_condition()
    let_user_choose_when_exit()
    let_user_choose_when_exit_4_user_flag()
    break_to_exit_loop()
    continue_in_loop()
    move_items_between_list()
    remove_special_items_in_list()
    return


test()
