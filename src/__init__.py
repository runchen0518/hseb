#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: keria(runchen.brc@alibaba-inc.com)
# @date: 2021/4/14
import sys
from time import sleep

from src.hseb import HSEB
from src.utils import Utils
from src.wuye import Wuye

if sys.version_info.major == 2:
    from imp import reload

    reload(sys)
    sys.setdefaultencoding('utf-8')


def main():
    year_from = 2019
    year_to = 2023

    hseb(year_from=year_from, year_to=year_to)

    sleep(3.75)

    wuye(year_from=year_from, year_to=year_to)


def hseb(year_from, year_to):
    Utils.run_log('now start hseb...')
    hseb_handler = HSEB(range(year_from, year_to + 1, 1))
    hseb_handler.run()
    Utils.run_log('***  hseb success!   ***\n')


def wuye(year_from, year_to):
    Utils.run_log('now start wuye...')
    wuye_handler = Wuye(range(year_from, year_to + 1, 1))
    wuye_handler.run()
    Utils.run_log('***  wuye success!   ***\n')


if __name__ == '__main__':
    main()
