from os.path import abspath
from os.path import dirname
from os.path import join
import sys


def load_external_module(module):
    current = dirname(abspath(__file__))
    module_dir = join(dirname(current), module)
    sys.path.insert(0, module_dir)