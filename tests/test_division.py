import pytest
from src.main import division

def test_division_basic():
    assert division(8, 2) == 4

def test_division_float():
    assert division(7, 2) == 3.5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(5, 0)
