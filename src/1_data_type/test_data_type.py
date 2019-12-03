# Var
msg = "A"
print(msg)

msg = "B"
print(msg)

# Traceback：NameError: name 'message' is not defined
# print(message)

# Traceback ：NameError: name 'num' is not defined
# num
# print(num)

# String
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

# number
print(20 + 2)
print(20 * 2)
print(20 + 2)
print(20 / 2)  # 10.0

print(2 + 3 * 4)
print((2 + 3) * 4)

# float
print(0.1 + 0.1)  # 0.2
float_num_1 = 0.1
float_num_2 = 0.1
float_num_total = float_num_1 + float_num_2
print(float_num_1 + float_num_2)  # 0.2
print(float_num_total)  # 0.2
print(0.2 + 1)
print(0.1 + 0.12)

# number -> string
age = 10
# Traceback : TypeError: can only concatenate str (not "int") to str
# msg = "Happy" + age + "rd Birthday!"
msg = "Happy " + str(age) + "rd Birthday!"
print(msg)
msg = "Happy " + repr(age) + "rd Birthday!"
print(msg)

# integer : Python 2 vs Python 3
print(3 / 2)        # Python 3: 1.5. Python 2: 1
print(3.0 / 2)      # 1.5
print(3 / 2.0)      # 1.5
print(3.0 / 2.0)    # 1.5
