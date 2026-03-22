import pytest

# Assuming int_to_mini_roman is already imported or defined in the test scope.

@pytest.mark.parametrize(
    "value,expected",
    [
        (1, "i"),          # minimum allowed value
        (1000, "m"),       # maximum allowed value (duplicate check)
        (999, "cmxcix"),   # upper‑boundary with multiple subtractive notations
        (944, "cmxliv"),   # complex subtractive combination: 900 + 40 + 4
    ],
)
def test_int_to_mini_roman(value, expected):
    assert int_to_mini_roman(value) == expected