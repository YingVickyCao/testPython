def test():
    test_string()
    return


# String
def test_string():
    print("String 1")
    print('String 2')

    print('A "B" C')  # A "B" C
    print("A 'B' C")  # A 'B' C
    print("A B' C")  # A B' C
    # Compile ERROR:Python can not confirm the end position of string
    # print('A B' C')  # A B' C

    hi = 'hI'
    print(hi.title())  # Hi
    print(hi.lower())  # hi
    print(hi.upper())  # HI

    # concat string
    first_name = 'M'
    last_name = 'n'
    full_name = first_name + " " + last_name
    print(full_name)

    # Add blank(空白)
    print("Python")
    print("\tPython")

    print("Language:\nC\nC++")

    print("Language:\nC\n\tC++")

    # Delete blank
    # string.rstrip() Delete character,default is blank, from tail of string.
    print("ABCD")
    str2 = " ABC "
    print(str2 + "D")
    print(str2.rstrip() + "D")
    str3 = " de\t "
    print(str3 + "f")
    print(str3.rstrip() + "f")

    # string.lstrip():返回截掉字符串左边的空格或指定字符后生成的新字符串。
    # 88mn88
    # 88mn88
    #    88mn88
    # mn88
    print("88mn88")
    print("   88mn88".lstrip())
    print("   88mn88".lstrip('8'))
    print("88mn88".lstrip('8'))
    return


test()
