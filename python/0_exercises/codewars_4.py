# Complete the solution so that it reverses all of the words within the string passed in.
# Words are separated by exactly one space and there are no leading or trailing spaces.
# Example(Input --> Output):
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"


def reverse_words_1(s: str) -> str:
    return " ".join(s.split(" ")[::-1])


def reverse_words_2(s: str) -> str:
    return " ".join(reversed(s.split(" ")))


if __name__ == "__main__":
    tests = {
        "hello world!": "world! hello",
        "The greatest victory is that which requires no battle": "battle no requires which that is victory greatest The",
    }
    for t in tests.keys():
        assert reverse_words_1(t) == tests[t]
        assert reverse_words_2(t) == tests[t]
