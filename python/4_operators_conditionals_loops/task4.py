students = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34,
            'Michael': 31, 'Richard': 12}

while True:
    name = input("Enter student name: ")
    if name in students:
        print(f"Student {name} has {students[name]} points")
    elif name == "Stop program":
        break
    else:
        print(f"Student {name} not in the list")