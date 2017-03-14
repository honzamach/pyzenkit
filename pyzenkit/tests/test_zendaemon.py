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
import pyzenkit.zendaemon

#
# Global variables
#
DMN_NAME       = 'test_zendaemon.py'              # Name of the daemon process
JSON_FILE_NAME = '/tmp/daemon-state.json'         # Name of the test JSON file
CFG_FILE_NAME  = '/tmp/{}.conf'.format(DMN_NAME)  # Name of the daemon configuration file
CFG_DIR_NAME   = '/tmp/{}'.format(DMN_NAME)       # Name of the daemon configuration directory

class TestPyzenkitZenDaemon(unittest.TestCase):

    def setUp(self):
        pyzenkit.baseapp.BaseApp.json_save(CFG_FILE_NAME, {'test': 'x'})
        try:
            os.mkdir(CFG_DIR_NAME)
        except FileExistsError:
            pass

        self.obj = pyzenkit.zendaemon._DemoZenDaemon(
            name = DMN_NAME,
            path_cfg = '/tmp',
            path_log = '/tmp',
            path_tmp = '/tmp',
            path_run = '/tmp',
            description = 'DemoZenDaemon - generic daemon (DEMO)',
            schedule = [('default',)],
            components = [
                pyzenkit.zendaemon._DemoDaemonComponent()
            ]
        )
    def tearDown(self):
        os.remove(CFG_FILE_NAME)
        shutil.rmtree(CFG_DIR_NAME)

    def test_01_basic(self):
        """
        Perform the basic operativity tests.
        """
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
