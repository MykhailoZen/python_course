"""
1. Create a new test file named test_data_processing.py.
2. Create a Pytest fixture to handle temporary files. This fixture should:
- Create a temporary file for writing before each test.
- Yield the file object to the test.
- Deletes the temporary file after the test is complete.
- Advanced task (optional): add "--keep-temp-files" Pytest parameter to keep the temporary files after test execution.
3. Use the fixture to get two temporary file objects - one for input and one for output.
4. Write a function that reads data form input file, does some data processing
 (converts everything to UPPER case, for example) and writes result into the output file.
5. Write a test that tests data processing function - writes something into the input file,
 call the function under test and verify its result.
6. Write a second test case that checks if the original content of the temporary file
remains unchanged after the data processing.
"""

"""
#TASK 4
#Extend the test_data_processing module with a patamertized test to verify multiple scenarios with different input values. 
"""

import pytest


def process_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()
        data = data.upper()
    with open(output_file, 'w') as f:
        f.write(data)


#-----------------------------------------------------------------------------
@pytest.mark.parametrize("input_file_data",
                         ["this is test text to deal with fixtures.",
                          1234567890,
                          "%#*&%(*!@!%)"])
def test_data_processing(input_file_data, temp_file_handler):
    if type(input_file_data) is not str:
        pytest.skip("Input data is not a string.")

    input_file = temp_file_handler()
    output_file = temp_file_handler()

    with open(input_file.name, 'w') as f:
        f.write(input_file_data)

    process_data(input_file.name, output_file.name)

    with open(output_file.name, 'r') as f:
        result = f.read()
    assert result == input_file_data.upper()

 # --------------------------------------------------------------

@pytest.mark.parametrize("input_file_data",
                        ["this is test text to deal with fixtures.",
                         1234567890,
                         "%#*&%(*!@!%)"])
def test_input_unchanged(input_file_data, temp_file_handler):
    if type(input_file_data) is not str:
        pytest.xfail("Input data is not a string.")

    input_file = temp_file_handler()
    output_file = temp_file_handler()
    with open(input_file.name, 'w') as f:
        f.write(input_file_data)

    process_data(input_file.name, output_file.name)

    with open(input_file.name, 'r') as f_in:
        result = f_in.read()

    assert result == input_file_data




