def read_while_file():
    print_file('pi_digits.txt')


def file_path():
    #  相对文件路径
    print_file("text_files/one.txt")  # OS，1
    # print_file("text_files\one.txt")  # Windows,1

    # 绝对文件路径
    print_file(
     "/Users/hades/Documents/project/testPython/python_basics/src/9_io/read/text_files/one.txt")  # OS，1
    # print_file("C:\Users\hades\Documents\project\testPython\python_basics\src\9_io\read\text_files/one.txt")  # Windows，1
    return


# 读取整个文件
def print_file(file_name):
    with open(file_name) as file_object:
        contents = file_object.read()
        # 3.1415926535
        #   8979323846
        #   2643383279
        #
        # print(contents)  # read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行.

        # 3.1415926535
        #   8979323846
        #   2643383279
        print(contents.rstrip())  # rstrip(): 删除(剥除)字符串末尾的空白


# 逐行读取
def print_file_line_by_line(file_name):
    with open(file_name) as file_object:
        # 通过对文件对象执行循环来遍历 文件中的每一行
        for line in file_object:
            print(line.rstrip())


# 在with代码块外，访问文件内容
def get_file_lines(file_name):
    with open(file_name) as file_object:
        # readlines()从文件中读取每一行，并将其存储在一个列表中
        lines = file_object.readlines()
        return lines


def read_line_by_line():
    file_name = 'pi_digits.txt'
    print_file_line_by_line(file_name)


def read_pi(file_name):
    # file_name = 'pi_digits.txt'
    lines = get_file_lines(file_name)
    pi_string = ''
    # pi_string2 = ''
    for line in lines:
        # 3.1415926535
        #   8979323846
        #   2643383279
        # print(line.strip())
        pi_string += line.strip()
        # print(line.rstrip())
        # pi_string2 += line.rstrip()
    return pi_string


def read_file_contents_outside_with():
    file_name = 'pi_digits.txt'  # 包含精确30位的圆周率值
    pi_string = read_pi(file_name)
    # 3.141592653589793238462643383279
    # 32

    # 3.1415926535  8979323846  2643383279
    # 36
    print(pi_string)
    print(len(pi_string))

    file_name2 = 'pi_million_digits.txt'  # 包含精确到小数点后1 000 000位的圆周率值
    pi_string2 = read_pi(file_name2)
    print(pi_string2[:52])  # 只打印到小数点后50位
    print(len(pi_string2))


def test():
    # read_while_file()
    file_path()
    # read_while_file()
    # read_file_contents_outside_with()


test()
