#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: keria(runchen.brc@alibaba-inc.com)
# @date: 2021/4/14
import datetime

import os

CONFS_FOLDER_NAME = u'confs'
HSEBS_OUTPUT_FOLDER = u'hsebs'


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def run_log(log):
        print(log)

    @staticmethod
    def calculate_days_diff(refer_year, refer_month, refer_day, target_year, target_month, target_day):
        refer_date = datetime.date(refer_year, refer_month, refer_day)
        target_date = datetime.date(target_year, target_month, target_day)
        diff = (target_date - refer_date).days
        return diff

    @staticmethod
    def get_project_full_path():
        current_folder_path = os.path.dirname(__file__)
        project_full_path = os.path.dirname(current_folder_path)
        return project_full_path

    @staticmethod
    def get_conf_folder_full_path():
        project_full_path = Utils.get_project_full_path()
        return os.path.join(project_full_path, CONFS_FOLDER_NAME)

    @staticmethod
    def get_hsebs_output_folder_full_path():
        project_full_path = Utils.get_project_full_path()
        return os.path.join(project_full_path, HSEBS_OUTPUT_FOLDER)

    @staticmethod
    def get_hseb_output_file_full_path(year):
        hsebs_output_folder_full_path = Utils.get_hsebs_output_folder_full_path()
        return os.path.join(hsebs_output_folder_full_path, u'hseb-%d.log' % year)
