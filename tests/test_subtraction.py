from src.main import subtraction

def test_subtraction_basic():
    assert subtraction(5, 2) == 3

def test_subtraction_negatives():
    assert subtraction(-5, -2) == -3
