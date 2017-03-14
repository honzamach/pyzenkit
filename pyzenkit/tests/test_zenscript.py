#!/usr/bin/python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Copyright (C) since 2016 Jan Mach <honza.mach.ml@gmail.com>
# Use of this source is governed by the MIT license, see LICENSE file.
#-------------------------------------------------------------------------------

import unittest
from unittest.mock import Mock, MagicMock, call
from pprint import pformat, pprint

import os
import sys
import shutil

# Generate the path to custom 'lib' directory
lib = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.insert(0, lib)

import pyzenkit.baseapp
import pyzenkit.zenscript

#
# Global variables
#
SCR_NAME       = 'test_zenscript.py'              # Name of the script process
JSON_FILE_NAME = '/tmp/daemon-state.json'         # Name of the test JSON file
CFG_FILE_NAME  = '/tmp/{}.conf'.format(SCR_NAME)  # Name of the script configuration file
CFG_DIR_NAME   = '/tmp/{}'.format(SCR_NAME)       # Name of the script configuration directory

class TestPyzenkitZenScript(unittest.TestCase):

    def setUp(self):
        pyzenkit.baseapp.BaseApp.json_save(CFG_FILE_NAME, {'test': 'x'})
        try:
            os.mkdir(CFG_DIR_NAME)
        except FileExistsError:
            pass

        self.obj = pyzenkit.zenscript._DemoZenScript(
            name = SCR_NAME,
            path_cfg = '/tmp',
            path_log = '/tmp',
            path_tmp = '/tmp',
            path_run = '/tmp',
            description = 'DemoZenScript - generic script (DEMO)'
        )
    def tearDown(self):
        os.remove(CFG_FILE_NAME)
        shutil.rmtree(CFG_DIR_NAME)

    def test_01_utils(self):
        """
        Perform the basic utility tests.
        """

        # Test the interval threshold calculations
        self.assertEqual(self.obj.calculate_interval_thresholds('daily', time_cur = 1454934631), (1454848231, 1454934631))
        self.assertEqual(self.obj.calculate_interval_thresholds('daily', time_cur = 1454934631, flag_floor = True), (1454803200, 1454889600))

    def test_02_basic(self):
        """
        Perform the basic operativity tests.
        """
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
