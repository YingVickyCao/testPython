import unittest

from stu import Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.stu = Student(100)

    def test_get_country(self):
        # stu = Student(100)
        # self.assertEqual('China', stu.get_country())
        self.assertEqual('China', self.stu.get_country())

    def test_get_score(self):
        # stu = Student(100)
        # self.assertEqual(100, stu.get_score())
        self.assertEqual(100, self.stu.get_score())


if __name__ == '__main__':
    unittest.main()
