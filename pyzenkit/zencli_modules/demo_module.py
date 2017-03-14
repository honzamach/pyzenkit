#!/usr/bin/python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Copyright (C) 2015-2016 Jan Mach <honza.mach.ml@gmail.com>
# Use of this source is governed by the MIT license, see LICENSE file.
#-------------------------------------------------------------------------------

import sys
sys.path.insert(0, '..')

from zencli import ZenCLIModule

VERSION = "0.1-beta1"

class TestModule(ZenCLIModule):
    '''
    Base class for all pluggable ZenCLI modules
    '''
    def process(self):
        print("Process: Inside TestModule")

if __name__ == "__main__":
    module = TestModule()
    module.process()
    
