from src.main import multiplication

def test_multiplication_basic():
    assert multiplication(3, 4) == 12

def test_multiplication_by_zero():
    assert multiplication(9, 0) == 0
