import pytest
import math

def test_separate_paren_groups_empty_string():
    """ Test that an empty string returns an empty list. """
    assert separate_paren_groups("") == []

def test_separate_nested_parentheses():
    result = separate_paren_groups('()()((()))')
    expected = ['()', '()', '((()))']
    assert result == expected, f"Expected {expected} but got {result}"

def test_separate_paren_groups_single_group():
    result = separate_paren_groups('()')
    expected = ['()']
    assert result == expected, f"Expected {expected} but got {result}"

def test_separate_paren_groups_multiple_groups():
    result = separate_paren_groups('(())(())')
    expected = ['(())', '(())']
    assert result == expected, f"Expected {expected} but got {result}"

def test_separate_paren_groups_no_parentheses():
    result = separate_paren_groups('abcdefg')
    expected = []
    assert result == expected, f"Expected {expected} but got {result}"