def traversing_list():
    score = [90, 94, 98]
    for item in score:
        print(item)
    return


def move_items_between_list():
    confirmed_users = []
    unconfirmed_users = ['A', "B", 'C']
    # When for loop, unconfirmed_users item can not be removed, or result will be wrong.
    for user in unconfirmed_users:
        # C
        # B
        # A
        print(user)
        confirmed_users.append(user)
    unconfirmed_users.clear()

    print("\n")
    print(confirmed_users)  # ['C', 'B', 'A']
    print(unconfirmed_users)  # []
    return


def remove_special_items_in_list():
    pets = ['dog', 'cat', 'dog', 'cat', 'rabbit', 'cat']
    for pet in pets:
        if pet == 'cat':
            pets.remove(pet)
    print(pets)  # ['dog', 'dog', 'rabbit']
    return


def test():
    traversing_list()
    move_items_between_list()
    remove_special_items_in_list()
    return


test()
