#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'djn1'

import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import main

if __name__ == "__main__":
    main.run()



