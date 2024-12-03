import pytest
import tempfile
import os


@pytest.mark.skip(reason="Feature is not working")
def test_skipped(temp_files):
    input_file, output_file = temp_files
    input_file.write(b"hello world")
    input_file.close()
    data_processing(input_file, output_file)
    with open(output_file.name, "r") as f:
        assert f.read() == "HELLO WORLD"


@pytest.mark.xfail(reason="Expected failure due to known issue")
def test_expected_failure(temp_files):
    input_file, output_file = temp_files
    input_file.write(b"hello world")
    input_file.close()
    data_processing(input_file, output_file)
    with open(output_file.name, "r") as f:
        assert f.read() == "hello world"


@pytest.mark.parametrize(
    "input_data, expected_output",
    [("hello world", "HELLO WORLD"), ("test123", "TEST123"), ("abc", "ABC")],
)
def test_parametrized(temp_files, input_data, expected_output):
    input_file, output_file = temp_files
    input_file.write(input_data.encode())
    input_file.close()
    data_processing(input_file, output_file)
    with open(output_file.name, "r") as f:
        assert f.read() == expected_output


@pytest.fixture
def temp_files():
    input_file = tempfile.NamedTemporaryFile(delete=False)
    output_file = tempfile.NamedTemporaryFile(delete=False)
    yield input_file, output_file
    os.remove(input_file.name)
    os.remove(output_file.name)


def data_processing(input_file, output_file):
    with open(input_file.name, "r") as infile, open(output_file.name, "w") as outfile:
        data = infile.read()
        processed_data = data.upper()
        outfile.write(processed_data)


def test_data_processing(temp_files):
    input_file, output_file = temp_files
    input_file.write(b"hello world")
    input_file.close()
    data_processing(input_file, output_file)
    with open(output_file.name, "r") as f:
        assert f.read() == "HELLO WORLD"


def test_original_content_remains_unchanged(temp_files):
    input_file, output_file = temp_files
    original_content = "hello world"
    input_file.write(original_content.encode())
    input_file.close()
    data_processing(input_file, output_file)
    with open(input_file.name, "r") as f:
        assert f.read() == original_content