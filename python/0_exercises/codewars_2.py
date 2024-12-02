# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F
def abbrev_name(name: str) -> str:
    return ".".join([n[0].upper() for n in name.split(" ")])


if __name__ == "__main__":
    tests = {"Sam Harris": "S.H", "patrick feenan": "P.F"}
    for t in tests.keys():
        assert abbrev_name(t) == tests[t]
