# Create a new test file named test_string_operations.py.
# Write a function to check if a given string is equal to its reversed version (a string is palindrome).
# Write several tests to verify if a string is palindrome.
# Use test filtering to run only the tests from the test_string_operations.py file.
# Use marker filtering to run only the palindrome test from the test_string_operations.py file.

import pytest

def reverse(string: str):
    if string == string[::-1]:
        return "string is palindrome"

@pytest.mark.parametrize('string',['abccba', 'pop', 'LOL'])
def test_true_reverse(string):
    assert reverse(string), "string is not palindrome"

@pytest.mark.parametrize('string',['abccba pop LOL', 'In God We Trust'])
def test_false_reverse(string):
    assert not reverse(string), "string is palindrome"