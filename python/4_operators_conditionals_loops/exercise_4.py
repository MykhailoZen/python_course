# Create a program that will help to find out the student's points.
# The program prompts you to enter the student's name and, if successful, returns the following message Student <name>
# has <value> points and complete its execution.
# If such a name is not in the dictionary, the program should inform about this and offer to enter another name.
# There should also be a way to end the program by typing Stop program.
#
# Student grades (data for homework) Collapse source
# {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34,
# 'Michael': 31, 'Richard': 12}


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
name = input("Enter the student's name: ")
while name != "Stop program" and students.get(name) is None:
    name = input("Incorrect student's name!\nEnter the student's name: ")
else:
    (
        print(f"The student's points: {students.get(name)}\nExit!")
        if students.get(name) is not None
        else print("Exit!")
    )
