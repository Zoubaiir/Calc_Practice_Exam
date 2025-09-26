from src.main import addition

def test_addition_basic():
    assert addition(2, 3) == 5

def test_addition_negatives():
    assert addition(-2, -3) == -5
