# Create a program that will help to find out the student's points.
# The program prompts you to enter the student's name and, if successful, returns the following message Student <name> has <value> points and complete its execution.
# If such a name is not in the dictionary, the program should inform about this and offer to enter another name.
# There should also be a way to end the program by typing Stop program.

# Creating of the database with students names and their points
student_grades = {'Alan': 68,
                  'Roslyn': 48,
                  'Bertha': 50,
                  'Sally': 95,
                  'Rachel': 11,
                  'John': 95,
                  'Derek': 82,
                  'Kevin': 34,
                  'Michael': 31,
                  'Richard': 12
                  }

print('You can find the students points for the following students:')
for x in student_grades:
    print(x)

student_name = input('Enter the name of a student or enter "Stop the program": ')

if student_name != 'Stop the program':
    while student_name not in student_grades:
        if student_name != 'Stop the program':
            print(f'There is no {student_name} in the school')
            student_name = input('Please enter another name or enter "Stop the program": ')
        else:
            print('You stopped the program')
            break
    else:
        print(f'Student {student_name} has {student_grades[student_name]} points')
else:
    print('You stopped the program')
   