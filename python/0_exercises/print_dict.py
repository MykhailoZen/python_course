import json
from pprint import pprint

students = {
    "Alan": 68,
    "Roslyn": 48,
    "Bertha": 50,
    "Sally": 95,
    "Rachel": 11,
    "John": 95,
    "Derek": 82,
    "Kevin": 34,
    "Michael": 31,
    "Richard": 12,
}

# version 1
print(json.dumps(students, indent=4, sort_keys=True))
print("___________________________")


# version 2
pprint(students)
print("___________________________")

# version 3
for key, value in students.items():
    print("{0}: {1}".format(key, value))
