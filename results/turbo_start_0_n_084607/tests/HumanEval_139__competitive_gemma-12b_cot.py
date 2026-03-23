import pytest

def test_special_factorial_positive():
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 14400
    assert special_factorial(6) == 10368000

def test_special_factorial_large():
    assert special_factorial(7) == 86400000000
    assert special_factorial(8) == 870912000000000

def test_special_factorial_edge_case():
    assert special_factorial(0) == 1 # Should not raise error, return 1

def test_special_factorial_type_error():
    with pytest.raises(TypeError):
        special_factorial("a")
    with pytest.raises(TypeError):
        special_factorial(1.5)
    with pytest.raises(TypeError):
        special_factorial([1,2,3])

def test_special_factorial_negative():
    with pytest.raises(ValueError):
        special_factorial(-1)
    with pytest.raises(ValueError):
        special_factorial(-5)