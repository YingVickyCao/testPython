def create_empty_dictionary():
    alien = {}
    print(alien)  # {}

    alien['color'] = 'green'
    print(alien)  # {'color': 'green'}

    alien2 = {}
    alien2[5] = 'green'
    print(alien2)  # {5: 'green'}

    alien3 = {5: 'green'}
    print(alien3)  # {5: 'green'}
    return


def access_dictionary():
    # people = {'color': "yellow", 'age': 100, }
    people = {'color': "yellow", 'age': 100}
    print(people['color'])  # yellow
    print(people['age'])  # 100
    # print(people['Color'])  # ERROR: Traceback (most recent call last): KeyError: 'Color'
    # print(people['dog'])  # ERROR: Traceback (most recent call last): KeyError: 'dog'
    return


def add_key_value():
    # Game, 外星人被杀死
    alien = {'color': "yellow", 'point': 5}
    alien["x_position"] = 10
    alien["y_position"] = 25
    print(alien)
    return


def modify_value():
    alien = {'color': "yellow", 'x_position': 5, 'speed': 'medium'}
    print(alien)  # {'color': 'yellow', 'x_position': 5, 'speed': 'medium'}

    alien['color'] = 'green'
    print(alien)  # {'color': 'green', 'x_position': 5, 'speed': 'medium'}

    if alien['speed'] == 'slow':
        x_increment = 1
    elif alien['speed'] == 'medium':
        x_increment = 2
    else:
        x_increment = 3
    alien['x_position'] = alien['x_position'] + x_increment
    print(alien)  # {'color': 'green', 'x_position': 7, 'speed': 'medium'}

    alien['x'] = alien['x_position'] + x_increment
    # 逻辑错误。 modify -> add
    print(alien)  # {'color': 'green', 'x_position': 7, 'speed': 'medium', 'x': 9}
    return


def delete_key_value():
    alien = {'color': "yellow", 'x_position': 5, 'speed': 'medium'}
    print(alien)

    del alien['x_position']
    print(alien)  # {'color': 'yellow', 'speed': 'medium'}

    # del alien['y']  # ERROR: Traceback (most recent call last): KeyError: 'y'
    return


def traversing_dictionary():
    traversing_dictionary_by_key_value()
    traversing_dictionary_by_key()
    traversing_dictionary_by_value()
    return


def traversing_dictionary_by_key_value():
    user = {
        'name': "A",
        'phone': "1"
    }
    for key, value in user.items():
        print(key)
        print(value)

    # Good : 所有key用途一致，所有value作用一致，使用具体含义的名字，而不是key 和 value，这让人更容易明白循环的作用
    favorite_languages = {'jen': 'python', 'sarah': 'c', }
    for name, language in favorite_languages.items():
        print(name.title() + "'s favorite language is " + language.title() + ".")
    return


def traversing_dictionary_by_key():
    favorite_languages = {'jen': 'python', 'sarah': 'c', }
    for name in favorite_languages:
        # jen
        # sarah
        print(name)

    # sarah
    # Hi, sarah,I see your favorite language is c
    print("\n")
    friends = ['p', 'sarah']
    # Good : 遍历字典时，会默认遍历所有的键.显示使用keys()，让代码更易理解
    # .keys()返回一个列表，其中包含了所有 key
    if name in favorite_languages.keys():
        print(name)
        if name in friends:
            print("Hi, " + name + ",I see your favorite language is " + favorite_languages[name])

    # 按顺序遍历字典中的所有键
    print("\n")
    favorite_languages2 = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
    for name in sorted(favorite_languages2.keys()):
        # edward
        # jen
        # phil
        # sarah
        print(name)
    return


def traversing_dictionary_by_value():
    favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
    # values()，它返回一个值列表
    for language in favorite_languages.values():
        # python
        # c
        # ruby
        # python
        print(language)

    # 去重
    print("\n")
    for language in set(favorite_languages.values()):
        # ruby
        # c
        # python
        print(language)
    return


def nested():
    # nested_type_list_nest_dictionary()
    # nested_type_dictionary_nest_list()
    nested_type_dictionary_nest_dictionary()
    return


def nested_type_list_nest_dictionary():
    stu1 = {'name': 'A', 'language': 'C++'}
    stu2 = {'name': 'C', 'language': 'Java'}

    students = [stu1, stu2]
    print(students)  # [{'name': 'A', 'language': 'C++'}, {'name': 'C', 'language': 'Java'}]

    print("\n")
    for stu in students:
        # {'name': 'A', 'language': 'C++'}
        # {'name': 'C', 'language': 'Java'}
        print(stu)

    print("\n")
    students2 = []
    students2.append(stu1)
    students2.append(stu2)
    print(students2)  # [{'name': 'A', 'language': 'C++'}, {'name': 'C', 'language': 'Java'}]
    return


def nested_type_dictionary_nest_list():
    students = {'phil': ['C++', 'Python'], "jen": ['Java']}
    print(students)  # {'phil': ['C++', 'Python'], 'jen': ['Java']}

    print("\n")
    for name, languages in students.items():
        # phil is good at
        # C++
        # Python
        # jen is good at
        # Java
        print(name + " is good at ")
        for language in languages:
            print(language)
    return


def nested_type_dictionary_nest_dictionary():
    users = {
        "id_1": {"name": "name_1", 'location': 'beiJing'},
        "id_2": {"name": "name_2", 'location': 'shangHai'}
    }
    print(users)  # {'id_1': {'name': 'name_1', 'location': 'bei jing'}, 'id_2': {'name': 'name_1', 'location': 'bei jing'}}

    for user_id, user_info in users.items():
        # id_1,name_1,beiJing
        # id_2,name_2,shangHai
        print(user_id + "," + user_info['name'] + "," + user_info['location'])

    return


def test():
    # access_dictionary()
    # create_empty_dictionary()
    # add_key_value()
    # modify_value()
    # delete_key_value()
    # traversing_dictionary()
    nested()
    return


test()
