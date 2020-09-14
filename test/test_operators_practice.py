import unittest


class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        self.assertFalse(5 == 5)
    def test_not_equals(self):
        self.assertFalse(5 != 6)
    def test_greater_than(self):
        self.assertFalse(6>3)
    def test_less_than(self):
        self.assertFalse(5<6)
    def test_greater_than_or_equal_to(self):
        self.assertFalse(3>=2)
    def test_less_than_or_equal_to(self):
        self.assertFalse(2<=3)


if __name__ == '__main__':
    unittest.main()
