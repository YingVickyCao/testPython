import unittest

from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):

    def test_get_formatted_name(self):
        print("test_get_formatted_name: START ")
        formatted_name = get_formatted_name('A', 's')
        self.assertEqual(formatted_name, 'A S')
        print("test_get_formatted_name: END ")


# 理解为是一个主函数，当前这个Python文件的入口
if __name__ == "__main__":
    unittest.main()

# unittest.main()
