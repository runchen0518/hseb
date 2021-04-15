#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: keria(runchen.brc@alibaba-inc.com)
# @date: 2021/4/14
import os

import sys

import datetime

from src.utils import Utils

HEAVENLY_STEMS = [u'甲', u'乙', u'丙', u'丁', u'戊', u'己', u'庚', u'辛', u'壬', u'癸']
EARTHLY_BRANCHES = [u'子', u'丑', u'寅', u'卯', u'辰', u'巳', u'午', u'未', u'申', u'酉', u'戌', u'亥']

HSEB_CONF_FILE_NAME = u'hseb.ini'


class HSEB:
    def __init__(self, years):
        self.years = years

        result = HSEB.pre_process()
        self.anchor_year = result[0]
        self.anchor_year_first_hs = result[1]
        self.anchor_year_first_eb = result[2]

    def run(self):
        for year in self.years:
            contents = self.calculate_year_hsebs(year)
            self.write_to_files(year, contents)

    @staticmethod
    def pre_process():
        conf_folder_full_path = Utils.get_conf_folder_full_path()
        hseb_conf_file_full_path = os.path.join(conf_folder_full_path, HSEB_CONF_FILE_NAME)

        if not os.path.exists(hseb_conf_file_full_path) or not os.path.isfile(hseb_conf_file_full_path):
            Utils.run_log(u'conf file error! full path: %s' % hseb_conf_file_full_path)
            sys.exit(-11)

        with open(hseb_conf_file_full_path, 'r') as fp:
            for line in fp:
                results = line.strip().split()
                if len(results) != 2:
                    Utils.run_log(u'conf file line error! line: %s' % results)
                    sys.exit(-12)

                year_str = results[0]
                first_hseb = results[1]
                if not year_str.isdigit():
                    Utils.run_log(u'conf file year error! line: %s' % results)
                    sys.exit(-13)

                year_int = int(year_str)
                first_hseb = first_hseb.encode('utf-8')
                first_hs = first_hseb[:3]
                first_eb = first_hseb[3:]
                return year_int, first_hs, first_eb

    def calculate_year_hsebs(self, year):
        Utils.run_log(u'calculate year %d hsebs...' % year)
        result = self.calculate_day_hseb(year, 1, 1)
        first_hs = result[0]
        first_eb = result[1]

        hseb_position_result = HSEB.calculate_hseb_position(first_hs, first_eb)
        first_hs_position = hseb_position_result[0]
        first_eb_position = hseb_position_result[1]

        begin = datetime.date(year, 1, 1)
        end = datetime.date(year, 12, 31)

        contents = []
        for days_diff in range((end - begin).days + 1):
            day = begin + datetime.timedelta(days=days_diff)
            today = int(day.strftime("%w"))
            day_hs_position = HSEB.calculate_hs_position_by_days_diff(first_hs_position, days_diff)
            day_eb_position = HSEB.calculate_eb_position_by_days_diff(first_eb_position, days_diff)
            day_hseb = HSEB.get_hseb_by_position(day_hs_position, day_eb_position)
            day_hs = day_hseb[0]
            day_eb = day_hseb[1]
            line = u'%s\t%d\t%s%s' % (day, today, day_hs, day_eb)
            contents.append(line)
        return contents

    def calculate_day_hseb(self, year, month, day):
        days_diff = Utils.calculate_days_diff(self.anchor_year, 1, 1, year, month, day)

        hseb_position_result = HSEB.calculate_hseb_position(self.anchor_year_first_hs, self.anchor_year_first_eb)
        anchor_hs_position = hseb_position_result[0]
        anchor_eb_position = hseb_position_result[1]

        target_hs_position = HSEB.calculate_hs_position_by_days_diff(anchor_hs_position, days_diff)
        target_eb_position = HSEB.calculate_eb_position_by_days_diff(anchor_eb_position, days_diff)

        hseb = HSEB.get_hseb_by_position(target_hs_position, target_eb_position)
        target_hs = hseb[0]
        target_eb = hseb[1]
        return target_hs, target_eb

    @staticmethod
    def write_to_files(year, contents):
        hsebs_output_folder_full_path = Utils.get_hsebs_output_folder_full_path()
        if not os.path.exists(hsebs_output_folder_full_path):
            os.mkdir(hsebs_output_folder_full_path)

        hseb_output_file_full_path = Utils.get_hseb_output_file_full_path(year)
        if os.path.exists(hseb_output_file_full_path):
            Utils.run_log(u'remove old file...')
            os.remove(hseb_output_file_full_path)

        Utils.run_log(u'write to hseb file: %s' % hseb_output_file_full_path)
        with open(hseb_output_file_full_path, 'w') as fp:
            for line in contents:
                fp.write('%s\n' % line)
        Utils.run_log(u'done!')

    @staticmethod
    def calculate_hs_position_by_days_diff(anchor_hs_position, days_diff):
        return (anchor_hs_position + days_diff) % 10

    @staticmethod
    def calculate_eb_position_by_days_diff(anchor_eb_position, days_diff):
        return (anchor_eb_position + days_diff) % 12

    @staticmethod
    def calculate_hseb_position(anchor_hs, anchor_eb):
        anchor_hs_position = -1
        anchor_eb_position = -1
        for hs in HEAVENLY_STEMS:
            if hs == anchor_hs:
                anchor_hs_position = HEAVENLY_STEMS.index(hs)
                break
        for eb in EARTHLY_BRANCHES:
            if eb == anchor_eb:
                anchor_eb_position = EARTHLY_BRANCHES.index(eb)
                break

        if anchor_hs_position == -1:
            Utils.run_log(u'calculate hseb anchor hs position error!')
            sys.exit(-14)
        if anchor_eb_position == -1:
            Utils.run_log(u'calculate hseb anchor eb position error!')
            sys.exit(-15)
        return anchor_hs_position, anchor_eb_position

    @staticmethod
    def get_hseb_by_position(target_hs_position, target_eb_position):
        target_hs = HEAVENLY_STEMS[target_hs_position]
        target_eb = EARTHLY_BRANCHES[target_eb_position]
        return target_hs, target_eb
