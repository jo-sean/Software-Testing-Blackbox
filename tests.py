# Name: Sean Perez
# Date: 4.11.22
# CS 362 - HW1

import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    """Unittest to find 6 bugs in the credit_card_validator func"""

    # Length related tests
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
        ae_short = "34826548652111"
        self.assertFalse(credit_card_validator(ae_short),
                         msg=''.format(credit_card_validator(ae_short)))

    def test9_ae_length_long(self):
        # Check and prefix are valid; length is 16
        ae_long = "3482654865211135"
        self.assertFalse(credit_card_validator(ae_long),
                         msg=''.format(credit_card_validator(ae_long)))

    # Everything is valid
    def test10_vs_valid_length(self):
        # Check and prefix are valid; length is 16
        vs_valid = "4582654865211421"
        self.assertTrue(credit_card_validator(vs_valid),
                        msg=''.format(credit_card_validator(vs_valid)))

    def test11_mc_51_55_valid_length(self):
        # Check and prefix are valid; length is 16
        mc_valid = "5282654865211413"
        self.assertTrue(credit_card_validator(mc_valid),
                        msg=''.format(credit_card_validator(mc_valid)))

    def test12_mc_2221_2720_valid_length(self):
        # Check and prefix are valid; length is 16
        mc_valid = "2222847589562356"
        self.assertTrue(credit_card_validator(mc_valid),
                        msg=''.format(credit_card_validator(mc_valid)))

    def test13_ae_valid_length(self):
        # Check and prefix are valid; length is 15
        ae_valid = "34826548652112"
        self.assertTrue(credit_card_validator(ae_valid),
                        msg=''.format(credit_card_validator(ae_valid)))

    # Prefix related tests
    def test14_vs_low_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_l_prefix = "3282654865211251"
        self.assertFalse(credit_card_validator(vs_l_prefix),
                         msg=''.format(credit_card_validator(vs_l_prefix)))

    def test15_vs_upper_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_u_prefix = "5782654865211251"
        self.assertFalse(credit_card_validator(vs_u_prefix),
                         msg=''.format(credit_card_validator(vs_u_prefix)))

    def test16_mc_51_55_low_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_l_prefix = "5082654865211258"
        self.assertFalse(credit_card_validator(vs_l_prefix),
                         msg=''.format(credit_card_validator(vs_l_prefix)))

    def test17_mc_51_55_upper_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_u_prefix = "5682654865211252"
        self.assertFalse(credit_card_validator(vs_u_prefix),
                         msg=''.format(credit_card_validator(vs_u_prefix)))

    def test18_mc_2221_2720_low_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_l_prefix = "2220654865211258"
        self.assertFalse(credit_card_validator(vs_l_prefix),
                         msg=''.format(credit_card_validator(vs_l_prefix)))

    def test19_mc_2221_2720_upper_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_u_prefix = "2721654865211252"
        self.assertFalse(credit_card_validator(vs_u_prefix),
                         msg=''.format(credit_card_validator(vs_u_prefix)))

    def test20_ae_34_low_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_l_prefix = "3382654865211250"
        self.assertFalse(credit_card_validator(vs_l_prefix),
                         msg=''.format(credit_card_validator(vs_l_prefix)))

    def test21_ae_34_upper_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_u_prefix = "5782654865211251"
        self.assertFalse(credit_card_validator(vs_u_prefix),
                         msg=''.format(credit_card_validator(vs_u_prefix)))

    def test22_ae_37_low_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_l_prefix = "3682654865211257"
        self.assertFalse(credit_card_validator(vs_l_prefix),
                         msg=''.format(credit_card_validator(vs_l_prefix)))

    def test23_ae_37_upper_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_u_prefix = "3882654865211255"
        self.assertFalse(credit_card_validator(vs_u_prefix),
                         msg=''.format(credit_card_validator(vs_u_prefix)))

    # Check digit related tests


if __name__ == '__main__':
    unittest.main(verbosity=2)
