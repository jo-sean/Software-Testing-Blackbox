# Name: Sean Perez
# Date: 4.11.22
# CS 362 - HW1

import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    """Unittest to find 6 bugs in the credit_card_validator func"""

    def test1_empty(self):
        empty_string = ""
        self.assertFalse(credit_card_validator(empty_string),
                         msg=''.format(credit_card_validator(empty_string)))

    def test2_vs_length_short(self):
        # Check and prefix are valid; length is 15
        vs_short = "458265486521145"
        self.assertFalse(credit_card_validator(vs_short),
                         msg=''.format(credit_card_validator(vs_short)))

    def test3_vs_length_long(self):
        # Check and prefix are valid; length is 17
        vs_long = "45826548652114211"
        self.assertFalse(credit_card_validator(vs_long),
                         msg=''.format(credit_card_validator(vs_long)))

    def test4_mc_51_55_length_short(self):
        # Check and prefix are valid; length is 15
        mc_short = "528265486521141"
        self.assertFalse(credit_card_validator(mc_short),
                         msg=''.format(credit_card_validator(mc_short)))

    def test5_mc_51_55_length_long(self):
        # Check and prefix are valid; length is 17
        mc_long = "52826548652114142"
        self.assertFalse(credit_card_validator(mc_long),
                         msg=''.format(credit_card_validator(mc_long)))

    def test6_mc_2221_2720_length_short(self):
        # Check and prefix are valid; length is 15
        mc_short = "222284758956231"
        self.assertFalse(credit_card_validator(mc_short),
                         msg=''.format(credit_card_validator(mc_short)))

    def test7_mc_2221_2720_length_long(self):
        # Check and prefix are valid; length is 17
        mc_long = "22228475895623548"
        self.assertFalse(credit_card_validator(mc_long),
                         msg=''.format(credit_card_validator(mc_long)))

    def test8_ae_length_short(self):
        # Check and prefix are valid; length is 14
        ae_short = "35826548652111"
        self.assertFalse(credit_card_validator(ae_short),
                         msg=''.format(credit_card_validator(ae_short)))

    def test9_ae_length_long(self):
        # Check and prefix are valid; length is 16
        ae_long = "3582654865211456"
        self.assertFalse(credit_card_validator(ae_long),
                         msg=''.format(credit_card_validator(ae_long)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
