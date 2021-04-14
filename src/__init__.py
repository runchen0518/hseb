#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: keria(runchen.brc@alibaba-inc.com)
# @date: 2021/4/14
import sys

from src.hseb import HSEB

if sys.version_info.major == 2:
    from imp import reload

    reload(sys)
    sys.setdefaultencoding('utf-8')


def main():
    year_from = 2019
    year_to = 2021
    hseb_handler = HSEB(range(year_from, year_to + 1, 1))
    hseb_handler.run()


if __name__ == '__main__':
    main()
