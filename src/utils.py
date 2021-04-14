#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: keria(runchen.brc@alibaba-inc.com)
# @date: 2021/4/14
import datetime


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def run_log(log):
        print log

    @staticmethod
    def calculate_days_diff(refer_year, refer_month, refer_day, target_year, target_month, target_day):
        refer_date = datetime.date(refer_year, refer_month, refer_day)
        target_date = datetime.date(target_year, target_month, target_day)
        diff = (target_date - refer_date).days
        return diff
