import pytest
import math


# Focus: Boundary Values
import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

### SCoT Steps:
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function calculates the MD5 hash of a string. Boundary values to test include empty strings and strings with extreme characters.
### STEP 2: PLAN - List test functions names and scenarios.
### test_string_to_md5_empty
### test_string_to_md5_short
### test_string_to_md5_long
### STEP 3: CODE - Write the high-quality pytest suite.

def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_short():
    assert string_to_md5("a") == "2536570d8c774b6a8a86d6476964965a"

def test_string_to_md5_long():
    assert string_to_md5("This is a very long string to test the MD5 hash function.") == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

# Focus: Type Scenarios
import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_simple_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_numbers():
    assert string_to_md5("12345") == 'b94d27b9934d3e08a52e52d46d1ff81a'

# Focus: Logic Branches
import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_simple_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_spaces():
    assert string_to_md5("  Test string  ") == "2c1f8a8a98a9901333836678a98a98a9"