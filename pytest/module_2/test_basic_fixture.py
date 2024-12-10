# 1 Create a new test file named test_basic_fixture.py.
# 2 Write a fixture named input_data that returns a dict with a predefined structure (a config with defined sections,
# for example).
# 3 Write a test function that validates input data.
from typing import List


def format_data_for_display(people: List[dict]) -> List[str]:
    return [person["given_name"] + " " + person["family_name"] + ": " + person["title"] for person in people]


def test_format_data_for_display(input_data):
    for data in input_data:
        assert list(data.keys()) == ["given_name", "family_name", "title"]
    assert format_data_for_display(input_data) == ["Hanna Semerenko: QAE", "Dmytro Lytvynenko: SDET"], \
        "Incorrect data after validation"
    assert input_data[0]["given_name"] == "Hanna", "say my name"
