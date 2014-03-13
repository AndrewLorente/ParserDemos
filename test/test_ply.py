from unittest import TestCase
from nose.tools import eq_, raises

from ndn.ply import calculate

from ply.lex import LexError

class TestPlyParse(TestCase):
    def test_parse_a_single_number(self):
        eq_(1, calculate('1'))

    def test_parse_a_decimal_number(self):
        eq_(3.141, calculate('3.141'))

    @raises(LexError)
    def test_numbers_can_have_at_most_one_decimal_point(self):
        calculate('2.7.2')

    def test_parse_a_negative_number(self):
        eq_(-1, calculate('-1'))
