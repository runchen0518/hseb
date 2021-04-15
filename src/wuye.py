#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: keria(runchen.brc@alibaba-inc.com)
# @date: 2021/4/15
import os

import sys

from src.utils import Utils

WUYE_CONF_FILE_PATH = u'wuye.ini'
WUYE_OUTPUT_FOLDER = u'wuye'


class Wuye:
    def __init__(self, years):
        self.years = years
        self.wuyes = Wuye.pre_process()

    def run(self):
        for year in self.years:
            contents = self.calculate_year_wuye(year)
            self.write_to_files(year=year, contents=contents)

    def calculate_year_wuye(self, year):
        hseb_file_full_path = Utils.get_hseb_output_file_full_path(year)
        wuyes = []
        with open(hseb_file_full_path, 'r') as fp:
            for line in fp.readlines():
                line = line.strip()
                wuye = self.check_day(line)
                if wuye:
                    wuyes.append(line)
        return wuyes

    def check_day(self, line):
        result = line.split()
        hseb = result[2]
        return hseb in self.wuyes

    @staticmethod
    def write_to_files(year, contents):
        current_folder_path = os.path.dirname(__file__)
        project_path = os.path.dirname(current_folder_path)
        wuyes_output_folder_full_path = os.path.join(project_path, WUYE_OUTPUT_FOLDER)
        if not os.path.exists(wuyes_output_folder_full_path):
            os.mkdir(wuyes_output_folder_full_path)

        wuye_output_file_full_path = os.path.join(wuyes_output_folder_full_path, u'wuye-%d.log' % year)
        if os.path.exists(wuye_output_file_full_path):
            Utils.run_log(u'remove old file...')
            os.remove(wuye_output_file_full_path)

        Utils.run_log(u'write to wuye file: %s' % wuye_output_file_full_path)
        with open(wuye_output_file_full_path, 'w') as fp:
            fp.write('\n'.join(contents) + '\n')
        Utils.run_log(u'done!')

    @staticmethod
    def pre_process():
        conf_folder_full_path = Utils.get_conf_folder_full_path()
        wuye_conf_file_full_path = os.path.join(conf_folder_full_path, WUYE_CONF_FILE_PATH)
        if not os.path.exists(wuye_conf_file_full_path) or not os.path.isfile(wuye_conf_file_full_path):
            Utils.run_log(u'conf file error! full path: %s' % wuye_conf_file_full_path)
            sys.exit(-21)

        wuyes = []
        with open(wuye_conf_file_full_path, 'r') as fp:
            for line in fp:
                wuyes.append(line.strip())
        return wuyes
