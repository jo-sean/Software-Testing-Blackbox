# Name: Sean Perez
# Date: 4.11.22
# CS 362 - HW1

import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    """Unittest to find 6 bugs in the credit_card_validator func"""

    # Length related tests

    # Verifies if empty string returns False
    # Picked using Category Partition Testing
    def test1_empty(self):
        empty_string = ""
        self.assertFalse(credit_card_validator(empty_string),
                         msg=''.format(credit_card_validator(empty_string)))

    # Verifies if Visa Cards with invalid lengths returns False
    # Picked using Category Partition Testing
    def test2_vs_length_short(self):
        # Check and prefix are valid; length is 15
        vs_short = "458265486521145"
        self.assertFalse(credit_card_validator(vs_short),
                         msg=''.format(credit_card_validator(vs_short)))

    # Verifies if Visa Cards with invalid lengths returns False
    # Picked using Category Partition Testing
    def test3_vs_length_long(self):
        # Check and prefix are valid; length is 17
        vs_long = "45826548652114211"
        self.assertFalse(credit_card_validator(vs_long),
                         msg=''.format(credit_card_validator(vs_long)))

    # Verifies if Master Cards with invalid lengths returns False
    # Picked using Category Partition Testing
    def test4_mc_51_55_length_short(self):
        # Check and prefix are valid; length is 15
        mc_short = "528265486521141"
        self.assertFalse(credit_card_validator(mc_short),
                         msg=''.format(credit_card_validator(mc_short)))

    # Verifies if Master Cards with invalid lengths returns False
    # Picked using Category Partition Testing
    def test5_mc_51_55_length_long(self):
        # Check and prefix are valid; length is 17
        mc_long = "52826548652114142"
        self.assertFalse(credit_card_validator(mc_long),
                         msg=''.format(credit_card_validator(mc_long)))

    # Verifies if Master Cards with invalid lengths returns False
    # Picked using Category Partition Testing
    def test6_mc_2221_2720_length_short(self):
        # Check and prefix are valid; length is 15
        mc_short = "222284758956231"
        self.assertFalse(credit_card_validator(mc_short),
                         msg=''.format(credit_card_validator(mc_short)))

    # Verifies if Master Cards with invalid lengths returns False
    # Picked using Category Partition Testing
    def test7_mc_2221_2720_length_long(self):
        # Check and prefix are valid; length is 17
        mc_long = "22228475895623548"
        self.assertFalse(credit_card_validator(mc_long),
                         msg=''.format(credit_card_validator(mc_long)))

    # Verifies if AmEx Cards with invalid lengths returns False
    # Picked using Category Partition Testing
    def test8_ae_length_short(self):
        # Check and prefix are valid; length is 14
        ae_short = "34826548652111"
        self.assertFalse(credit_card_validator(ae_short),
                         msg=''.format(credit_card_validator(ae_short)))

    # Verifies if AmEx with invalid lengths returns False
    # Picked using Category Partition Testing
    def test9_ae_length_long(self):
        # Check and prefix are valid; length is 16
        ae_long = "3722564865211458"
        self.assertFalse(credit_card_validator(ae_long),
                         msg=''.format(credit_card_validator(ae_long)))

    # Everything is valid

    # Verifies if Visa Cards with everything valid returns True
    # Picked using Category Partition Testing
    def test10_vs_valid(self):
        # Check and prefix are valid; length is 16
        vs_valid = "4282654865211424"
        self.assertTrue(credit_card_validator(vs_valid),
                        msg=''.format(credit_card_validator(vs_valid)))

    # Verifies if Master Cards with everything valid returns True
    # Picked using Category Partition Testing
    def test11_mc_51_55_valid(self):
        # Check and prefix are valid; length is 16
        mc_valid = "5282654865211413"
        self.assertTrue(credit_card_validator(mc_valid),
                        msg=''.format(credit_card_validator(mc_valid)))

    # Verifies if Master Cards with everything valid returns True
    # Picked using Category Partition Testing
    def test12_mc_2221_2720_valid(self):
        # Check and prefix are valid; length is 16
        mc_valid = "2222847589562356"
        self.assertTrue(credit_card_validator(mc_valid),
                        msg=''.format(credit_card_validator(mc_valid)))

    # Verifies if AmEx Cards with everything valid returns True
    # Picked using Category Partition Testing
    def test13_ae_34_valid(self):
        # Check and prefix are valid; length is 15
        ae_valid = "348265486521123"
        self.assertTrue(credit_card_validator(ae_valid),
                        msg=''.format(credit_card_validator(ae_valid)))

    # Verifies if AmEx Cards with everything valid returns True
    # Picked using Category Partition Testing
    def test14_ae_37_valid(self):
        # Check and prefix are valid; length is 15
        ae_valid = "378265486521126"
        self.assertTrue(credit_card_validator(ae_valid),
                        msg=''.format(credit_card_validator(ae_valid)))

    # Prefix related tests

    # Verifies if Visa Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test15_vs_low_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_l_prefix = "3999999999999998"
        self.assertFalse(credit_card_validator(vs_l_prefix),
                         msg=''.format(credit_card_validator(vs_l_prefix)))

    # Verifies if Visa Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test16_vs_upper_prefix(self):
        # Check and length are valid; prefix starts with 5 for visa
        # (but no conflicts with other ranges)
        vs_u_prefix = "5000000000000009"
        self.assertFalse(credit_card_validator(vs_u_prefix),
                         msg=''.format(credit_card_validator(vs_u_prefix)))

    # Verifies if Master Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test17_mc_51_55_low_prefix(self):
        # Check and length are valid; prefix starts with 50 for Master Card
        # (but no conflicts with other ranges)
        mc_l_prefix = "5099999999999992"
        self.assertFalse(credit_card_validator(mc_l_prefix),
                         msg=''.format(credit_card_validator(mc_l_prefix)))

    # Verifies if Master Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test18_mc_51_55_upper_prefix(self):
        # Check and length are valid; prefix starts with 56 for Master Card
        # (but no conflicts with other ranges)
        mc_u_prefix = "5600000000000003"
        self.assertFalse(credit_card_validator(mc_u_prefix),
                         msg=''.format(credit_card_validator(mc_u_prefix)))

    # Verifies if Master Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test19_mc_2221_2720_low_prefix(self):
        # Check and length are valid; prefix starts with 2220 for Master Card
        # (but no conflicts with other ranges)
        mc_l_prefix = "2220999999999991"
        self.assertFalse(credit_card_validator(mc_l_prefix),
                         msg=''.format(credit_card_validator(mc_l_prefix)))

    # Verifies if Master Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test20_mc_2221_2720_upper_prefix(self):
        # Check and length are valid; prefix starts with 2721 for Master Card
        # (but no conflicts with other ranges)
        mc_u_prefix = "2721000000000004"
        self.assertFalse(credit_card_validator(mc_u_prefix),
                         msg=''.format(credit_card_validator(mc_u_prefix)))

    # Verifies if AmEx Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test21_ae_34_low_prefix(self):
        # Check and length are valid; prefix starts with 33 for AmEx Card
        # (but no conflicts with other ranges)
        ae_l_prefix = "339999999999993"
        self.assertFalse(credit_card_validator(ae_l_prefix),
                         msg=''.format(credit_card_validator(ae_l_prefix)))

    # Verifies if AmEx Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test22_ae_34_upper_prefix(self):
        # Check and length are valid; prefix starts with 35 for AmEx Card
        # (but no conflicts with other ranges)
        ae_u_prefix = "350000000000006"
        self.assertFalse(credit_card_validator(ae_u_prefix),
                         msg=''.format(credit_card_validator(ae_u_prefix)))

    # Verifies if AmEx Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test23_ae_37_low_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        ae_l_prefix = "369999999999996"
        self.assertFalse(credit_card_validator(ae_l_prefix),
                         msg=''.format(credit_card_validator(ae_l_prefix)))

    # Verifies if AmEx Cards with invalid prefix, valid check and length
    # returns False
    # Picked using Boundary Testing
    def test24_ae_37_upper_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        ae_u_prefix = "380000000000000"
        self.assertFalse(credit_card_validator(ae_u_prefix),
                         msg=''.format(credit_card_validator(ae_u_prefix)))

    # Check digit related tests

    # Verifies if Visa Cards with invalid check, valid prefix and length
    # returns False
    # Picked using Category Partition Testing
    def test25_vs_check(self):
        vs_check = "4582654865211455"
        self.assertFalse(credit_card_validator(vs_check),
                         msg=''.format(credit_card_validator(vs_check)))

    # Verifies if Master Cards with invalid check, valid prefix and length
    # returns False
    # Picked using Category Partition Testing
    def test26_mc_51_55_check(self):
        vs_check = "5282654865211455"
        self.assertFalse(credit_card_validator(vs_check),
                         msg=''.format(credit_card_validator(vs_check)))

    # Verifies if Master Cards with invalid check, valid prefix and length
    # returns False
    # Picked using Category Partition Testing
    def test27_mc_2221_2720_check(self):
        vs_check = "2222654865211455"
        self.assertFalse(credit_card_validator(vs_check),
                         msg=''.format(credit_card_validator(vs_check)))

    # Verifies if AmEx Cards with invalid check, valid prefix and length
    # returns False
    # Picked using Category Partition Testing
    def test28_ae_34_check(self):
        vs_check = "342265486521146"
        self.assertFalse(credit_card_validator(vs_check),
                         msg=''.format(credit_card_validator(vs_check)))

    # Verifies if AmEx Cards with invalid check, valid prefix and length
    # returns False
    # Picked using Category Partition Testing
    def test29_ae_37_check(self):
        vs_check = "372265486521148"
        self.assertFalse(credit_card_validator(vs_check),
                         msg=''.format(credit_card_validator(vs_check)))

    # Inner boundary check

    # Verifies if Visa Cards boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test30_vs_low_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        vs_l_prefix = "4000000000000002"
        self.assertFalse(credit_card_validator(vs_l_prefix),
                         msg=''.format(credit_card_validator(vs_l_prefix)))

    # Verifies if Visa Cards boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test31_vs_upper_prefix(self):
        # Check and length are valid; prefix starts with 5 for visa
        # (but no conflicts with other ranges)
        vs_u_prefix = "4999999999999996"
        self.assertFalse(credit_card_validator(vs_u_prefix),
                         msg=''.format(credit_card_validator(vs_u_prefix)))

    # Verifies if Master Cards with boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test32_mc_51_55_low_prefix(self):
        # Check and length are valid; prefix starts with 50 for Master Card
        # (but no conflicts with other ranges)
        mc_l_prefix = "5100000000000008"
        self.assertTrue(credit_card_validator(mc_l_prefix),
                        msg=''.format(credit_card_validator(mc_l_prefix)))

    # Verifies if Master Cards boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test33_mc_51_55_upper_prefix(self):
        # Check and length are valid; prefix starts with 56 for Master Card
        # (but no conflicts with other ranges)
        mc_u_prefix = "5599999999999997"
        self.assertTrue(credit_card_validator(mc_u_prefix),
                        msg=''.format(credit_card_validator(mc_u_prefix)))

    # Verifies if Master Cards boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test34_mc_2221_2720_low_prefix(self):
        # Check and length are valid; prefix starts with 2220 for Master Card
        # (but no conflicts with other ranges)
        mc_l_prefix = "2221000000000009"
        self.assertTrue(credit_card_validator(mc_l_prefix),
                        msg=''.format(credit_card_validator(mc_l_prefix)))

    # Verifies if Master Cards boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test35_mc_2221_2720_upper_prefix(self):
        # Check and length are valid; prefix starts with 2721 for Master Card
        # (but no conflicts with other ranges)
        mc_u_prefix = "2720999999999996"
        self.assertTrue(credit_card_validator(mc_u_prefix),
                        msg=''.format(credit_card_validator(mc_u_prefix)))

    # Verifies if AmEx Cards boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test36_ae_34_low_prefix(self):
        # Check and length are valid; prefix starts with 33 for AmEx Card
        # (but no conflicts with other ranges)
        ae_l_prefix = "340000000000009"
        self.assertTrue(credit_card_validator(ae_l_prefix),
                        msg=''.format(credit_card_validator(ae_l_prefix)))

    # Verifies if AmEx Cards boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test37_ae_34_upper_prefix(self):
        # Check and length are valid; prefix starts with 35 for AmEx Card
        # (but no conflicts with other ranges)
        ae_u_prefix = "349999999999991"
        self.assertTrue(credit_card_validator(ae_u_prefix),
                        msg=''.format(credit_card_validator(ae_u_prefix)))

    # Verifies if AmEx Cards boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test38_ae_37_low_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        ae_l_prefix = "370000000000002"
        self.assertTrue(credit_card_validator(ae_l_prefix),
                        msg=''.format(credit_card_validator(ae_l_prefix)))

    # Verifies if AmEx Cards boundaries with everything else valid
    # returns True
    # Picked using Boundary Testing
    def test39_ae_37_upper_prefix(self):
        # Check and length are valid; prefix starts with 3 for visa
        # (but no conflicts with other ranges)
        ae_u_prefix = "379999999999994"
        self.assertFalse(credit_card_validator(ae_u_prefix),
                         msg=''.format(credit_card_validator(ae_u_prefix)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
