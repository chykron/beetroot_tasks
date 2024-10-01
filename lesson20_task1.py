import unittest
from lesson20_functions import *


class TestFunctions(unittest.TestCase):
    # Testing add func
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(3.2, 2.3), 5.5)

    def test_is_palindrome(self):
        # Testing the is_palindrome
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))


if __name__ == '__main__':
    unittest.main()
