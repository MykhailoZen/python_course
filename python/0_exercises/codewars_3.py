# Write a function to split a string and convert it into an array of words.
#
# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]
#
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
from typing import List


def string_to_array(s: str) -> List[str]:
    return s.split(" ")


if __name__ == "__main__":
    tests = {
        "Robin Singh": ["Robin", "Singh"],
        "CodeWars": ["CodeWars"],
        "I love arrays they are my favorite": [
            "I",
            "love",
            "arrays",
            "they",
            "are",
            "my",
            "favorite",
        ],
        "1 2 3": ["1", "2", "3"],
        "": [""],
    }
    for t in tests.keys():
        assert string_to_array(t) == tests[t]
