import sys
sys.path.append('src')

from utils import dummy_func_1

def test_dummy_func_1():
    assert dummy_func_1() == "This is line 2"