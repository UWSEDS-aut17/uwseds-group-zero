"""
Path magic to make tests' import work like a charm.
And without any pep8 complaints
"""

import os
import sys

sys.path.insert(0, '../')
sys.path.insert(1, '../../')