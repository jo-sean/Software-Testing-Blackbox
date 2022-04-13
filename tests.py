# Name: Sean Perez
# Date: 4.11.22
# CS 362 - HW1

import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    """Unittest to find 6 bugs in the credit_card_validator func"""

    def test_empty(self):
        empty_string = ""
        self.assertTrue(credit_card_validator(empty_string), msg=''.format(credit_card_validator(empty_string)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
