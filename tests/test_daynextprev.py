# - *- coding: utf-8 -*-
from unittest import TestCase
from nose.tools import ok_, eq_

from datetime import date

from daynextprev import (
    prev_month,
    next_month,
    is_less_ym,
    months,
    months_backward,
    is_leapyear,
    days_of_month,
    next_day,
    prev_day,
    days,
    days_backward,
    this_week,
    next_week,
    prev_week,
    W_MONDAY,
    W_TUESDAY,
    W_WEDNESDAY,
    W_THURSDAY,
    W_FRIDAY,
    W_SATURDAY,
    W_SUNDAY
)


class DayNextPrevTestCase(TestCase):

    def test_constants(self):
        eq_(0, W_MONDAY)
        eq_(1, W_TUESDAY)
        eq_(2, W_WEDNESDAY)
        eq_(3, W_THURSDAY)
        eq_(4, W_FRIDAY)
        eq_(5, W_SATURDAY)
        eq_(6, W_SUNDAY)

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

    def test_is_less_ym(self):
        # ym1 < ym2
        ok_(is_less_ym((2018, 1), (2018, 2)))
        ok_(is_less_ym((2015, 10), (2017, 3)))

        # ym1 == ym2
        ok_(not is_less_ym((2018, 1), (2018, 1)))
        ok_(not is_less_ym((2000, 3), (2000, 3)))

        # ym1 > ym2
        ok_(not is_less_ym((2018, 2), (2018, 1)))
        ok_(not is_less_ym((2015, 10), (2014, 12)))

    def test_months(self):
        months1 = months((2018, 1), (2018, 5), include_end=True)

        months1_1 = []
        for ym in months1:
            months1_1.append(ym)

        eq_(
            [
                (2018, 1),
                (2018, 2),
                (2018, 3),
                (2018, 4),
                (2018, 5)
            ],
            months1_1
        )

        months1_2 = []
        for ym in months1:
            months1_2.append(ym)

        eq_(
            [
                (2018, 1),
                (2018, 2),
                (2018, 3),
                (2018, 4),
                (2018, 5)
            ],
            months1_2
        )

        months2 = list(months((2018, 1), (2018, 5), include_end=False))
        eq_(
            [
                (2018, 1),
                (2018, 2),
                (2018, 3),
                (2018, 4)
            ],
            months2
        )

        months3 = list(months((2018, 2), (2018, 6)))
        eq_(
            [
                (2018, 2),
                (2018, 3),
                (2018, 4),
                (2018, 5),
                (2018, 6)
            ],
            months3
        )

    def test_months_backward(self):
        months1 = months_backward((2018, 2), (2017, 11), include_end=True)
        months1_1 = []
        for ym in months1:
            months1_1.append(ym)

        eq_(
            [
                (2018, 2),
                (2018, 1),
                (2017, 12),
                (2017, 11)
            ],
            months1_1
        )

        months1_2 = list(months1)

        eq_(
            [
                (2018, 2),
                (2018, 1),
                (2017, 12),
                (2017, 11)
            ],
            months1_2
        )

        months2 = list(months_backward((2018, 2), (2017, 11), include_end=False))
        eq_(
            [
                (2018, 2),
                (2018, 1),
                (2017, 12)
            ],
            months2
        )

        months3 = list(months_backward((2018, 3), (2018 ,1)))
        eq_(
            [
                (2018, 3),
                (2018, 2),
                (2018, 1)
            ],
            months3
        )

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
        eq_(date(2016, 2, 28), next_day(date(2016, 2, 27)))
        eq_((2016, 2, 29), next_day(2016, 2, 28))
        eq_(date(2016, 2, 29), next_day(date(2016, 2, 28)))
        eq_((2016, 3, 1), next_day(2016, 2, 29))
        eq_(date(2016, 3, 1), next_day(date(2016, 2, 29)))

        eq_((2015, 2, 28), next_day(2015, 2, 27))
        eq_(date(2015, 2, 28), next_day(date(2015, 2, 27)))
        eq_((2015, 3, 1), next_day(2015, 2, 28))
        eq_(date(2015, 3, 1), next_day(date(2015, 2, 28)))

        eq_((2000, 2, 28), next_day(2000, 2, 27))
        eq_(date(2000, 2, 28), next_day(date(2000, 2, 27)))
        eq_((2000, 2, 29), next_day(2000, 2, 28))
        eq_(date(2000, 2, 29), next_day(date(2000, 2, 28)))
        eq_((2000, 3, 1), next_day(2000, 2, 29))
        eq_(date(2000, 3, 1), next_day(date(2000, 2, 29)))

        eq_((1900, 2, 28), next_day(1900, 2, 27))
        eq_(date(1900, 2, 28), next_day(date(1900, 2, 27)))
        eq_((1900, 3, 1), next_day(1900, 2, 28))
        eq_(date(1900, 3, 1), next_day(date(1900, 2, 28)))

        eq_((2017, 1, 1), next_day(2016, 12, 31))
        eq_(date(2017, 1, 1), next_day(date(2016, 12, 31)))
        eq_((2017, 2, 1), next_day(2017, 1, 31))
        eq_(date(2017, 2, 1), next_day(date(2017, 1, 31)))
        eq_((2017, 3, 1), next_day(2017, 2, 28))
        eq_(date(2017, 3, 1), next_day(date(2017, 2, 28)))
        eq_((2017, 4, 1), next_day(2017, 3, 31))
        eq_(date(2017, 4, 1), next_day(date(2017, 3, 31)))
        eq_((2017, 5, 1), next_day(2017, 4, 30))
        eq_(date(2017, 5, 1), next_day(date(2017, 4, 30)))
        eq_((2017, 6, 1), next_day(2017, 5, 31))
        eq_(date(2017, 6, 1), next_day(date(2017, 5, 31)))
        eq_((2017, 7, 1), next_day(2017, 6, 30))
        eq_(date(2017, 7, 1), next_day(date(2017, 6, 30)))
        eq_((2017, 7, 31), next_day(2017, 7, 30))
        eq_(date(2017, 7, 31), next_day(date(2017, 7, 30)))
        eq_((2017, 8, 1), next_day(2017, 7, 31))
        eq_(date(2017, 8, 1), next_day(date(2017, 7, 31)))
        eq_((2017, 9, 1), next_day(2017, 8, 31))
        eq_(date(2017, 9, 1), next_day(date(2017, 8, 31)))
        eq_((2017, 10, 1), next_day(2017, 9, 30))
        eq_(date(2017, 10, 1), next_day(date(2017, 9, 30)))
        eq_((2017, 11, 1), next_day(2017, 10, 31))
        eq_(date(2017, 11, 1), next_day(date(2017, 10, 31)))
        eq_((2017, 12, 1), next_day(2017, 11, 30))
        eq_(date(2017, 12, 1), next_day(date(2017, 11, 30)))
        eq_((2017, 12, 31), next_day(2017, 12, 30))
        eq_(date(2017, 12, 31), next_day(date(2017, 12, 30)))
        eq_((2018, 1, 1), next_day(2017, 12, 31))
        eq_(date(2018, 1, 1), next_day(date(2017, 12, 31)))

        eq_((2017, 5, 13), next_day(2017, 5, 12))
        eq_(date(2017, 5, 13), next_day(date(2017, 5, 12)))
        eq_((2017, 5, 14), next_day(2017, 5, 13))
        eq_(date(2017, 5, 14), next_day(date(2017, 5, 13)))
        eq_((2017, 5, 15), next_day(2017, 5, 14))
        eq_(date(2017, 5, 15), next_day(date(2017, 5, 14)))
        eq_((2017, 5, 16), next_day(2017, 5, 15))
        eq_(date(2017, 5, 16), next_day(date(2017, 5, 15)))

    def test_prev_day(self):
        eq_((2016, 2, 27), prev_day(2016, 2, 28))
        eq_(date(2016, 2, 27), prev_day(date(2016, 2, 28)))
        eq_((2016, 2, 28), prev_day(2016, 2, 29))
        eq_(date(2016, 2, 28), prev_day(date(2016, 2, 29)))
        eq_((2016, 2, 29), prev_day(2016, 3, 1))
        eq_(date(2016, 2, 29), prev_day(date(2016, 3, 1)))

        eq_((2015, 2, 27), prev_day(2015, 2, 28))
        eq_(date(2015, 2, 27), prev_day(date(2015, 2, 28)))
        eq_((2015, 2, 28), prev_day(2015, 3, 1))
        eq_(date(2015, 2, 28), prev_day(date(2015, 3, 1)))

        eq_((2000, 2, 27), prev_day(2000, 2, 28))
        eq_(date(2000, 2, 27), prev_day(date(2000, 2, 28)))
        eq_((2000, 2, 28), prev_day(2000, 2, 29))
        eq_(date(2000, 2, 28), prev_day(date(2000, 2, 29)))
        eq_((2000, 2, 29), prev_day(2000, 3, 1))
        eq_(date(2000, 2, 29), prev_day(date(2000, 3, 1)))

        eq_((1900, 2, 27), prev_day(1900, 2, 28))
        eq_(date(1900, 2, 27), prev_day(date(1900, 2, 28)))
        eq_((1900, 2, 28), prev_day(1900, 3, 1))
        eq_(date(1900, 2, 28), prev_day(date(1900, 3, 1)))

        eq_((2016, 12, 31), prev_day(2017, 1, 1))
        eq_(date(2016, 12, 31), prev_day(date(2017, 1, 1)))
        eq_((2017, 1, 31), prev_day(2017, 2, 1))
        eq_(date(2017, 1, 31), prev_day(date(2017, 2, 1)))
        eq_((2017, 2, 28), prev_day(2017, 3, 1))
        eq_(date(2017, 2, 28), prev_day(date(2017, 3, 1)))
        eq_((2017, 3, 31), prev_day(2017, 4, 1))
        eq_(date(2017, 3, 31), prev_day(date(2017, 4, 1)))
        eq_((2017, 4, 30), prev_day(2017, 5, 1))
        eq_(date(2017, 4, 30), prev_day(date(2017, 5, 1)))
        eq_((2017, 5, 31), prev_day(2017, 6, 1))
        eq_(date(2017, 5, 31), prev_day(date(2017, 6, 1)))
        eq_((2017, 6, 30), prev_day(2017, 7, 1))
        eq_(date(2017, 6, 30), prev_day(date(2017, 7, 1)))
        eq_((2017, 7, 30), prev_day(2017, 7, 31))
        eq_(date(2017, 7, 30), prev_day(date(2017, 7, 31)))
        eq_((2017, 7, 31), prev_day(2017, 8, 1))
        eq_(date(2017, 7, 31), prev_day(date(2017, 8, 1)))
        eq_((2017, 8, 31), prev_day(2017, 9, 1))
        eq_(date(2017, 8, 31), prev_day(date(2017, 9, 1)))
        eq_((2017, 9, 30), prev_day(2017, 10, 1))
        eq_(date(2017, 9, 30), prev_day(date(2017, 10, 1)))
        eq_((2017, 10, 31), prev_day(2017, 11, 1))
        eq_(date(2017, 10, 31), prev_day(date(2017, 11, 1)))
        eq_((2017, 11, 30), prev_day(2017, 12, 1))
        eq_(date(2017, 11, 30), prev_day(date(2017, 12, 1)))
        eq_((2017, 12, 30), prev_day(2017, 12, 31))
        eq_(date(2017, 12, 30), prev_day(date(2017, 12, 31)))
        eq_((2017, 12, 31), prev_day(2018, 1, 1))
        eq_(date(2017, 12, 31), prev_day(date(2018, 1, 1)))

        eq_((2017, 5, 12), prev_day(2017, 5, 13))
        eq_(date(2017, 5, 12), prev_day(date(2017, 5, 13)))
        eq_((2017, 5, 13), prev_day(2017, 5, 14))
        eq_(date(2017, 5, 13), prev_day(date(2017, 5, 14)))
        eq_((2017, 5, 14), prev_day(2017, 5, 15))
        eq_(date(2017, 5, 14), prev_day(date(2017, 5, 15)))
        eq_((2017, 5, 15), prev_day(2017, 5, 16))
        eq_(date(2017, 5, 15), prev_day(date(2017, 5, 16)))

    def test_days(self):
        days1 = days((2018, 1, 30), (2018, 2, 3), include_end=True)
        days1_1 = []
        for d in days1:
            days1_1.append(d)

        eq_(
            [
                (2018, 1, 30),
                (2018, 1, 31),
                (2018, 2, 1),
                (2018, 2, 2),
                (2018, 2, 3)
            ],
            days1_1
        )

        days1_2 = list(days1)
        eq_(
            [
                (2018, 1, 30),
                (2018, 1, 31),
                (2018, 2, 1),
                (2018, 2, 2),
                (2018, 2, 3)
            ],
            days1_2
        )

        days2 = days((2018, 1, 30), (2018, 2, 3))
        days2_1 = list(days2)
        eq_(
            [
                (2018, 1, 30),
                (2018, 1, 31),
                (2018, 2, 1),
                (2018, 2, 2),
                (2018, 2, 3)
            ],
            days2_1
        )

        days3 = days(date(2020, 2, 26), date(2020, 3, 2), include_end=False)
        days3_1 = list(days3)
        eq_(
            [
                date(2020, 2, 26),
                date(2020, 2, 27),
                date(2020, 2, 28),
                date(2020, 2, 29),
                date(2020, 3, 1)
            ],
            days3_1
        )

        days3_2 = []
        for d in days3:
            days3_2.append(d)

        eq_(
            [
                date(2020, 2, 26),
                date(2020, 2, 27),
                date(2020, 2, 28),
                date(2020, 2, 29),
                date(2020, 3, 1)
            ],
            days3_2
        )

        days4 = days(date(2020, 2, 26), date(2020, 3, 2))
        days4_1 = list(days4)
        eq_(
            [
                date(2020, 2, 26),
                date(2020, 2, 27),
                date(2020, 2, 28),
                date(2020, 2, 29),
                date(2020, 3, 1),
                date(2020, 3, 2)
            ],
            days4_1
        )

    def test_days_backward(self):
        days1 = days_backward((2018, 5, 4), (2018, 4, 27), include_end=True)
        days1_1 = []
        for d in days1:
            days1_1.append(d)

        eq_(
            [
                (2018, 5, 4),
                (2018, 5, 3),
                (2018, 5, 2),
                (2018, 5, 1),
                (2018, 4, 30),
                (2018, 4, 29),
                (2018, 4, 28),
                (2018, 4, 27)
            ],
            days1_1
        )

        days1_2 = list(days1)
        eq_(
            [
                (2018, 5, 4),
                (2018, 5, 3),
                (2018, 5, 2),
                (2018, 5, 1),
                (2018, 4, 30),
                (2018, 4, 29),
                (2018, 4, 28),
                (2018, 4, 27)
            ],
            days1_2
        )

        days2 = days_backward((2018, 5, 4), (2018, 4, 27), include_end=False)
        days2_1 = list(days2)
        eq_(
            [
                (2018, 5, 4),
                (2018, 5, 3),
                (2018, 5, 2),
                (2018, 5, 1),
                (2018, 4, 30),
                (2018, 4, 29),
                (2018, 4, 28)
            ],
            days2_1
        )

        days3 = days_backward((2018, 5, 4), (2018, 4, 27))
        days3_1 = list(days3)
        eq_(
            [
                (2018, 5, 4),
                (2018, 5, 3),
                (2018, 5, 2),
                (2018, 5, 1),
                (2018, 4, 30),
                (2018, 4, 29),
                (2018, 4, 28),
                (2018, 4, 27)
            ],
            days3_1
        )

        days4 = days_backward(date(2020, 3, 8), date(2020, 2, 19), include_end=True)
        days4_1 = []
        for d in days4:
            days4_1.append(d)
        eq_(
            [
                date(2020, 3, 8),
                date(2020, 3, 7),
                date(2020, 3, 6),
                date(2020, 3, 5),
                date(2020, 3, 4),
                date(2020, 3, 3),
                date(2020, 3, 2),
                date(2020, 3, 1),
                date(2020, 2, 29),
                date(2020, 2, 28),
                date(2020, 2, 27),
                date(2020, 2, 26),
                date(2020, 2, 25),
                date(2020, 2, 24),
                date(2020, 2, 23),
                date(2020, 2, 22),
                date(2020, 2, 21),
                date(2020, 2, 20),
                date(2020, 2, 19)
            ],
            days4_1
        )

        days4_2 = list(days4)
        eq_(
            [
                date(2020, 3, 8),
                date(2020, 3, 7),
                date(2020, 3, 6),
                date(2020, 3, 5),
                date(2020, 3, 4),
                date(2020, 3, 3),
                date(2020, 3, 2),
                date(2020, 3, 1),
                date(2020, 2, 29),
                date(2020, 2, 28),
                date(2020, 2, 27),
                date(2020, 2, 26),
                date(2020, 2, 25),
                date(2020, 2, 24),
                date(2020, 2, 23),
                date(2020, 2, 22),
                date(2020, 2, 21),
                date(2020, 2, 20),
                date(2020, 2, 19)
            ],
            days4_2
        )

        days5 = days_backward(date(2020, 3, 8), date(2020, 2, 19), include_end=False)
        days5_1 = list(days5)
        eq_(
            [
                date(2020, 3, 8),
                date(2020, 3, 7),
                date(2020, 3, 6),
                date(2020, 3, 5),
                date(2020, 3, 4),
                date(2020, 3, 3),
                date(2020, 3, 2),
                date(2020, 3, 1),
                date(2020, 2, 29),
                date(2020, 2, 28),
                date(2020, 2, 27),
                date(2020, 2, 26),
                date(2020, 2, 25),
                date(2020, 2, 24),
                date(2020, 2, 23),
                date(2020, 2, 22),
                date(2020, 2, 21),
                date(2020, 2, 20)
            ],
            days5_1
        )

        days6 = days_backward(date(2020, 3, 8), date(2020, 2, 19))
        days6_1 = list(days6)
        eq_(
            [
                date(2020, 3, 8),
                date(2020, 3, 7),
                date(2020, 3, 6),
                date(2020, 3, 5),
                date(2020, 3, 4),
                date(2020, 3, 3),
                date(2020, 3, 2),
                date(2020, 3, 1),
                date(2020, 2, 29),
                date(2020, 2, 28),
                date(2020, 2, 27),
                date(2020, 2, 26),
                date(2020, 2, 25),
                date(2020, 2, 24),
                date(2020, 2, 23),
                date(2020, 2, 22),
                date(2020, 2, 21),
                date(2020, 2, 20),
                date(2020, 2, 19)
            ],
            days6_1
        )

    def test_this_week(self):
        d1 = date(2018, 1, 1)  # monday
        eq_(date(2018, 1,1), this_week(d1))
        eq_(date(2018, 1,1), this_week(d1, week_start=W_MONDAY))
        eq_(date(2017, 12, 31), this_week(d1, week_start=W_SUNDAY))
        eq_(date(2017, 12, 30), this_week(d1, week_start=W_SATURDAY))
        eq_(date(2017, 12, 29), this_week(d1, week_start=W_FRIDAY))
        eq_(date(2017, 12, 28), this_week(d1, week_start=W_THURSDAY))
        eq_(date(2017, 12, 27), this_week(d1, week_start=W_WEDNESDAY))
        eq_(date(2017, 12, 26), this_week(d1, week_start=W_TUESDAY))

    def test_next_week(self):
        d1 = date(2018, 1, 1)  # monday
        eq_(date(2018, 1, 8), next_week(d1))
        eq_(date(2018, 1, 8), next_week(d1, week_start=W_MONDAY))

        d2 = date(2019, 1, 3)  # thursday
        eq_(date(2019, 1, 8), next_week(d2, week_start=W_TUESDAY))

        d3 = date(2019, 2, 6)  # wednesday
        eq_(date(2019, 2, 10), next_week(d3, week_start=W_SUNDAY))

    def test_prev_week(self):
        d1 = date(2018, 1, 1)  # monday
        eq_(date(2017, 12, 25), prev_week(d1))
        eq_(date(2017, 12, 25), prev_week(d1, week_start=W_MONDAY))

        d2 = date(2019, 1, 3)  # thursday
        eq_(date(2018, 12, 25), prev_week(d2, week_start=W_TUESDAY))

        d3 = date(2019, 2, 6)  # wednesday
        eq_(date(2019, 1, 27), prev_week(d3, week_start=W_SUNDAY))
