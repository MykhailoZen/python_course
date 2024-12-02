# You need to write a function that reverses the words in a given string. Words are always separated by a single space.
#
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
#
# Example (Input --> Output)
#
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
# Happy coding!


def reverse(st: str) -> str:
    return " ".join(st.split()[::-1])


if __name__ == "__main__":
    tests = {"Hello World": "World Hello", "Hi There.": "There. Hi"}
    for t in tests.keys():
        assert reverse(t) == tests[t]
