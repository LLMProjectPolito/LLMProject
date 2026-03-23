import pytest

# The function int_to_mini_roman is assumed to be imported in the test environment.


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, "i"),
        (4, "iv"),
        (5, "v"),
        (9, "ix"),
        (10, "x"),
        (40, "xl"),
        (44, "xliv"),
        (49, "xlix"),
        (50, "l"),
        (90, "xc"),
        (99, "xcix"),
        (100, "c"),
        (400, "cd"),
        (444, "cdxliv"),
        (500, "d"),
        (900, "cm"),
        (944, "cmxliv"),
        (1000, "m"),
        (19, "xix"),
        (152, "clii"),
        (426, "cdxxvi"),
    ],
)
def test_int_to_mini_roman_valid_cases(number, expected):
    """Test typical, boundary and subtractive cases."""
    result = int_to_mini_roman(number)
    assert isinstance(result, str), "Result should be a string"
    assert result == expected, f"Roman numeral for {number} should be {expected}"
    assert result.islower(), "Result should be in lowercase"


@pytest.mark.parametrize(
    "invalid_input",
    [
        0,          # below lower bound
        -5,         # negative number
        1001,       # above upper bound
        3.14,       # non‑integer (float)
        "X",        # non‑integer (string)
        None,       # NoneType
        [],         # other iterable
    ],
)
def test_int_to_mini_roman_invalid_inputs(invalid_input):
    """Function should raise an exception for out‑of‑range or non‑integer inputs."""
    with pytest.raises(Exception):
        int_to_mini_roman(invalid_input)