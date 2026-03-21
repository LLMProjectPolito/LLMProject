import pytest

def test_change_base_base_2():
    assert change_base(8, 2) == '1000'
    assert change_base(7, 2) == '111'
    assert change_base(6, 2) == '110'
    assert change_base(5, 2) == '101'
    assert change_base(4, 2) == '100'
    assert change_base(3, 2) == '11'
    assert change_base(2, 2) == '10'
    assert change_base(1, 2) == '1'
    assert change_base(0, 2) == '0'

def test_change_base_base_3():
    assert change_base(8, 3) == '22'
    assert change_base(7, 3) == '21'
    assert change_base(6, 3) == '20'
    assert change_base(5, 3) == '12'
    assert change_base(4, 3) == '11'
    assert change_base(3, 3) == '10'
    assert change_base(2, 3) == '2'
    assert change_base(1, 3) == '1'
    assert change_base(0, 3) == '0'

def test_change_base_base_4_to_9():
    for base in range(4, 10):
        assert change_base(0, base) == '0'
        assert change_base(1, base) == '1'
        assert change_base(base - 1, base) == str(base - 1)
        assert change_base(base, base) == '10'
        assert change_base(base + 1, base) == '11'

def test_change_base_invalid_base():
    with pytest.raises(ValueError):
        change_base(8, 1)
    with pytest.raises(ValueError):
        change_base(8, 10)
    with pytest.raises(ValueError):
        change_base(8, -1)

def test_change_base_invalid_input():
    with pytest.raises(ValueError):
        change_base(-1, 2)
    with pytest.raises(ValueError):
        change_base(-8, 2)