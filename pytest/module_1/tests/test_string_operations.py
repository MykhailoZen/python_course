# 1 Create a new test file named test_string_operations.py.
# 2 Write a function to check if a given string is equal to its reversed version (a string is palindrome).
# 3 Write several tests to verify if a string is palindrome.
# 4 Use test filtering to run only the tests from the test_string_operations.py file.
# 5 Use marker filtering to run only the palindrome test from the test_string_operations.py file.

# pytest -m P0 ./pytest/module_1/test_string_operations.py
import pytest


@pytest.mark.P0
@pytest.mark.parametrize('string_for_test', ['amanaplanacanalpanama', 'abcddcba'])
def test_palindrome(string_for_test: str):
    assert string_for_test[::-1] == string_for_test, "This string is not palindrome"


@pytest.mark.P0
@pytest.mark.parametrize('string_for_test', ['tryt'])
def test__is_not_palindrome(string_for_test: str):
    assert string_for_test[::-1] != string_for_test, "This string is not palindrome"
