import pytest

@pytest.mark.parametrize("input_string, expected_output", [
    ("Hi, my name is John", ["Hi", "my", "name", "is", "John"]),
    ("One, two, three, four, five, six", ["One", "two", "three", "four", "five", "six"]),
    ("Single word", ["Single", "word"]),
    ("Multiple   spaces", ["Multiple", "spaces"]),
    ("No spaces or commas", ["No", "spaces", "or", "commas"]),
    ("Leading and trailing spaces   ", ["Leading", "and", "trailing", "spaces"]),
    ("", []),
    (",", []),
    (" , ", []),
    (",, ,", []),
    ("a, b, c", ["a", "b", "c"]),
    ("a b c", ["a", "b", "c"]),
    ("a, b c", ["a", "b", "c"]),
    ("a b, c", ["a", "b", "c"]),
    ("One, two three, four, five six", ["One", "two", "three", "four", "five", "six"]),
    ("One, two! three, four? five, six.", ["One", "two!", "three", "four?", "five", "six."]),
    ("One, 2 three, four 5, six", ["One", "2", "three", "four", "5", "six"]),
    ("One, @two three, #four 5, $six", ["One", "@two", "three", "#four", "5", "$six"]),
])
def test_words_string(input_string, expected_output):
    assert words_string(input_string) == expected_output

def test_words_string_with_leading_trailing_spaces():
    input_string = "   a, b, c   "
    expected_output = ["a", "b", "c"]
    assert words_string(input_string) == expected_output

def test_words_string_with_multiple_consecutive_spaces():
    input_string = "a   b   c"
    expected_output = ["a", "b", "c"]
    assert words_string(input_string) == expected_output

def test_words_string_with_multiple_consecutive_commas():
    input_string = "a,,b,,c"
    expected_output = ["a", "b", "c"]
    assert words_string(input_string) == expected_output