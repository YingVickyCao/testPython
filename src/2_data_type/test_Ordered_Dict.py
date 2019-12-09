from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'C++'
favorite_languages['phil'] = 'java'
for name, language in favorite_languages.items():
    # Jen's favorite language is Python
    # Sarah's favorite language is C++
    # Phil's favorite language is Java
    print(name.title() + "'s favorite language is " + language.title())
print("\n")

favorite_languages2 = {}
favorite_languages2['jen'] = 'python'
favorite_languages2['sarah'] = 'C++'
favorite_languages2['phil'] = 'java'
for name, language in favorite_languages2.items():
    # Jen's favorite language is Python
    # Sarah's favorite language is C++
    # Phil's favorite language is Java
    print(name.title() + "'s favorite language is " + language.title())
