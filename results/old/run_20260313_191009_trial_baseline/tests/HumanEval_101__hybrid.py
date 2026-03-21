import pytest

@pytest.mark.parametrize("input_string, expected_output", [
    ("Hi, my name is John", ["Hi", "my", "name", "is", "John"]),
    ("One, two, three, four, five, six", ["One", "two", "three", "four", "five", "six"]),
    ("Hello world", ["Hello", "world"]),
    ("Single", ["Single"]),
    ("", []),
    (",", ["", ""]),
    (" , ", ["", ""]),
    ("Hello, world this is a test", ["Hello", "world", "this", "is", "a", "test"]),
    ("Hello, world,", ["Hello", "world"]),
    ("Hello   world", ["Hello", "world"]),
    ("a,,b,,c", ["a", "", "b", "", "c"]),
    ("a  b  c", ["a", "b", "c"]),
    ("   a, b, c  ", ["a", "b", "c"]),
    (",a,b,c,", ["", "a", "b", "c", ""]),
])
def test_words_string(input_string, expected_output):
    assert words_string(input_string) == expected_output

def test_words_string_with_mixed_separators():
    assert words_string("Hello, world this is a test") == ["Hello", "world", "this", "is", "a", "test"]

def test_words_string_with_leading_trailing_spaces():
    assert words_string("   a, b, c  ") == ["a", "b", "c"]

def test_words_string_with_leading_trailing_commas():
    assert words_string(",a,b,c,") == ["", "a", "b", "c", ""]

def test_words_string_with_consecutive_commas():
    assert words_string("a,,b,,c") == ["a", "", "b", "", "c"]

def test_words_string_with_consecutive_spaces():
    assert words_string("a  b  c") == ["a", "b", "c"]