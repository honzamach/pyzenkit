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

#
# Global variables
#
SCR_NAME       = 'test_baseapp.py'                # Name of the script process
JSON_FILE_NAME = '/tmp/script-state.json'         # Name of the test JSON file
CFG_FILE_NAME  = '/tmp/{}.conf'.format(SCR_NAME)  # Name of the script configuration file
CFG_DIR_NAME   = '/tmp/{}'.format(SCR_NAME)       # Name of the script configuration directory

class TestPyzenkitScript(unittest.TestCase):

    def setUp(self):
        pyzenkit.baseapp.BaseApp.json_save(CFG_FILE_NAME, {'test': 'x'})
        try:
            os.mkdir(CFG_DIR_NAME)
        except FileExistsError:
            pass

        self.obj = pyzenkit.baseapp._DemoBaseApp(
            name = SCR_NAME,
            path_cfg = '/tmp',
            path_log = '/tmp',
            path_tmp = '/tmp',
            path_run = '/tmp',
            description = 'DemoBaseApp - generic base script (DEMO)'
        )
    def tearDown(self):
        os.remove(CFG_FILE_NAME)
        shutil.rmtree(CFG_DIR_NAME)

    def test_01_utils(self):
        """
        Perform tests of generic script utils.
        """
        # Test the saving of JSON files
        self.assertEqual(self.obj.name, SCR_NAME)

        # Test the saving of JSON files
        self.assertTrue(self.obj.json_save(JSON_FILE_NAME, { "test": 1 }))

        # Test that the JSON file was really created
        self.assertTrue(os.path.isfile(JSON_FILE_NAME))

        # Test the loading of JSON files
        self.assertEqual(self.obj.json_load(JSON_FILE_NAME), { "test": 1 })

        # Remove the JSON file we are done with
        os.remove(JSON_FILE_NAME)

    def test_02_basic(self):
        """
        Perform the basic operativity tests.
        """
        self.obj.plugin()

if __name__ == "__main__":
    unittest.main()

