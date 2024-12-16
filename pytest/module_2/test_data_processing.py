# 1. Create a new test file named test_data_processing.py.
# 2. Create a Pytest fixture to handle temporary files. This fixture should:
#
# - Create a temporary file for writing before each test.
# - Yield the file object to the test.
# - Deletes the temporary file after the test is complete.
# - Advanced task (optional): add "--keep-temp-files" Pytest parameter to keep the temporary files after test execution.
# 3. Use the fixture to get two temporary file objects - one for input and one for output.
# 4. Write a function that reads data form input file, does some data processing (converts everything to UPPER case, for
# example) and writes result into the output file.
# 5. Write a test that tests data processing function - writes something into the input file, call the function under test
# and verify its result.
# 6. Write a second test case that checks if the original content of the temporary file remains unchanged after the data
# processing.

from pathlib import Path

import pytest


def data_processing(output_file: Path, input_file: Path):
    output_file.write_text(input_file.read_text().upper())


def test_data_processing(files_operations):
    content = "test data"
    input_file, output_file = files_operations
    input_file.write_text(content)
    data_processing(output_file, input_file)
    assert output_file.read_text() == content.upper(), "Wrong output file content"
    assert input_file.read_text() == content, "Wrong input file content"
    assert output_file.read_text() == input_file.read_text.upper(), "Function doesn't work as expected"
