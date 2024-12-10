import pytest
from pathlib import PosixPath
import os
from typing import List


@pytest.fixture
def input_data() -> List[dict]:
    return [
        {
            "given_name": "Hanna",
            "family_name": "Semerenko",
            "title": "QAE",
        },
        {
            "given_name": "Dmytro",
            "family_name": "Lytvynenko",
            "title": "SDET",
        },
    ]


@pytest.fixture()
def create_files(tmp_path: PosixPath):
    temp_dir = tmp_path / "my_temp_dir"
    temp_dir.mkdir()
    input_file = temp_dir / "test_file_1.txt"
    output_file = temp_dir / "test_file_2.txt"
    yield input_file, output_file
    os.remove(input_file)
    os.remove(output_file)
