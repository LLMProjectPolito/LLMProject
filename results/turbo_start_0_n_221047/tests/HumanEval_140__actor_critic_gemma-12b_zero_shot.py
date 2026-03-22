import pytest
from your_module import fix_spaces  # Replace your_module

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "-Example_2"

def test_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_multiple_consecutive_spaces():
    assert fix_spaces("This  is   a    test") == "This_is-a-test"

def test_mixed_spaces():
    assert fix_spaces("  Hello  World  ") == "-Hello_World-"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_spaces_at_beginning_and_end():
    assert fix_spaces("  Test  ") == "-Test-"

def test_long_string_with_multiple_spaces():
    long_string = "This is a very long string with many spaces.   It has  multiple   consecutive   spaces."
    expected_result = "This_is_a_very_long_string_with_many_spaces.-It_has-multiple-consecutive-spaces."
    assert fix_spaces(long_string) == expected_result

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_mixed_whitespace():
    assert fix_spaces("Example\t 1 \n 2") == "Example_1_2"

def test_string_with_only_consecutive_spaces_at_start():
    assert fix_spaces("   Example") == "-Example"

def test_string_with_only_consecutive_spaces_at_end():
    assert fix_spaces("Example   ") == "Example-"

def test_string_with_only_tabs():
    assert fix_spaces("\t\t") == "-"

def test_string_with_only_newlines():
    assert fix_spaces("\n\n") == "-"

def test_string_with_tabs_and_newlines():
    assert fix_spaces("\t\n\n") == "-"

def test_string_with_numbers_and_special_characters():
    assert fix_spaces("Test 123!@#") == "Test_123!@#"

def test_mix_of_tabs_newlines_and_spaces():
    assert fix_spaces("  Example\t1\n2  ") == "-Example_1_2-"

def test_empty_string_with_whitespace():
    assert fix_spaces("   ") == "-"

def test_unicode_whitespace():
    assert fix_spaces("Example\u200B1") == "Example_1"

def test_mixed_hyphens_newlines_tabs():
    assert fix_spaces("-\t\n-") == "-_-_"

def test_non_string_input():
    with pytest.raises(TypeError):
        fix_spaces(123)