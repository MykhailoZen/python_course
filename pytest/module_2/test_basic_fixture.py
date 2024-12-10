# 1 Create a new test file named test_basic_fixture.py.
# 2 Write a fixture named input_data that returns a dict with a predefined structure (a config with defined sections,
# for example).
# 3 Write a test function that validates input data.
import pytest
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


def format_data_for_display(people: List[dict]) -> List[str]:
    return [person["given_name"] + " " + person["family_name"] + ": " + person["title"] for person in people]


def test_format_data_for_display(input_data: List[dict]):
    assert format_data_for_display(input_data) == ["Hanna Semerenko: QAE", "Dmytro Lytvynenko: SDET"], \
        "Incorrect data after validation"
