#!/usr/bin/python3
"""	Module to test the max integer
    from 6-max_integer module
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerMethod(unittest.TestCase):

    def test_max_integer(self):
        """test max integer
        """
        self.assertEqual(max_integer([2, 4, 65, 3, 9]), 65)
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
