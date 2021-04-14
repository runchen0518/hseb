#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: keria(runchen.brc@alibaba-inc.com)
# @date: 2021/4/14
import sys

from src.utils import Utils

BIG_MONTH = [1, 3, 5, 7, 8, 10, 12]
SMALL_MONTH = [4, 6, 9, 11]
FEBRUARY_MONTH = [2]

BIG_MONTH_DAYS_COUNT = 31
SMALL_MONTH_DAYS_COUNT = 30
LEAP_YEAR_FEBRUARY_DAYS_COUNT = 29
NON_LEAP_YEAR_FEBRUARY_DAYS_COUNT = 28


class YearDays:
    @staticmethod
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def __init__(self, year):
        self.year = year

    def get_month_days(self, month):
        if month in BIG_MONTH:
            days_count = BIG_MONTH_DAYS_COUNT
        elif month in SMALL_MONTH:
            days_count = SMALL_MONTH_DAYS_COUNT
        elif month in FEBRUARY_MONTH:
            leap = YearDays.is_leap(year=self.year)
            days_count = LEAP_YEAR_FEBRUARY_DAYS_COUNT if leap else NON_LEAP_YEAR_FEBRUARY_DAYS_COUNT
        else:
            Utils.run_log(u'month is error!')
            sys.exit(-1)
        Utils.run_log(u'year: %d, month: %d, days: %d' % (self.year, month, days_count))
        return range(1, days_count + 1)
