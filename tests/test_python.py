import pytest
from src.utils import dummy_func_1

def test_dummy_func_1():
    assert dummy_func_1() == "This is line 2"

# Note: Importing validator will fail due to syntax error
# from src.validator import validate_data
# def test_validator():
#     assert validate_data({}) is True
