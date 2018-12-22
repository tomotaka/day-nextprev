# - *- coding: utf-8 -*-
from unittest import TestCase
from nose.tools import ok_, eq_

from daynextprev import (
    prev_month,
    next_month,
    is_leapyear,
    days_of_month,
    next_day,
    prev_day
)


class DayNextPrevTestCase(TestCase):
    def test_prev_month(self):
        eq_((2017, 12), prev_month(2018, 1))
        eq_((2018, 1), prev_month(2018, 2))
        eq_((2018, 2), prev_month(2018, 3))
        eq_((2018, 3), prev_month(2018, 4))
        eq_((2018, 4), prev_month(2018, 5))
        eq_((2018, 5), prev_month(2018, 6))
        eq_((2018, 6), prev_month(2018, 7))
        eq_((2018, 7), prev_month(2018, 8))
        eq_((2018, 8), prev_month(2018, 9))
        eq_((2018, 9), prev_month(2018, 10))
        eq_((2018, 10), prev_month(2018, 11))
        eq_((2018, 11), prev_month(2018, 12))

    def test_next_month(self):
        eq_((2018, 2), next_month(2018, 1))
        eq_((2018, 3), next_month(2018, 2))
        eq_((2018, 4), next_month(2018, 3))
        eq_((2018, 5), next_month(2018, 4))
        eq_((2018, 6), next_month(2018, 5))
        eq_((2018, 7), next_month(2018, 6))
        eq_((2018, 8), next_month(2018, 7))
        eq_((2018, 9), next_month(2018, 8))
        eq_((2018, 10), next_month(2018, 9))
        eq_((2018, 11), next_month(2018, 10))
        eq_((2018, 12), next_month(2018, 11))
        eq_((2019, 1), next_month(2018, 12))

    def test_is_leapyear(self):
        # leap year (y % 400 == 0)
        ok_(is_leapyear(1600))
        ok_(is_leapyear(2000))
        ok_(is_leapyear(2400))

        # NOT leap year (y % 100 == 0)
        ok_(not is_leapyear(1700))
        ok_(not is_leapyear(1800))
        ok_(not is_leapyear(1900))
        ok_(not is_leapyear(2100))
        ok_(not is_leapyear(2200))
        ok_(not is_leapyear(2300))

        # leap year (y % 4 == 0)
        ok_(is_leapyear(1704))
        ok_(is_leapyear(1784))
        ok_(is_leapyear(1820))
        ok_(is_leapyear(1896))
        ok_(is_leapyear(1912))
        ok_(is_leapyear(1924))
        ok_(is_leapyear(2004))
        ok_(is_leapyear(2056))

        # NOT leap year
        ok_(not is_leapyear(1711))
        ok_(not is_leapyear(1757))
        ok_(not is_leapyear(1791))

        ok_(not is_leapyear(1805))
        ok_(not is_leapyear(1822))
        ok_(not is_leapyear(1861))

        ok_(not is_leapyear(1918))
        ok_(not is_leapyear(1942))
        ok_(not is_leapyear(1997))

        ok_(not is_leapyear(2035))
        ok_(not is_leapyear(2078))
        ok_(not is_leapyear(2095))

        ok_(not is_leapyear(2101))
        ok_(not is_leapyear(2149))
        ok_(not is_leapyear(2189))

    def test_days_of_month(self):
        eq_(29, days_of_month(2016, 2))
        eq_(28, days_of_month(2015, 2))
        eq_(29, days_of_month(2000, 2))
        eq_(28, days_of_month(1900, 2))

        eq_(31, days_of_month(2017, 1))
        eq_(28, days_of_month(2017, 2))
        eq_(31, days_of_month(2017, 3))
        eq_(30, days_of_month(2017, 4))
        eq_(31, days_of_month(2017, 5))
        eq_(30, days_of_month(2017, 6))
        eq_(31, days_of_month(2017, 7))
        eq_(31, days_of_month(2017, 8))
        eq_(30, days_of_month(2017, 9))
        eq_(31, days_of_month(2017, 10))
        eq_(30, days_of_month(2017, 11))
        eq_(31, days_of_month(2017, 12))

    def test_next_day(self):
        eq_((2016, 2, 28), next_day(2016, 2, 27))
        eq_((2016, 2, 29), next_day(2016, 2, 28))
        eq_((2016, 3, 1), next_day(2016, 2, 29))

        eq_((2015, 2, 28), next_day(2015, 2, 27))
        eq_((2015, 3, 1), next_day(2015, 2, 28))

        eq_((2000, 2, 28), next_day(2000, 2, 27))
        eq_((2000, 2, 29), next_day(2000, 2, 28))
        eq_((2000, 3, 1), next_day(2000, 2, 29))

        eq_((1900, 2, 28), next_day(1900, 2, 27))
        eq_((1900, 3, 1), next_day(1900, 2, 28))

        eq_((2017, 1, 1), next_day(2016, 12, 31))
        eq_((2017, 2, 1), next_day(2017, 1, 31))
        eq_((2017, 3, 1), next_day(2017, 2, 28))
        eq_((2017, 4, 1), next_day(2017, 3, 31))
        eq_((2017, 5, 1), next_day(2017, 4, 30))
        eq_((2017, 6, 1), next_day(2017, 5, 31))
        eq_((2017, 7, 1), next_day(2017, 6, 30))
        eq_((2017, 7, 31), next_day(2017, 7, 30))
        eq_((2017, 8, 1), next_day(2017, 7, 31))
        eq_((2017, 9, 1), next_day(2017, 8, 31))
        eq_((2017, 10, 1), next_day(2017, 9, 30))
        eq_((2017, 11, 1), next_day(2017, 10, 31))
        eq_((2017, 12, 1), next_day(2017, 11, 30))
        eq_((2017, 12, 31), next_day(2017, 12, 30))
        eq_((2018, 1, 1), next_day(2017, 12, 31))

        eq_((2017, 5, 13), next_day(2017, 5, 12))
        eq_((2017, 5, 14), next_day(2017, 5, 13))
        eq_((2017, 5, 15), next_day(2017, 5, 14))
        eq_((2017, 5, 16), next_day(2017, 5, 15))

    def test_prev_day(self):
        eq_((2016, 2, 27), prev_day(2016, 2, 28))
        eq_((2016, 2, 28), prev_day(2016, 2, 29))
        eq_((2016, 2, 29), prev_day(2016, 3, 1))

        eq_((2015, 2, 27), prev_day(2015, 2, 28))
        eq_((2015, 2, 28), prev_day(2015, 3, 1))

        eq_((2000, 2, 27), prev_day(2000, 2, 28))
        eq_((2000, 2, 28), prev_day(2000, 2, 29))
        eq_((2000, 2, 29), prev_day(2000, 3, 1))

        eq_((1900, 2, 27), prev_day(1900, 2, 28))
        eq_((1900, 2, 28), prev_day(1900, 3, 1))

        eq_((2016, 12, 31), prev_day(2017, 1, 1))
        eq_((2017, 1, 31), prev_day(2017, 2, 1))
        eq_((2017, 2, 28), prev_day(2017, 3, 1))
        eq_((2017, 3, 31), prev_day(2017, 4, 1))
        eq_((2017, 4, 30), prev_day(2017, 5, 1))
        eq_((2017, 5, 31), prev_day(2017, 6, 1))
        eq_((2017, 6, 30), prev_day(2017, 7, 1))
        eq_((2017, 7, 30), prev_day(2017, 7, 31))
        eq_((2017, 7, 31), prev_day(2017, 8, 1))
        eq_((2017, 8, 31), prev_day(2017, 9, 1))
        eq_((2017, 9, 30), prev_day(2017, 10, 1))
        eq_((2017, 10, 31), prev_day(2017, 11, 1))
        eq_((2017, 11, 30), prev_day(2017, 12, 1))
        eq_((2017, 12, 30), prev_day(2017, 12, 31))
        eq_((2017, 12, 31), prev_day(2018, 1, 1))

        eq_((2017, 5, 12), prev_day(2017, 5, 13))
        eq_((2017, 5, 13), prev_day(2017, 5, 14))
        eq_((2017, 5, 14), prev_day(2017, 5, 15))
        eq_((2017, 5, 15), prev_day(2017, 5, 16))
