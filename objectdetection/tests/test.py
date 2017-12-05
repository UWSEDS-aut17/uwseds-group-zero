import sys
import os
sys.path.insert(0, '../submodule') # -- OK
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),"../submodule"))) -- ok

# print(os.path.abspath(os.path.join(os.path.dirname(__file__),"../submodule/appfunction")))
import appfunction as af


# test appfunction.py
import unittest
from urllib import request
import urllib


class utilsTest(unittest.TestCase):