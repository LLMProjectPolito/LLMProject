
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

import pytest

@pytest.mark.parametrize("input_text, expected", [
    # --- Identity & No Spaces ---
    pytest.param("", "", id="empty_string"),
    pytest.param("Hello", "Hello", id="no_spaces_alpha"),
    pytest.param("12345", "12345", id="no_spaces_numeric"),
    pytest.param("!@#$%", "!@#$%", id="no_spaces_symbols"),

    # --- Single Space (Rule: 1 space -> "_") ---
    pytest.param("a b", "a_b", id="single_space_middle"),
    pytest.param(" a ", "_a_", id="single_space_leading_trailing"),
    pytest.param(" a", "_a", id="single_space_leading"),
    pytest.param("a ", "a_", id="single_space_trailing"),
    pytest.param(" ", "_", id="only_single_space"),

    # --- Double Space (Rule: 2 spaces -> "__") ---
    pytest.param("a  b", "a__b", id="double_space_middle"),
    pytest.param("  a  ", "__a__", id="double_space_leading_trailing"),
    pytest.param("  a", "__a", id="double_space_leading"),
    pytest.param("a  ", "a__", id="double_space_trailing"),
    pytest.param("  ", "__", id="only_double_space"),

    # --- Triple or More Spaces (Rule: 3+ spaces -> "-") ---
    pytest.param("a   b", "a-b", id="triple_space_middle"),
    pytest.param("a    b", "a-b", id="quad_space_middle"),
    pytest.param("a     b", "a-b", id="multi_space_middle"),
    pytest.param("   a", "-a", id="triple_space_leading"),
    pytest.param("a   ", "a-", id="triple_space_trailing"),
    pytest.param("   ", "-", id="only_triple_space"),
    pytest.param("    ", "-", id="only_quad_space"),
    pytest.param("     ", "-", id="only_multi_space"),

    # --- Complex Mixed Patterns ---
    pytest.param("a b  c   d", "a_b__c-d", id="mixed_1_2_3"),
    pytest.param("  a b   c d ", "__a_b-c_d_", id="mixed_complex_start_end"),
    pytest.param("a    b  c b", "a-b__c_b", id="mixed_4_2_1"),
    pytest.param("a b  c   d    e", "a_b__c-d-e", id="mixed_long_sequence"),
    pytest.param(" Example   3", "_Example-3", id="mixed_leading_trailing"),
    pytest.param("  Multiple   Spaces  Test ", "__Multiple-Spaces__Test_", id="mixed_very_complex"),
])
def test_fix_spaces_logic(input_text, expected):
    """Tests all logical branches of space replacement via comprehensive parametrization."""
    from __main__ import fix_spaces
    assert fix_spaces(input_text) == expected

def test_fix_spaces_type_error():
    """Verifies that non-string inputs raise a TypeError."""
    from __main__ import fix_spaces
    invalid_inputs = [None, 123, 45.6, [], {}, True]
    for val in invalid_inputs:
        with pytest.raises(TypeError):
            fix_spaces(val)

def test_fix_spaces_consistency():
    """Ensures the function is deterministic (idempotent for the same input)."""
    from __main__ import fix_spaces
    input_val = "Complex   string  with  many    spaces"
    assert fix_spaces(input_val) == fix_spaces(input_val)