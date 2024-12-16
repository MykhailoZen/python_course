# 1. Create a new test file named test_basic_fixture.py.
# 2. Write a fixture named input_data that returns a dict with a predefined structure (a config with defined sections,
# for example).
# 3. Write a test function that validates input data.

def test_basic_fixture(input_data):
    assert input_data["name"] == "Bob", "Name should be Bob"
    assert input_data["age"] == 30, "Age should be 30"
    assert input_data["sex"] == "Male", "Gender should be Male"