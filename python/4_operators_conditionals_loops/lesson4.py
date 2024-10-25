students = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}
name = input("Enter student name: ")
while name not in students:
    if name == "Stop program":
        exit()
    name = input("Enter another name ")
print("Student: "+name+" has "+str(students.get(name))+" points")