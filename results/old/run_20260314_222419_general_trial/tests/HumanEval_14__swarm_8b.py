import pytest
import math
from typing import List

def test_all_prefixes_empty_string():
    """Edge case: Input string is empty"""
    assert all_prefixes('') == ['']

def test_all_prefixes_non_empty_string():
    """Test case: Input string is not empty"""
    assert all_prefixes("test") == ["", "t", "te", "tes", "test"]

def test_all_prefixes_single_character_string():
    """Test case: Input string is a single character"""
    assert all_prefixes("a") == ["", "a"]