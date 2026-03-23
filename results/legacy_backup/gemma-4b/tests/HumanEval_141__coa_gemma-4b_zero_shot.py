import pytest
import math


# Focus: Boundary Values
import pytest

def test_file_name_check_valid_1():
    assert file_name_check("example.txt") == "Yes"

def test_file_name_check_valid_2():
    assert file_name_check("data.dll") == "Yes"

def test_file_name_check_invalid_1():
    assert file_name_check("1example.dll") == "No"

def test_file_name_check_invalid_2():
    assert file_name_check("123.txt") == "No"

def test_file_name_check_invalid_3():
    assert file_name_check("example..txt") == "No"

def test_file_name_check_invalid_4():
    assert file_name_check("example.exe") == "No"

def test_file_name_check_invalid_5():
    assert file_name_check("example.pdf") == "No"

def test_file_name_check_invalid_6():
    assert file_name_check("example") == "No"

# Focus: Type Scenarios
import pytest

def test_type_scenario_1():
    assert file_name_check("example.txt") == "Yes"

def test_type_scenario_2():
    assert file_name_check("1example.dll") == "No"

def test_type_scenario_3():
    assert file_name_check("example.exe") == "Yes"

def test_type_scenario_4():
    assert file_name_check("example..txt") == "No"

def test_type_scenario_5():
    assert file_name_check("example.txt.txt") == "No"

def test_type_scenario_6():
    assert file_name_check("example.123") == "No"

def test_type_scenario_7():
    assert file_name_check("a.txt") == "Yes"

def test_type_scenario_8():
    assert file_name_check("A.TXT") == "Yes"

def test_type_scenario_9():
    assert file_name_check("1a.txt") == "No"

# Focus: Logic Branches
import pytest

def test_valid_file_name_one_dot():
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("data.dll") == "Yes"
    assert file_name_check("report.exe") == "Yes"

def test_invalid_file_name_no_dot():
    assert file_name_check("exampletxt") == "No"
    assert file_name_check("dataexe") == "No"
    assert file_name_check("reportdll") == "No"

def test_invalid_file_name_multiple_dots():
    assert file_name_check("example..txt") == "No"
    assert file_name_check("example.txt.bak") == "No"

def test_invalid_file_name_digit_count():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("12example.txt") == "No"
    assert file_name_check("123example.txt") == "No"

def test_invalid_file_name_prefix():
    assert file_name_check("1example.txt") == "No"
    assert file_name_check("0example.txt") == "No"
    assert file_name_check("2example.txt") == "No"

def test_invalid_file_name_suffix():
    assert file_name_check("example.txt.pdf") == "No"
    assert file_name_check("example.txt.jpg") == "No"