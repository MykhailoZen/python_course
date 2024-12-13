"""
1. Create a new test file named test_string_operations.py.
2. Write a function to check if a given string is equal to its reversed version (a string is palindrome).
3. Write several tests to verify if a string is palindrome.
4. Use test filtering to run only the tests from the test_string_operations.py file.
5. Use marker filtering to run only the palindrome test from the test_string_operations.py file.

In the test_string_operations.py file, add a marker "P0" to one positive and one negative tests.

"""
import pytest

def is_palindrome(string):
    return string == string[::-1]

@pytest.mark.palindrome
@pytest.mark.P0
def test_is_palindrome():
    assert is_palindrome("depomytymoped") == True
    assert is_palindrome("did") == True
    assert is_palindrome("umuminimumu") == True

@pytest.mark.not_palindrome
@pytest.mark.P0
def test_is_not_palindrome():
    assert is_palindrome("janesugusenja") == False
    assert is_palindrome("didizaraz") == False

@pytest.mark.not_palindrome
def test_is_palindrome_a_letter():
    assert is_palindrome("a") == True
    assert is_palindrome("R") == True

@pytest.mark.not_palindrome
def test_is_palindrome_with_punctuation():
    assert is_palindrome("Do geese see God?") == False
