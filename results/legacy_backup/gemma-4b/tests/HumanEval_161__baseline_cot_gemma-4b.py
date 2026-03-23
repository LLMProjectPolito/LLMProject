import pytest
from solution import solve  # Assuming the function is in solution.py

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("", ""),
        ("1234", "4321"),
        ("ab", "AB"),
        ("#a@C", "#A@c"),
        ("hello", "HELLO"),
        ("WORLD", "world"),
        ("HeLlO", "hElLo"),
        ("123abc456", "654cb321"),
        ("!@#$%^", "^%$#@!"),
        ("a", "A"),
        ("1", "1"),
        (" ", " "),
        ("a b", "A B"),
        ("a123", "A123"),
        ("123a", "123A"),
        ("a123b", "A123B"),
        ("A123b", "a123B"),
        ("a123B", "A123b"),
        ("A123b", "a123B"),
        ("1234567890", "0987654321"),
        ("aBcDeFgHiJkLmNoPqRsTuVwXyZ", "A bCdeFgHiJkLmNoPqRsTuVwXyZ"),
    ],
)
def test_solve(input_string, expected_output):
    assert solve(input_string) == expected_output