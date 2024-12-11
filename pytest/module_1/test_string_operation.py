# Create a new test file named test_string_operations.py.
# Write a function to check if a given string is equal to its reversed version (a string is palindrome).
# Write several tests to verify if a string is palindrome.
# Use test filtering to run only the tests from the test_string_operations.py file.
# Use marker filtering to run only the palindrome test from the test_string_operations.py file.
import pytest


def palindrome(str_for_check: str) -> bool:
    return str_for_check.lower().replace(' ', '') == str_for_check.lower().replace(' ', '')[::-1]

@pytest.mark.P0
@pytest.mark.parametrize("str_for_check", ['Do geese see God', 'noon', 'racecar'])
def test_palindrome(str_for_check: str):
    assert palindrome(str_for_check), f"This string '{str_for_check}' is not palindrome"

@pytest.mark.P1
@pytest.mark.parametrize("str_for_check", ['miaw'])
def test_not_palindrome(str_for_check: str):
    assert not palindrome(str_for_check), f"This string '{str_for_check}' is palindrome"
