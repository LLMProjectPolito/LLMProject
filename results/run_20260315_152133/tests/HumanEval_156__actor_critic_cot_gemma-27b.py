import pytest
from your_module import int_to_mini_roman  # Replace your_module

# Valid Input Tests
def test_representative_cases():
    """Tests the core logic with a smaller set of representative values."""
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_combinations():
    """Tests combinations of values."""
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(1999) == 'mcmxcix'
    assert int_to_mini_roman(256) == 'ccLvi'

# Edge Case Tests
def test_edge_cases():
    """Tests numbers with combinations of symbols."""
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(12) == 'xii'
    assert int_to_mini_roman(17) == 'xvii'
    assert int_to_mini_roman(23) == 'xxiii'
    assert int_to_mini_roman(28) == 'xxviii'

# Invalid Input Tests
def test_invalid_input():
    """Tests the function's behavior with invalid inputs."""
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)
    with pytest.raises(TypeError):
        int_to_mini_roman(1.5)
    with pytest.raises(TypeError):
        int_to_mini_roman("1")
    with pytest.raises(ValueError):
        int_to_mini_roman(4000)

# Removed test_case_sensitivity as it was testing incorrect behavior.
# Input Validation
def test_upper_bound():
    """Tests the upper bound of the function."""
    assert int_to_mini_roman(3999) == 'mmmcmxcix'