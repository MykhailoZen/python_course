students = {
    'Monika': 88, 'Rick': 98, 'Seth': 100, 'Tim': 99,
    'Simona': 91, 'Elvis': 85, 'Dora': 69,
    'Maria': 84, 'Nick': 71, 'Rocky': 77
}

to_continue = True

while to_continue:
    name = input("Enter student's name (or type 'Stop program' to exit): ").capitalize()

    if name.lower() == "stop program":
        print("Exiting the program. Goodbye!")
        to_continue = False
        break

    if name in students.keys():
        print(f"Student {name} has {students[name]} points.")
    else:
        print(f"No student {name} in the list.")
