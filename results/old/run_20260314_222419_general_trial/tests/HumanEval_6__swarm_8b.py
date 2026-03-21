import pytest
import math
from typing import List

def test_parse_nested_parens_empty_string():
    """ Test parsing an empty string. """
    result = parse_nested_parens('')
    assert result == [], "Expected empty list for empty input string"

@pytest.mark.parametrize("input_string, expected_output", [
    ("((( )))", [1, 1]),  # edge case: empty paren groups separated by spaces
])
def test_parse_nested_parens_edge_cases(input_string, expected_output):
    """ Test parse_nested_parens with edge cases """
    result = parse_nested_parens(input_string)
    assert result == expected_output