#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# This file is part of PyZenKit package.
#
# Copyright (C) since 2016 CESNET, z.s.p.o (http://www.ces.net/)
# Copyright (C) since 2015 Jan Mach <honza.mach.ml@gmail.com>
# Use of this package is governed by the MIT license, see LICENSE file.
#
# This project was initially written for personal use of the original author. Later
# it was developed much further and used for project of author`s employer.
#-------------------------------------------------------------------------------


import unittest
from unittest.mock import Mock, MagicMock, call
from pprint import pformat, pprint

import os
import sys
import shutil
import datetime


# Generate the path to custom 'lib' directory
lib = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.insert(0, lib)

import pyzenkit.baseapp
import pyzenkit.zenscript


#
# Global variables
#
SCR_NAME      = 'test-zenscript.py'              # Name of the script process
CFG_FILE_NAME = '/tmp/{}.conf'.format(SCR_NAME)  # Name of the script configuration file
CFG_DIR_NAME  = '/tmp/{}'.format(SCR_NAME)       # Name of the script configuration directory


class TestPyzenkitZenScript(unittest.TestCase):

    def setUp(self):
        pyzenkit.baseapp.BaseApp.json_save(CFG_FILE_NAME, {'test': 'x'})
        try:
            os.mkdir(CFG_DIR_NAME)
        except FileExistsError:
            pass

        self.obj = pyzenkit.zenscript.DemoZenScript(
            name        = SCR_NAME,
            description = 'TestZenScript - Testing script'
        )
    def tearDown(self):
        os.remove(CFG_FILE_NAME)
        shutil.rmtree(CFG_DIR_NAME)

    def test_01_utils(self):
        """
        Perform the basic utility tests.
        """
        self.maxDiff = None

        self.obj.plugin()

        # Test the interval threshold calculations
        self.assertEqual(self.obj.calculate_interval_thresholds(time_high = 1454934631, interval = 'daily'), (datetime.datetime(2016, 2, 7, 12, 30, 31), datetime.datetime(2016, 2, 8, 12, 30, 31)))
        self.assertEqual(self.obj.calculate_interval_thresholds(time_high = 1454934631, interval = 'daily', adjust = True), (datetime.datetime(2016, 2, 7, 0, 0), datetime.datetime(2016, 2, 8, 0, 0)))

    def test_02_plugin(self):
        """
        Perform the basic operativity tests.
        """
        self.maxDiff = None

        self.obj.plugin()

if __name__ == "__main__":
    unittest.main()
