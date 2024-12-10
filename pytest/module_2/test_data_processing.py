# 1 Create a new test file named test_data_processing.py.
# 2 Create a Pytest fixture to handle temporary files. This fixture should:
# - Create a temporary file for writing before each test.
# - Yield the file object to the test.
# - Deletes the temporary file after the test is complete.
# - Advanced task (optional): add "--keep-temp-files" Pytest parameter to keep the temporary files after test execution.
# 3 Use the fixture to get two temporary file objects - one for input and one for output.
# 4 Write a function that reads data form input file, does some data processing (converts everything to UPPER case,
# for example) and writes result into the output file.
# 5 Write a test that tests data processing function - writes something into the input file, call the function under
# test and verify its result.
# 6 Write a second test case that checks if the original content of the temporary file remains unchanged after the data
# processing.
import pytest
from pathlib import PosixPath


def data_processing(file1: PosixPath, file2: PosixPath):
    file2.write_text(file1.read_text().upper())


@pytest.mark.parametrize('content', ['content_1', 'conTEnt_2'])
def test_data_processing(create_files, content):
    """
    Test data_processing function
    """
    input_file, output_file = create_files
    input_file.write_text(content)
    data_processing(input_file, output_file)
    assert input_file.read_text() == content, f"incorrect content in input_file={input_file.name}"
    assert output_file.read_text() == content.upper(), f"incorrect content in output_file={output_file.name}"
    assert input_file.read_text().upper() == output_file.read_text(), "content not expected"


@pytest.mark.parametrize('content', ['content_1'])
def test_data_processing_failed(create_files, content):
    """
    failed test for reruns
    """
    input_file, output_file = create_files
    input_file.write_text(content)
    data_processing(input_file, output_file)
    assert input_file.read_text().upper() == content, f"incorrect content in input_file={input_file.name}"


@pytest.mark.skip(reason="Skipping this test for now")
@pytest.mark.parametrize('content', ['content_1', 'conTEnt_2'])
def test_data_processing_for_skipp(create_files, content):
    """
    skipped test
    """
    input_file, output_file = create_files
    input_file.write_text(content)
    data_processing(input_file, output_file)
    assert input_file.read_text() == content, f"incorrect content in input_file={input_file.name}"


@pytest.mark.xfail(reason="Expected failure due to known issue")
@pytest.mark.parametrize('content', ['content_1', 'conTEnt_2'])
def test_data_processing_for_xfail(create_files, content):
    """
    xfail test
    """
    input_file, output_file = create_files
    input_file.write_text(content)
    data_processing(input_file, output_file)
    assert input_file.read_text() == content.upper(), f"incorrect content in input_file={input_file.name}"

# pytest --reruns 3 --reruns-delay 2 ./pytest/module_2/
# 1 failed, 3 passed, 2 skipped, 2 xfailed, 3 rerun in 6.11s
