# -*- coding: utf-8 -*-


class _reiter(object):
    def __init__(self, f):
        self.f = f

    def __iter__(self):
        return self.f()


def prev_month(y, m):
    if m == 1:
        return (y - 1, 12)
    else:
        return (y, m - 1)


def next_month(y, m):
    if m == 12:
        return (y + 1, 1)
    else:
        return (y, m + 1)


def is_less_ym(ym1, ym2):
    y1, m1 = ym1
    y2, m2 = ym2

    if y1 < y2:
        return True
    elif y1 == y2 and m1 < m2:
        return True
    else:
        return False


def months(ym_start, ym_end, include_end=True):
    if include_end:
        ym_end = next_month(*ym_end)

    def _months():
        ym = ym_start
        while is_less_ym(ym, ym_end):
            yield ym
            ym = next_month(*ym)

    return _reiter(_months)


def is_leapyear(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False


def days_of_month(y, m):
    if m == 2:
        return (29 if is_leapyear(y) else 28)
    elif m in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        return 30


def next_day(y, m, d):
    if d == days_of_month(y, m):
        if m == 12:
            return (y + 1, 1, 1)
        else:
            return (y, m + 1, 1)
    else:
        return (y, m, d + 1)


def prev_day(y, m, d):
    if d == 1:
        if m == 1:
            return (y - 1, 12, 31)
        else:
            bm = m - 1
            return (y, bm, days_of_month(y, bm))
    else:
        return (y, m, d - 1)
