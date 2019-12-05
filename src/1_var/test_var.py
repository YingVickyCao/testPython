def test():
    test_var()
    return


# Var
def test_var():
    msg = "A"
    print(msg)

    msg = "B"
    print(msg)

    # ERROR:Traceback：NameError: name 'message' is not defined
    # print(message)

    # ERROR:Traceback ：NameError: name 'num' is not defined
    # num
    # print(num)
    return


test()
