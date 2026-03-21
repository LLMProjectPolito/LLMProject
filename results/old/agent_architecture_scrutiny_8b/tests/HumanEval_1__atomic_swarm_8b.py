import pytest
import math

import pytest
from typing import List

def test_separate_paren_groups():
    """Test the function with a typical positive case."""
    from separate_groups import separate_paren_groups  # import the function to be tested

    # Typical positive case: Multiple balanced groups of nested parentheses
    input_string = '( ) (( )) (( )( ))'
    expected_output = ['()', '(())', '(()())']
    assert separate_paren_groups(input_string) == expected_output

import pytest
from typing import List

def test_empty_input():
    """ Test the function with an empty input string. """
    # Arrange
    input_string = ""

    # Act
    result = separate_paren_groups(input_string)

    # Assert
    assert result == []

import pytest
from typing import List

def test_separate_paren_groups_empty_string():
    """ Test for an empty string input """
    assert separate_paren_groups('') == []