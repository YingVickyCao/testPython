def has_ZeroDivisionError():
    print(5 / 0)  # ERROR: Traceback (most recent call last): ZeroDivisionError: division by zero


def handle_ZeroDivisionError(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Wrong operation: divide by zero")
    else:
        print(result)
    return


def has_FileNotFoundError():
    filename = 'alice.txt'
    with open(filename) as f_obj:  # ERROR: Traceback (most recent call last): FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
        contents = f_obj.read()


def handle_FileNotFoundError():
    file_name = 'alice.txt'
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = file_name + " does not exist."
        print(msg)


def test():
    # has_ZeroDivisionError()

    # handle_ZeroDivisionError(5, 0)  # Wrong operation: divide by zero
    # handle_ZeroDivisionError(5, 2)  # 2.5

    # has_FileNotFoundError()
    handle_FileNotFoundError()  # alice.txt does not exist.


test()
