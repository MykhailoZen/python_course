import logging

import pytest

logger = logging.getLogger(__name__)


def file_operations(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        content = infile.read()
        outfile.write(content.upper())


@pytest.mark.parametrize('content_input', [
    'The text without any sense!',
    'Tabula Rasa',
    'C3PO',
    pytest.param('451!', marks=pytest.mark.skip(reason="Manuscripts don't burn"))
])
def test_data_processing_verification(temp_file_creation, content_input):
    input_file, output_file = temp_file_creation
    with open(input_file, 'w') as infile:
        infile.write(content_input)

    file_operations(input_file, output_file)

    with open(output_file, 'r') as outfile:
        content_output = outfile.read()
        assert content_input.upper() == content_output


def test_input_file_unchanged(temp_file_creation, cli_log_capture):
    input_file, output_file = temp_file_creation
    with open(input_file, 'w') as infile:
        content_input = 'The text without any sense!'
        infile.write(content_input)

    file_operations(input_file, output_file)
    logger.info('This is the message I was waiting for')

    with open(input_file, 'r') as infile:
        content_input_after_func = infile.read()
        assert content_input_after_func == content_input
